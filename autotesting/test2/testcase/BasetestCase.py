#coding:utf-8

import unittest
from tools import ReadYaml
from test.comwork import OpenBrower

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        brotype = ReadYaml.get_value('brotype',"config.yaml")
        url = ReadYaml.get_value('url',"config.yaml")
        cls.driver = OpenBrower.is_brower(brotype, url)

    @classmethod
    def tearDownClass(cls):
    	cls.driver.quit()
