# -*- coding: utf-8 -*
import MySQLdb
import unittest
import json
import requests
import HTMLTestRunner
class logintest(unittest.TestCase):
   def test_001(self):
    '''验证正确用户名密码'''
    url = 'http://127.0.0.1:8000/ltcs/api/token'
    data ='{"username":"root","password":"123456"}'
    r = requests.post(url,data)
    # print r.status_code
    data = r.json()
    print url
    print data
    print data['result']['status']
    self.assertEqual('sucess',data['result']['status'])
   def test_002(self):
      '''验证正确用户名,错误密码'''
      url = 'http://127.0.0.1:8000/ltcs/api/token'
      data ='{"username":"root","password":"12345"}'
      r = requests.post(url,data)
      data = r.json()
      print data
      self.assertEqual('failed',data['result']['status'])
   def test_003(self):
          '''验证输入空用户名，正确密码'''
          url = 'http://127.0.0.1:8000/ltcs/api/token'
          data ='{"username":"","password":"12345"}'
          r = requests.post(url,data)
          data = r.json()
          self.assertEqual('failed',data['result']['status'])
if  '__name__' == '__main__':
    #考虑下是否可以重构
     unittest.main(verbosity=2)


















