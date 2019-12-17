from base.base_page import BasePage


class ShopBeforeLogin(BasePage):
    def num_shop_login(self):
        '''短信验证登录'''
        driver = self.base_driver
        driver.click_by_text('登录')
        driver.sleep(3)
        driver.click('sms_login_1')
        print('手机验证码登录')
        driver.sleep(4)
        self.login_text = driver.get_text('sms_login_1')
        print(self.login_text)
        # 输入手机号码
        driver.type('sms_name','13823218582')
        # 点击【获取验证码】
        driver.click('getSMSPwd1')
        # 输入验证码
        driver.sleep(20)
        # 【登录】
        driver.click('submit_bt')
        driver.sleep(3)