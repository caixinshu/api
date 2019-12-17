# -*- coding: utf-8 -*
'''
Created on 2015-12-19
'''
import unittest

import requests
from config import url
from data import datapath
from utils import lib_db
from utils import readexceldata
class addbookapi(unittest.TestCase):
    ''''添加书接口验证'''''
    def setUp(self):
      # self.testtinit= testbase.test(url.addbookurl,datapath.datastudy,0,"addbook")
      self.data=readexceldata.excel_table_byname(datapath.datastudy,0,"addbook")
      print self.data
    def test_01(self):
      ''''验证正确添加图书返回的值'''''
      data11=self.data[0]["token"]
      self.data[0].pop("token")
      data1={"token":data11,"data":self.data[0]}
      r=requests.post(url.addbookurl,json=data1)
      self.assertEqual("sucess",r.json()["result"]["status"])
      #删除添加的数据
      lib_db.deletebook()
    def test_02(self):
      ''''验证添加图书，必填字段为空的情况'''''
      data11=self.data[1]["token"]
      self.data[1].pop("token")
      data1={"token":data11,"data":self.data[1]}
      r=requests.post(url.addbookurl,json=data1)
      self.assertEqual("failed",r.json()["result"]["status"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
