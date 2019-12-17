import unittest
from base.html_test_runner import HtmlTestRunner
import time

from base.base_driver import ShopDriver
from page.login_page import ShopBeforeLogin
from page.shop_page import HomeShopPage

class LoginShopTest(unittest.TestCase):

    def setUp(self):
        # 选择浏览器
        self.driver = ShopDriver('Chrome')
        # 输入网址
        self.driver.navigate('https://shop.10086.cn/mall_100_100.html')
        self.shop = HomeShopPage(self.driver)
        self.login = ShopBeforeLogin(self.driver)


    def test_success_check(self):
        '''断言，短信登录后购买手机'''
        driver = self.driver
        self.login.num_shop_login()
        print('短信验证，成功登录移动商城')
        self.driver.get_screenshot('登录成功')
        self.driver.picture()

        # self.shop.shop_floor_page()
        # print('登录后，成功购买手机')
        # driver.sleep(5)
        # driver.click('x,/html/body/div[6]/form/div[2]/a/em')
        # # 登录后购买成功断言
        # driver.sleep(2)
        # text1 = driver.get_text('x,/html/body/div[2]/div[1]/div[1]/p[1]/span[3]')
        # print(text1)
        # self.assertEqual('提交成功，请您尽快付款！',text1,'登录后购买手机失败')
        # driver.get_screenshot('登录后购买手机成功')

if '__main__' == __name__:
    aa = LoginShopTest()
    aa.test_success_check()