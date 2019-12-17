#!/usr/bin/env python
# -*- coding=utf-8 -*-

from selenium import webdriver
from operate.baseoperate import BaseOperate
import unittest


class MainCase(unittest.TestCase):
    driver = webdriver
    base_operate = BaseOperate

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver.get('http://openstore.91msp.com:81/')
        # self.driver.maximize_window()
        self.base_operate = BaseOperate(self.driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
   unittest.main()