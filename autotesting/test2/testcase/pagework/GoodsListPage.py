# -*- coding: utf-8 -*-
__author__ = 'liyingfeng'

import time
from selenium.webdriver.common.by import By
from test.pagework.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
# 继承BasePage类
class GoodsListWork(BasePage):
    # 定位器，通过元素属性定位元素对象
     #定位器，通过元素属性定位元素对象
    menu_loc =(By.XPATH,".//*[@id='nav']/div/ul[1]/li[2]/p/em")
    goodslist_loc =(By.LINK_TEXT,"商品列表")
    keyword_loc=(By.NAME,"keyword")
    select_loc=(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/input[2]")

    def DeleteGoodsInfo(self):
        print(u"删除问题的case")
        time.sleep(5)
        self.find_element(*self.malink_loc).click()

    def SelectGoodsInfo(self,goodsname):
        ActionChains(self.driver).move_to_element(self.findElement(*self.menu_loc)).perform()#鼠标悬停在分类和商品菜单
        self.findElement(*self.goodslist_loc).click()#点击商品列表
        self.findElement(*self.keyword_loc).send_keys(goodsname)#输入搜索内容
        self.findElement(*self.select_loc).click()  #点击搜索按钮
    def UpdateGoodsInfo(self):
        print(u"修改问题的case")
        time.sleep(5)
