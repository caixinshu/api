# coding=utf-8
import unittest
from ddt import ddt, data, file_data, unpack
from selenium import webdriver

@ddt
class orderLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profilepath = r"C:\Users\liyingfeng\AppData\Roaming\Mozilla\Firefox\Profiles\c1r4vm2f.default"
        # 打开火狐浏览器
        cls.profile = webdriver.FirefoxProfile(cls.profilepath)
        cls.driver = webdriver.Firefox(cls.profile)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.baidu.com/")
    data()
    def test_search_001(self):
        '''验证搜索功能是否正确'''
        self.driver.find_element_by_id("kw").send_keys(u"龙腾测试")
        self.driver.find_element_by_id("su").click()
        self.assertTrue(u"龙腾测试" in self.driver.page_source)