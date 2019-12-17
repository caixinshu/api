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


class lendbookapi(unittest.TestCase):
    ''''借书接口验证'''''
    def setUp(self):
      data1 = {'token':'a724636d6dba10a8e92d351e9d783ebcc3a4de79','id':9}
      # self.data=readexceldata.excel_table_byname(datapath.datastudy,0,"lendbook")
    def test_01(self):
      ''''验证有图书返回的值'''''
      data1=self.data[0]
      print data1
      #初始化借书数据为0
      lib_db.updatebook(9,0)

      r=requests.post(url.lendbookurl,json=data1)
      lib_db.searchbook1(9)[0][6]
      self.assertEqual(1,lib_db.searchbook1(9)[0][6])
      self.assertEqual("sucess",r.json()["result"]["status"])
      #还原数据库借书的值为0
    def test_02(self):
      ''''验证图书全部借出的情况'''''
      data2=self.data[1]
      #更新借出去的书的数量和总数量相等
      lib_db.updatebook(9,lib_db.searchbook1(9)[0][5])
      r=requests.post(url.lendbookurl,json=data2)
      self.assertEqual("failed",r.json()["result"]["status"])
    def test_03(self):
     ''''验证无此图书的情况'''''

    def tearDown(self):
         lib_db.updatebook(9,0)
if __name__ == '__main__':
    unittest.main()
