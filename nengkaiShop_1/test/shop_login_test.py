import unittest
from base.html_test_runner import HtmlTestRunner
import time

from base.base_driver import ShopDriver
from page.after_login_page.shop_after_login.ShopAfterLogin import *
from page.shop_page import HomeShopPage


class ShopLoginTest(unittest.TestCase):

    def setUp(self):
        # 选择浏览器
        self.driver = ShopDriver('Firefox')
        # 输入网址
        self.driver.navigate('https://shop.10086.cn/mall_100_100.html')
        self.shop = HomeShopPage(self.driver)
        self.login = ShopAfterLogin.shop_net_login(self.driver)


    def test_success_check(self):
        '''断言，登录前购买手机，短信登录校验'''
        driver = self.driver
        self.shop.shop_floor_page()
        print('未登录时购买手机，出现登录校验提示框')
        self.login.shop_num_login()
        print('未登录时购买手机，短信登录成功')
        driver.sleep(5)
        # 购买后登录断言
        get_text = self.login.login_text
        print(get_text)
        self.assertEqual('手机号登录',get_text,'登录前购买手机，短信登录校验失败')
        driver.get_screenshot('登录前购买手机，短信登录校验成功')


if '__main__' == __name__:
    test_suite = unittest.TestSuite()
    print('实例化测试套件')
    test_suite.addTest(ShopLoginTest('test_success_check'))  # 类名
    report_path = 'report\\shop_tests_report_%s.html' \
                  % time.strftime('%Y-%m-%d %H-%M-%S')
    report_file = open(report_path, 'wd')
    test_runner = HtmlTestRunner(stream=report_file,
                                 title='销售子系统测试报告',
                                 description='测试详情')
    test_runner.run(test_suite)
    report_file.close()
