# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from test.pagework.BasePage import BasePage
import time


# 继承BasePage类
class LoginPage(BasePage):
    # 用户名文本框定位器
    username_loc = (By.NAME, "username")
    # 密码文本框定位器
    password_loc = (By.NAME, "password")
    # 登入后台按钮定位器
    submit_loc = (By.XPATH, "/html/body/div/form/p[4]/input[1]")
    #退出按钮的定位器
    exit_loc = (By.LINK_TEXT,"退出")
    def getUserTextField(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    def getPasswordField(self, password):
        self.findElement(*self.password_loc).send_keys(password)

    def getSubmitButton(self):
        self.findElement(*self.submit_loc).click()

    def getExitLink(self):
        self.findElement(*self.exit_loc).click()

    def Login(self,username, password):
        self.getUserTextField(username)
        self.getPasswordField(password)
        time.sleep(8)
        # 调用send_keys对象，点击登录
        self.getSubmitButton()
        time.sleep(1)
        self.getExitLink()

    def stepLogin(self,username, password):
        self.getUserTextField(username)
        self.getPasswordField(password)
        time.sleep(8)
        # 调用send_keys对象，点击登录
        self.getSubmitButton()
        time.sleep(1)

