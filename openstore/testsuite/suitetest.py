#!/usr/bin/env python
# -*- coding=utf-8 -*-


import unittest
import time
from config import sysconfig
from utils import HTMLTestRunner



'''
addTest

suite = unittest.TestSuite()
suite.addTest('测试用例类名')


############################
makeSuite

suite = unittest.TestSuite(unittest.makeSuite('测试用例类名'))

############################


suite = unittest.TestLoader().discover("你的测试用例类的路径")

 '''
suite = unittest.TestSuite()
suite.addTest('测试用例类名')


if __name__ == '__main__':

    runner = unittest.TextTestRunner()


    filename = sysconfig.ReportUrl + time.strftime(sysconfig.ISOTIMEFORMAT,time.localtime(time.time()))
    fp = open(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Openstore Test Report',
        description='Openstore All Testcase'
        )
    runner.run(suite)