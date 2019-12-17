#-*- coding: utf-8 -*-
__author__ = ''

from selenium.webdriver.common.by import By
from test.pagework.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from tools import utils

#继承BasePage类
class AddGoodsPage(BasePage):
    #定位器，通过元素属性定位元素对象
    menu_loc =(By.XPATH,".//*[@id='nav']/div/ul[1]/li[2]/p/em")
    addgoods_loc =(By.LINK_TEXT,"添加新商品")
    goods_name_loc =(By.NAME,"goods_name")#商品名称
    cat_id_loc =(By.NAME,"cat_id") #商品分类下拉选择框
    shop_price_loc =(By.NAME,"shop_price")#输入市场价格
    price_loc = (By.XPATH,".//*[@id='general-table']/tbody/tr[7]/td[2]/input[2]")#市场价格计算按钮
    save_link = (By.XPATH,".//*[@id='tabbody-div']/form/div/input[2]")#确定按钮

    def AddGoods(self):
        ActionChains(self.driver).move_to_element(self.findElement(*self.menu_loc)).perform()#鼠标悬停在分类和商品菜单
        self.findElement(*self.addgoods_loc).click()#点击添加商品按钮
        self.findElement(*self.goods_name_loc).send_keys(u"自动化测试商品"+utils.randomhs())#添加商品名称
        Select(self.findElement(*self.cat_id_loc)).select_by_value("69")#选择休闲鞋
        self.findElement(*self.shop_price_loc).send_keys("100")#输入市场价格
        self.findElement(*self.price_loc).click() #点击按市场价格计算
        self.findElement(*self.save_link).click() #点击确定按钮
