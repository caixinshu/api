# -*- coding: utf-8 -*-
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("D:\\pythonworkspace\\autotesting")
print sys.path

import unittest
from test2.testcase.bookapi import loginapi,getbookapi
from test2.testcase.bookapi import addbookapi,lendbookapi
from utils import lib_db
from utils import HTMLTestRunner
def suite():
   login=unittest.makeSuite(loginapi.loginapi,'test')
   getbook=unittest.makeSuite(getbookapi.totalbookapi,'test')
   # lendbook=unittest.makeSuite(lendbookapi.lendbookapi,'test')
   # addbook=unittest.makeSuite(addbookapi.addbookapi,'test')
   suite=unittest.TestSuite((login,getbook))
   return suite
# 单个方法
# def suite():
#    suite = unittest.TestSuite()
#    suite.addTest(loginapi.loginapi("test_01"))
#    suite.addTest(loginapi.loginapi("test_02"))
#    return suite

#搜索所有的test,
def suite():
    """想用TestLoader方式把测试加到TestSuite的死后可以这样用
    """
    test_cases = (study.login)
    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite


if __name__ == "__main__":
    #初始化数据
    #插入图书的记录n条
    lib_db.insertbook("java","冯丽英","17-18-19","人民日报",5,0)
    lib_db.insertbook("Python","贾老师","29-89-90","人民日报",5,0)
    lib_db.insertbook("selenium","胡老师","29-89-90","人民日报",5,0)
    now=time.strftime("%Y-%m-%d")
    print now
    filename = "D:\\pythonworkspace\\autotesting\\report\\%sresult.html"%now
    print filename
    # filename = "D:\\pythonworkspace\\apiteststudy\\apiteststudy\\report\\result.html"
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description ='Test_Report')
    runner.run(suite())
    lib_db.deletetable()
    #sendemail("test1","发送测试报告",filename)
    #删除所有库的数据

    # unittest.main(defaultTest='suite')







