# -*- coding: utf-8 -*
'''
Created on 2015-12-19

@author: 胡晓燕
'''
import unittest

import requests

from config import url
from config import config
from data import datapath
from utils import lib_db
from utils import readexceldata


class totalbookapi(unittest.TestCase):
    ''''查询总图书'''''
    def setUp(self):
      self.data=readexceldata.excel_table_byname(datapath.datastudy,by_name="getbook")
    def test_01(self):
      ''''验证正确的token返回的值'''''
      data1=self.data[0]
      r=requests.post(url.getbookurl,json=data1)
      self.assertEqual(lib_db.searchbook()[0][0],r.json()["result"]["total"])
      self.assertEqual("sucess",r.json()["result"]["status"])
    def test_02(self):
      ''''验证错误的token返回的值'''''
      data2=self.data[1]
      r=requests.post(url.getbookurl,json=data2)
      self.assertDictEqual({"status": "failed", "mes": "auth failed"},r.json()["result"])

    def test_03(self):
      ''''验证空的token返回的值'''''
      data2=self.data[2]
      r=requests.post(url.getbookurl,json=data2)
      self.assertDictEqual({"status": "failed", "mes": "auth failed"},r.json()["result"])

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
