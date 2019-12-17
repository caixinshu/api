# coding:utf-8

import requests
import re

# url = "https://shop.10086.cn/list/146_100_100_1_0_0_0.html?p=1"
def spider():

	url = "https://shop.10086.cn/list/146_100_100_1_0_0_0.html?p="
	for i in range(1,4):
		r = requests.get(url+str(i))
		yewu_herfs = re.findall('href="(.*?)" title',r.content)
	
		for yewu_herf in yewu_herfs:
			if "shop.10086.cn" in yewu_herf:
				print yewu_herf

spider()