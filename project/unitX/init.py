# coding=utf-8

import unittest
from selenium import webdriver

class Init(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://shop.10086.cn/mall_100_100.html")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()
