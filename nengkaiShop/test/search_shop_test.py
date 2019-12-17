import unittest
from base.html_test_runner import HtmlTestRunner
import time

from base.base_driver import ShopDriver
from page.after_login_page.shop_after_login import ShopAfterLogin
from page.search_page import SearchComm

class SearchShopTest(unittest.TestCase):

    def setUp(self):
        # 选择浏览器
        self.driver = ShopDriver('Chrome')
        # 输入网址
        self.driver.navigate('https://shop.10086.cn/mall_100_100.html')
        self.searchs = SearchComm(self.driver)
        self.login = ShopAfterLogin(self.driver)


    def test_success_check(self):
        '''断言，短信登录后购买手机'''
        driver = self.driver
        self.searchs.search()
        print('搜索商品')
        self.login.shop_num_login()
        print('登录账号')
        driver.sleep(5)
        text1 = driver.get_text('x,/html/body/div[6]/div[1]/div[1]')
        print(text1)
        if '+ 新增地址' not in text1:
            self.order.first_order_info()
        elif '+ 新增地址' in text1:
            self.order.edit_order_info()
        else:
            print('No elements found !')
        driver.click('x,/html/body/div[6]/form/div[2]/a/em')
        text = driver.get_text('x,/html/body/div[2]/div[1]/div[1]/p[1]/span[3]')
        print(text)
        self.assertEqual('提交成功，请您尽快付款！',text,'登录后购买手机失败')
        driver.get_screenshot('登录后购买手机成功')

if '__main__' == __name__:
    aa = SearchShopTest()
    aa.test_success_check()