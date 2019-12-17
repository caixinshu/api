# coding=utf-8
# src = 123123123
# digits = 4 if isinstance(src,unicode) else 2
# print "%0*x"
# import base64


# print base64.__file__

import re
import requests
from bs4 import BeautifulSoup

# p = re.compile("hello")
# ma = p.match("hello you ")
# word = "http://shop.10086.com/admi/login. PHP"
# print re.findall('i.',word)
# print re.findall('\.',word)
# print re.findall('\d',word)
# print re.findall('\D',word)
# print re.findall('\s',word)
# print re.findall('\S',word)
# print re.findall('\w',word)
# print re.findall('\W',word)
# print re.findall('shop*',word)
# print re.findall('p+',word)
# s = "abbbc"
# print re.findall('ab*',s)
# print re.findall('ab*?',s)
# string = '''
# 		<a dcs_id="nav_recharge_more_1_1" class="ac_dcs_base" href="https://shop.10086.cn/i/service/recharge/item/itemcollect_100_100_30.html" target="_blank">30元</a>
# 		<a dcs_id="nav_recharge_more_1_2" class="ac_dcs_base" href="https://shop.10086.cn/i/service/recharge/item/itemcollect_100_100_50.html" target="_blank">50元</a>
# 		<a dcs_id="nav_recharge_more_1_3" class="ac_dcs_base" href="https://shop.10086.cn/i/service/recharge/item/itemcollect_100_100_100.html" target="_blank">100元</a>
# 		<a dcs_id="nav_recharge_more_1_4" class="ac_dcs_base" href="https://shop.10086.cn/i/service/recharge/item/itemcollect_100_100_300.html" target="_blank">300元</a>
# 		<a dcs_id="nav_recharge_more_1_5" class="ac_dcs_base" href="https://shop.10086.cn/i/service/recharge/item/itemcollect_100_100_500.html" target="_blank">500元</a>
# 		<a dcs_id="nav_recharge_more_1_6" class="ac_dcs_base" href="https://shop.10086.cn/i/service/recharge/item/itemcollect_100_100_000.html" target="_blank">任意金额</a>
# 		'''

# href = re.findall(r'href="(.*?)" target=',string)
# for i in href:
# 	print i

# s = '''
# 	<meta author="Zjmainstay" />
# 	another author="Zjmainstay too"
# 	'''
# print re.findall(r'(\w+)\b',s)
# s="i love you not because of who you are, but because of who i am when i am with you"
# print re.findall(r'(\b\w+)',s)
# print re.findall(r'\b\w',s)
# s="i love you not because 12sd 34er 56df e4 54434"
# print re.findall(r'\b\d',s)
# www.heibanke.com

# url = "http://shop.10086.cn"
# r = requests.get(url)
# r_http = re.findall(r'href="(.*?)" target=',r.text)
# for i in r_http:
# 	print i
'''
 黑客版爬虫第一关
'''
# url = "http://www.heibanke.com/lesson/crawler_ex00/"
# # r = requests.get(url)
# # r_text = re.findall(r'数字[^\d]*(\d+)[\.<]',r.text)
# # print r_text
# ruler = re.compile(r'数字[^\d]*(\d+)[\.<]')
# html = requests.get(url).content
# num = ruler.findall(html)

# index = 1
# while  num:
# 	url2 = url + num[0]
# 	html = requests.get(url2).content
# 	num = ruler.findall(html)
# 	print "访问网页%d: %s" %(index, url2)
# 	index += 1
# else:
#     print "\n下一关的入口: %s" % url2
'''
 黑客版爬虫第二关
'''
# url = "http://www.heibanke.com/lesson/crawler_ex01/"
# index = 1
# error_ms = "您输入的密码错误, 请重新输入"
# while True:
# 	data = {'username': 'Thare', 'password': index}
# 	html = requests.post(url,data).content
# 	if error_ms not in html:
# 		print "\n密码是: %d" % index
# 		break
# 	print u"第%s次,密码 ：%s,错误" %(index,index)	
# 	index +=1
'''
 黑客版爬虫第三关
'''
# url = "http://www.heibanke.com/accounts/login/"
# url1 = "http://www.heibanke.com/accounts/login/crawler_ex02/"
# error_ms = "您输入的密码错误, 请重新输入"

# s = requests.Session()
# s.get(url)
# token1 = s.cookies['csrftoken']
# data = {
# 				'username': 'user',
#                 'password': 'password',
#                 'csrfmiddlewaretoken': token1
# }
# s.post(url,data)
# pwd = 1
# while pwd<30:
# 	s.post(url1)
# 	token2 = s.cookies['csrftoken']
# 	data2 = {
# 				'username': 'Thare','password': pwd, 'csrfmiddlewaretoken': token1
# 				}
# 	result = s.post(url1,data2).content
# 	if error_ms in result:
# 		print "\n密码: %d error" % pwd
# 		pwd += 1
# 	else:
# 		print "密码是：%s"%(pwd)
# 		break
# num=1
# while num<9:	
# 	url = "https://shop.10086.cn/list/101_471_471_0_0_0_0.html?p="+str(num)
# 	r = requests.get(url)
# 	html = r.content
# 	title = re.findall('title="(.*?)" dcs_id',html)
# 	num += 1
# 	for i in title:
# 		with open('./title.txt','w') as f:
# 			f.write(i,)
url = "https://shop.10086.cn/list/101_471_471_0_0_0_0.html"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
title = soup.find_all(name='img',attrs={'class':'lazy'})
# print title
for i in title:
	print i