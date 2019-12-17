# coding=utf-8
# https://shop.10086.cn
import exrex

host = 'https://shop.10086.cn/'

web_white = ['com','cn','org','edu','gov']

def host_para(host):
	if '://' in host:
		host = host.split('://')[1].replace('/','')		
	if '/' in host:
		host = host.replace('/','')
	return host

def dic_create(hosts):
	web_dics = hosts.split('.')
	for web_dic in web_dics:
		if web_dic not in web_white:
			f_pass = open('pass_1.txt','r')
			for dic_pass in f_pass:
				dics = list(exrex.generate(web_dic+'[!@#]'+dic_pass.strip('\n')))
				for dic in dics:
					print dic
dic_create(host_para(host))
