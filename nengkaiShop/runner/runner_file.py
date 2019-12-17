# encoding:utf8
import time
import unittest

from base.html_test_runner import HtmlTestRunner
from login_shop_test import LoginShopTest
from shop_login_test import ShopLoginTest
# from order_check_one import OrderCheckTest
# from base.html_email_attachment import HtmlEmailAttachment

class ShopRunner():
    '''运行用例，并生成报告'''
    def runner(self):
        test_suite = unittest.TestSuite()
        print('实例化测试套件')
        test_suite.addTest(LoginShopTest('test_success_check'))

        report_path = '..\\report\\shop_tests_report_%s.html' \
                      % time.strftime('%Y-%m-%d %H-%M-%S')
        report_file = open(report_path,mode='wb')
        test_runner = HtmlTestRunner(stream=report_file,
                                     title='销售子系统测试报告',
                                     description='测试详情')
        test_runner.run(test_suite)
        # HtmlEmailAttachment().email_attachment(report_path)
        # report_file.close()

    def runnerall(self):
        test_suit = unittest.TestSuite()
        tests = [LoginShopTest('test_success_check'),
                 ShopLoginTest('test_success_check')
                 ]
        test_suit.addTests(tests)
        report_path = '..\\report\\shop_tests_report_%s.html' \
                      % time.strftime('%Y-%m-%d %H-%M-%S')
        report_file = open(report_path,mode='wd')
        test_runner = HtmlTestRunner(stream=report_file,
                                     title='销售子系统测试报告',
                                     description='测试详情')
        test_runner.run(test_suit)
        report_file.close()



if '__main__' == __name__:
    aa = ShopRunner()
    aa.runner()


