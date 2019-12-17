# -*- coding: utf-8 -*
'''
Created on 2015-4-29

@author: 胡晓燕
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from suds.client import Client
url="http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl"
client=Client(url)
print client
result=client.service.getCountryCityByIp("111.13.100.92")
print result
# url="http://10.10.37.29:8088/helloWorld?wsdl"

# client=Client(url)
# 接口：SayHiToUserList
# print client #打印client,可以看见命名空间，接口名称，方法，参数等
# user1=client.factory.create('user')
# print user1
# user1.age=16
# user1.description="python"
# user1.id=98
# user1.name="huxiaoyan"
# result=client.service.SayHiToUserList(user1)
# print result
# print type(result)
# assert(result[0]=="Hello huxiaoyan")

# 接口sayHi

# text="huxiaoyan"
# arg1=11
# arg2=11.12
# result=client.service.sayHi(text,arg1,arg2)
# print result
# print type(result)
# assert(str(result)=="Hello,huxiaoyan年龄11浮点11.12")

#接口sayHiToUser

# user2=client.factory.create('user')
# user2.age=16
# user2.description="python"
# user2.id=98
# user2.name="huxiaoyan"
# result=client.service.sayHiToUser(user2)
# print result
# assert(result.age=="16")

