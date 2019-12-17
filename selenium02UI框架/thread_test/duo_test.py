#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
import time
import json
from lxml import etree
import threading
from queue import Queue

# 存放采集线程
g_crawl_list = []
# 存放解析线程
g_parse_list = []

class CrawlThread(threading.Thread):
    def __init__(self,name,page_queue,data_queue):
        super(CrawlThread,self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jiantu-{}'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }

    def run(self):
        print('%s------线程启动'%self.name)
        while True:
            # 从队列中去页码
            page = self.page_queue.get()
            # 拼接url，发送请求
            url = self.url.format(page)
            r = requests.get(url,headers=self.headers)
            # 将相应内容放在data_queue
            self.data_queue.put(r.text)
        print('%s------线程结束'%self.name)


class ParseThread(threading.Thread):
    def __init__(self,name,data_queue,fp,lock):
        super(ParseThread,self).__init__()
        self.name = name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        print('%s------线程启动'%self.name)
        while True:
            if self.data_queue.empty():
                break
            # 从data_queue取数据
            data = self.data_queue.get()
            # 解析内容
            self.parse_content(data)

    def parse_content(self,data):
        tree = etree.HTML(data)
        # 获取图片url
        li_list = tree.xpath('//ul[@class="cont-list"]/li')
        items = []
        for o in li_list:
            title = o.xpath('.//h2/a/text()')[0]
            image_url = o.xpath('.//div[contains(@class,"cont-list-main")]/a/p/img/@src')
            item = {'标题' : title,
                    'url' : image_url}
            items.append(item)

        self.lock.acquire()
        self.fp.write(json.dumps(items,ensure_ascii=False)+'\n')
        self.lock.release()

def create_queue():
    # 创建页码队列
    page_queue = Queue()
    for page in range(1,51):
        page_queue.put(page)
    # 创建内容队列
    data_queue = Queue()
    return data_queue,page_queue

# 创建采集线程
def create_crawl_thread(page_queue,data_queue):
    crawl_name = ['采集线程1号', '采集线程2号', '采集线程3号']
    for name in crawl_name:
        # 创建一个采集线程
        tcrawl = CrawlThread(name,page_queue,data_queue)
        g_crawl_list.append(tcrawl)

# 创建解析线程
def create_parse_thread(data_queue,fp,lock):
    parse_name = ['解析线程1号', '解析线程2号', '解析线程3号']
    for name in parse_name:
        # 创建一个解析线程
        tparse = ParseThread(name,data_queue,fp,lock)
        g_parse_list.append(tparse)


def main():
    # 创建队列
    data_queue,page_queue = create_queue()
    # 打开文件
    fp = open('test.json','a')
    # 创建锁
    lock = threading.Lock()
    # 创建采集线程
    create_crawl_thread(page_queue,data_queue)
    time.sleep(3)
    # 创建解析线程
    create_parse_thread(data_queue,fp,lock)

    # 启动所有采集线程
    for tcrawl in g_crawl_list:
        tcrawl.start()
    # 启动所有解析线程
    for gparse in g_parse_list:
        gparse.start()

    # 主线程等待子线程结束
    for tcrawl in g_crawl_list:
        tcrawl.join()
    for gparse in g_parse_list:
        gparse.join()

    fp.close()
    print('线程全部结束')
if __name__ == '__main__':
    main()