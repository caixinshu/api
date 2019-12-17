import unittest
from base.base_driver import ShopDriver
from page.shop_page import HomeShopPage
from page.login_page import ShopBeforeLogin
from page.after_login_page.order_add_page.order_add import OrderAdd

class OrderCheckTest(unittest.TestCase):
     def setUp(self):
         # 选择浏览器
         self.driver = ShopDriver('Chrome')
         # 输入网址
         self.driver.navigate('https://shop.10086.cn/mall_100_100.html')
         self.shop = HomeShopPage(self.driver)
         self.login = ShopBeforeLogin(self.driver)
         self.order = OrderAdd(self.driver)

     def test_edit_check(self):
         '''断言，编辑已有地址'''
         driver = self.driver
         self.login.num_shop_login()
         print('短信验证，成功登录移动商城')
         self.shop.shop_floor_page()
         print('登录后，成功购买手机')
         driver.sleep(5)
         text1 = driver.get_text('x,/html/body/div[6]/div[1]/div[1]')
         print(text1)
         if '+ 新增地址' not in text1:
            self.order.first_order_info()
         elif '+ 新增地址' in text1:
            self.order.edit_order_info()
         else:
            print('No elements found !')

     def test_del_check(self):
         '''断言，删除已有地址'''
         driver = self.driver
         self.login.num_shop_login()
         print('短信验证，成功登录移动商城')
         self.shop.shop_floor_page()
         print('登录后，成功购买手机')
         driver.sleep(5)
         text1 = driver.get_text('x,/html/body/div[6]/div[1]/div[1]')
         print(text1)
         if '+ 新增地址' not in text1:
            self.order.first_order_info()
         elif '+ 新增地址' in text1:
            self.order.del_order_info()
         else:
            print('No elements found !')


if '__main__' == __name__:
    aa = OrderCheckTest()
    aa.test_del_check()