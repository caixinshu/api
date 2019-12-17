#  -*- coding: utf-8 -*-
__author__ = 'liyingfeng'
from selenium import webdriver
import time
def is_brower(uchar,url):
    if uchar==1:
            driver = webdriver.Firefox()
            driver.implicitly_wait(30)
            driver.get(url)
            print("打开了火狐浏览器")
            driver.maximize_window()
            return driver
    elif uchar==2:
            driver =webdriver.Chrome("D:\\PycharmProjects\\uitestframework\\lib\\chromedriver.exe")
            driver.implicitly_wait(30)
            driver.get(url)
            print("打开了谷歌浏览器")
            driver.maximize_window()
            time.sleep(2)
            return driver
    else:
        driver =webdriver.Ie()
        driver.implicitly_wait(30)
        driver.get(url)
        driver.maximize_window()
        return driver
if __name__=='__main__':
  #函数调用
  is_brower(2,'http://www.baidu.com')