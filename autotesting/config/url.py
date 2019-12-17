# -*- coding: utf-8 -*
'''
Created on 2015-4-29

@author: 胡晓燕
'''
#放一些基础数据

from suds.client import Client

pdfurl="http://pre-pdf.creditease.corp/services/ceBorrowingProducts?wsdl"
Translator="http://webservice.webxml.com.cn/WebServices/TranslatorWebService.asmx?wsdl"
#get
ipget="http://ip.taobao.com/service/getIpInfo.php?"

loginurl="http://127.0.0.1:8000/ltcs/api/token"#登录接口

getbookurl='http://127.0.0.1:8000/ltcs/api/book/get'
lendbookurl='http://127.0.0.1:8000/ltcs/api/book/lend'
addbookurl="http://127.0.0.1:8000/ltcs/api/book/add"
#post
#
# client=Client(Translator)
# print client
# # #
# queryProductInfoIdReq=client.factory.create("ns2:newCustomer")
# print queryProductInfoIdReq
# print queryProductInfoIdReq
# newCustomer=client.factory.create("proListParamAdd")
# print newCustomer

# 字符窜合并

