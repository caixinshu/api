from base.base_page import BasePage


class ShopAfterLogin(BasePage):
    def shop_num_login(self):
        '''购买商品后短信验证登录'''
        driver = self.base_driver
        driver.sleep(3)
        driver.switch_to_frame('x,//*[@id ="jquery-interactive-alert"]/table/tbody/tr[2]/td[2]/div/div/div[4]/div/iframe')
        driver.sleep(4)
        self.login_text = driver.get_text('x,//*[@id="phone_login_1"]')
        # 输入手机号码
        driver.type('p_name','13823218582')
        # 选择验证方式
        driver.click('x,//*[@id="am"]')
        # 点击【短信验证】
        driver.click('x,/html/body/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/span[2]')
        # 【获取验证码】
        driver.click('x,//*[@id="getSMSpwd"]')
        driver.sleep(30)
        # 【登录】
        driver.click('submit_bt')

    def shop_net_login(self):
        '''购买商品后互联网验证登录'''
        driver = self.base_driver
        driver.sleep(3)
        driver.switch_to_frame(
            'x,//*[@id ="jquery-interactive-alert"]/table/tbody/tr[2]/td[2]/div/div/div[4]/div/iframe')
        print('互联网登录')
        driver.sleep(4)
        driver.click('mail_login_1')
        self.login_text = driver.get_text('x,//*[@id="phone_login_1"]')
        print(self.login_text)
        # 输入互联网账号
        driver.type('e_name', '13823218582')
        # 输入密码
        driver.type('e_pwd','2342534')
        # 输入图形验证码
        driver.sleep(20)
        # 【登录】
        driver.click('submit_bt')
