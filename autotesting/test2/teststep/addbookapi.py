# -*- coding: utf-8 -*
'''
Created on 2015-2-2

@author: 胡晓燕
'''
import unittest
import json
import requests
from config import url
from tools import readexceldata
from data import datapath
#添加书
def addbookapi(token):
      data=readexceldata.excel_table_byname(datapath.datastudy,0,"addbook")
      data11=data[0]["token"]
      data[0].pop("token")
      data1={"token":token,"data":data[0]}
      r=requests.post(url.addbookurl,json=data1)
