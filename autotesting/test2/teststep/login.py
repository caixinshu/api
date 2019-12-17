# -*- coding: utf-8 -*
'''
Created on 2015-2-2

@author: 胡晓燕
'''
import unittest
import json
import requests
from config import url
from utils import readexceldata
from data import datapath
#登录系统
def login():
      data=readexceldata.excel_table_byname(datapath.datastudy,0,"login")
      data1=data[0]
      r=requests.post(url.loginurl,data=json.dumps(data1))
      result=r.json()
      print result
      return result["result"]["token"]
print login()