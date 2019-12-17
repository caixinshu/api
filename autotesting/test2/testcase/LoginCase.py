#coding:utf-8

import  unittest
from test.testcase.BasetestCase import BaseTestCase
from test.pagework.LoginPage import LoginPage
from tools import ReadCsv1
from ddt import  ddt,data,unpack
@ddt
class LoginCase(BaseTestCase,LoginPage):
	@data(*ReadCsv1.readCsv1("../../data/csvdata1.csv"))
	@unpack
	def test_Login001(self,username,password):
		'''测试：登录电子商城'''
		self.Login(username,password)
		#self.assertEqual(context_expxcted,self.getLoginErrorDiv())

if __name__=='__main__':
	unittest.main(verbosity=2)
