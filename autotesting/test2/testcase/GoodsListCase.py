#-*- coding: utf-8 -*-
__author__ = '201406030209'

# CaseLoginTest.py：
import logging
import unittest
from tools import utils
from test.pagework.GoodsListPage import GoodsListWork
from tools import ReadYaml
from test.testcase.BasetestCase import BaseTestCase
from test.pagework.LoginPage import LoginPage
"""
 电子商城case
  """
class GoodsListCase(BaseTestCase, GoodsListWork,LoginPage):
        #删除试题用例
    # def test_DeleteGoodsInfoCase(self):
    #     #设置日志输出格式
    #     utils.testlog("test_DeleteGoodsInfoCase")
    #     logging.info(u"删除商品信息")
        # manage_page =GoodsListWork(self.driver)
        # manage_page.DeleteQuestion()
    #
    # def test_UpdateGoodsInfoCase(self):
    #
    #     #设置日志输出格式
    #     utils.testlog("test_UpdateGoodsInfoCase")
    #     logging.info(u"修改商品信息")
        # manage_page =GoodsListWork(self.driver)
        # manage_page.UpdateQuestion()
    def test_SelectGoodsCase001(self):
        '''测试：添加商品信息'''
        # 设置日志输出格式
        utils.testlog("test_SelectGoodsCase001")
        logging.info(u"查询商品信息的case开始")
        username = ReadYaml.get_value('UserName', "config.yaml")
        password = ReadYaml.get_value('PassWord', "config.yaml")
        self.stepLogin(username, password)  # 登录系统
        self.SelectGoodsInfo(u"商品")
        logging.info(u"商品查询成功！！")
        # sussce=self.findElement(*self.succuse_loc).text
        # self.assertEqual(sussce,"添加商品成功。")

# 测试
if __name__ == "__main__":
    unittest.main(verbosity=2)
