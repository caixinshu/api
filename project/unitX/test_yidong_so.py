# coding=utf-8

import unittest
from selenium import webdriver
import time
from init import Init

class UnitTest(Init):

    def test_yidong_so(self):
        '''搜索业务：移动商城首页的搜索'''
        self.driver.find_element_by_id("skeywords").clear()
        self.driver.find_element_by_id("skeywords").send_keys('iphonexr')

    @unittest.skip(u"不执行的理由")
    def test_yidong_buzhi(self):
        pass
if __name__ == '__main__':
   unittest.main(verbosity=2)
