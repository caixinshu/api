# -*- coding: utf-8 -*-
__author__ = '201406030209'

# CaseLoginTest.py：
import logging
from selenium.webdriver.common.by import By
from test.testcase.BasetestCase import BaseTestCase
from test.pagework.AddGoodsPage import AddGoodsPage
from tools import ReadYaml
import logging.config
from tools import utils
from test.pagework.LoginPage import LoginPage
"""

  """
class AddGoodsCase(BaseTestCase,AddGoodsPage,LoginPage):
    succuse_loc = (By.XPATH, ".//*[@id='content']/div/div/div[2]/div/table/tbody/tr[1]/td[2]")

    def test_AddGoodsCase001(self):
        '''测试：添加商品信息'''
        # 设置日志输出格式
        utils.testlog("test_AddGoodsCase001")
        logging.info(u"添加商品信息的case开始")
        username = ReadYaml.get_value('UserName', "config.yaml")
        password = ReadYaml.get_value('PassWord', "config.yaml")
        self.stepLogin(username, password)  # 登录系统
        self.AddGoods()
        logging.info(u"商品添加成功！！")
        sussce=self.findElement(*self.succuse_loc).text
        self.assertEqual(sussce,"添加商品成功。")








#
# if __name__ == "__main__":
#     unittest.main(verbosity=2)
