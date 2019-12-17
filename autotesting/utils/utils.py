# -*- coding: utf-8 -*-
import random

import re
import logging
from datetime import date, timedelta
import hashlib
import types
import time
import datetime

'''
Created on 2015-4-24

'''
#读取字符窜，以：作为分割符号，返回对应键值
def vrifyPara(pareterName,result):

    pareterNameTest='"'+pareterName+'":"'

    res = re.findall(pareterNameTest+'([^"]+)"',result)

    print "res[0]:=", res[0]
    return res[0]

#读取返回的json格式的字符串，以字典的方式存储。
# json_str='{"total":1,"data":[{"outGuaranteeTime":"","assetsNum":"B50070100007003","cabinet":"H05","deviceModel":"PowerEdge 1950","hostname":"hzshterm1.alibaba.com","logicSite":"中文站","memoryInfo":{"amount":4,"size":8192},"ip":"172.16.20.163","isOnline":true,"useState":"使用中","serviceTag":"729HH2X","cpuInfo":{"amount":2,"masterFrequency":1995,"model":"Intel(R) Xeon(R) CPU           E5405  @ 2.00GHz","coreNum":8,"l2CacheSize":6144},"cabinetPositionNum":"","buyTime":"2009-06-29","manageIp":"172.31.58.223","idc":"杭州德胜机房","responsibilityPerson":"张之诚"}],"errorMsg":"","isSuccess":true}'
dict_str={}
class joon:
    def jsn(self,dict_json):
     for i in dict_json:
        if str(type(dict_json[i]))=='<type \'list\'>':
          for ii in dict_json[i]:
            self.jsn(ii)
        elif str(type(dict_json[i]))=='<type \'dict\'>':
            self.jsn(dict_json[i])
        else:
            dict_str[i]=dict_json[i]
            # list_dict.append(dict_str)
     return dict_str

# dict_json1=json.loads(json_str)#调用上面的方法
# a=joon()
# print a.jsn(dict_json1)

#xml格式的解释
# list_str=[]
# def readxmlNodes(domElement):
#     print domElement
#     dom=minidom.parseString(domElement)
#     root=dom.documentElement
#     for nodes in root.childNodes:
#         #if nodes.nodeType==nodes.ELEMENT_NODE:
#             #pass
#             #for keys in nodes.attributes.keys():
#                 #print nodes.attributes[keys].name+"="+nodes.attributes[keys].value
#         if len(nodes.childNodes)==1:
#             dict_str={}
#             dict_str[nodes.nodeName]=nodes.childNodes[0].nodeValue
#             list_str.append(dict_str)
#             #print nodes.nodeName+":"+nodes.childNodes[0].nodeValue
#         else:
#             readxmlNodes(nodes)
#     return list_str
# print readxmlNodes(str2)

#获取当前时间
def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

# 配置日志信息
def testlog(testcaseID):
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=r'D:/PycharmProjects/uitestframework/log/'+getNowTime()+'mylog.log',
                    filemode='a')
    #定义一个Handler打印INFO及以上级别的日志到sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # 设置日志打印格式
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
   # 将定义好的console日志handler添加到root logger
    #logging.getLogger('').addHandler(console)
    logger = logging.getLogger(testcaseID)

    # if exception=='pass':
    #    logger.info(exception)
    # else:
    #     logger.error(exception)
import math
# 计算两个值在允许的范围之内可等
def mat(x,y):
    flag="false"
    if math.fabs(y-x)<=1:
       flag="true"
    return flag

#随机生成电话号码
def randomtelphone():
    telnum=random.choice(['139','188','185','136','158','151','186'])+"".join(random. sample ("0123456789",8 ))
    return telnum

#随机生成一个字符串
def randomhs():
   hsnum="HS"+"".join(random.sample('zyxwvutsrqponmlkjihgfedcba',5))
   return hsnum
#随机生成一个姓名

#生成身份证
def gennerator():
  listcode=['230200','230201','230202','230203','230204','230205','230206','230207','230208']#山西省的部分BM
  #id = codelist[random.randint(0,len(codelist))]['code'] #地区项
  id=random.choice(listcode)
  id = id + str(random.randint(1930,2013)) #年份项
  da = date.today()+timedelta(days=random.randint(1,366)) #月份和日期项
  id = id + da.strftime('%m%d')
  id = id+ str(random.randint(100,999))#，顺序号简单处理
  i = 0
  count = 0
  weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
  checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
  for i in range(0,len(id)):
    count = count +int(id[i])*weight[i]
  id = id + checkcode[str(count%11)] #算出校验码
  return id



def getMd5(key):
    if type(key) is types.StringType:
        currdate = time.strftime("%Y-%m-%d")
        datekey = currdate+key
        m = hashlib.md5()
        m.update(datekey)
        psw1 = m.hexdigest()
        # 再次加密
        m = hashlib.md5()
        m.update(psw1)
        psw2 = m.hexdigest()
        return psw2[:16]
    else:
        return ''

def getfromatDate():
    i = datetime.datetime.now()
    return i.isoformat()


