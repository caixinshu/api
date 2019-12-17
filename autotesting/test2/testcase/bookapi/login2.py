# -*- coding: utf-8 -*
import MySQLdb
from utils import lib_db
import unittest
import json
import requests
import HTMLTestRunner
class logintest(unittest.TestCase):
   def test_001(self):
    '''验证正确用户名密码'''
    url = 'http://127.0.0.1:8000/ltcs/api/book/get'
    data ='{"token":"a724636d6dba10a8e92d351e9d783ebcc3a4de79"}'
    r = requests.post(url,data)
    # print r.status_code
    print r.content
    data = r.json()
    # print data['result']['data']['total_num']