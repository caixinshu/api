# -*- coding: utf-8 -*
'''
Created on 2015-12-19

@author: 胡晓燕
'''
import unittest

import requests


from config import url
from data import datapath
from utils import lib_db
from utils import readexceldata
from test2.teststep import login
from test2.teststep import addbookapi
class logic(unittest.TestCase):
    def setUp(self):
        pass
    def test_01(self):
      login.login()
      addbookapi.addbookapi(login.login())
      print "123"

