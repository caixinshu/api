# -*- coding: utf-8 -*
'''
Created on 2015-12-19

@author: 胡晓燕
'''
import unittest
import json
import requests
from config import url
from utils import readexceldata
from ddt import ddt,data,unpack
from data import datapath

@ddt
class loginapi(unittest.TestCase):
    '''验证登录'''
    def setUp(self):
      print self._testMethodName   #打印test的名称
    @data(*readexceldata.excel_table_byname(datapath.datastudy,by_name="login"))
    @unpack
    def test_login(self,postdata,expect):
      r=requests.post(url.loginurl,data=postdata)
      self.assertEqual(r.content,expect)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
