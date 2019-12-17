# coding=utf-8

import requests
from bs4 import BeautifulSoup as bs
import re 


def GetFromBaidu(word,pageout):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	for k in range(10,(pageout-1)*10,10):
		url = 'https://www.baidu.coms?wd='+ word+'&pn=' + str(k)
		html = requests.get(url=url,headers=headers,timeout=5)
		soup = bs(html.content,'lxml',from_encoding='utf-8')
		bqs = soup.find_all(name='a',attrs={'data-click':re.compile(r'.'),'class':None})
		
		for i in bqs:
			r = requests.get(i['href'],headers=headers,timeout=5)
			print r.url

if __name__ == '__main__':
	GetFromBaidu('php?id=',10)
