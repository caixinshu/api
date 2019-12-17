# -*- coding: utf-8 -*-
import sys
sys.path.append("D://workspace//apitest")
from lib import HTMLTestRunner
from test.testsuit import suite

#生成测试报告
def testresult():
 filename="D:\\workspace\\apitest\\result.html"
 fp=file(filename,'wb')
 runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='Test_Report')
 runner.run(suite.suite())

if __name__=="__main__":
  testresult()
