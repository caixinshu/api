# coding=utf-8

import unittest
from selenium import webdriver
import time
from init import Init

class UnitTest(Init):
# class UnitTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get("https://shop.10086.cn/mall_100_100.html")
    #     cls.driver.implicitly_wait(30)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get("https://shop.10086.cn/mall_100_100.html")
    #     self.driver.implicitly_wait(30)
    #
    # def tearDown(self):
    #     self.driver.close()

    def test_yidong_yidongshuoming(self):
        '''首页业务：移动商城关于中国移动'''
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/a[4]').click()

    # @unittest.skip(u"不执行的理由")
    def test_yidong_buzhi(self):
        self.assertEqual(self.driver.title, u"中国移动网上商城_北京_话费查询与充值,手机流量查询,4G套餐办理,移动宽带,手机正品低价")

if __name__ == '__main__':
    #创建测试套件，然后一个一个的加用例
    # suite=unittest.TestSuite()
    # suite.addTest(UnitTest('test_yidong_so'))
    # suite.addTest(UnitTest('test_yidong_yidongshuoming'))
    #直接添加测试用例的类
    # suite = unittest.makeSuite(UnitTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    #直接使用main函数运行测试套件
    # unittest.main(verbosity=2)
    #使用testloader加载测试用例的类
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)