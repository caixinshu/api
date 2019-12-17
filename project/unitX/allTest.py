# coding=utf-8

import unittest
import os
import time
import sys
# sys.setdefaultencoding('utf-8')

def allTestCase():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None)
    unittest.TextTestRunner(verbosity=2).run(suite)
    return suite

def getNowTime():
    # return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    return time.strftime("%Y-%m-%d %H:%M:%S")

print(getNowTime())

# def run():
#     fp = open(getNowTime()+"testReport.html", "wb")
#     HTMLTestRunner.HTMLTestRunner(
#         stream=fp,
#         title="自动化测试报告",
#         description="ceshi"
#     ).run(allTestCase())

# if __name__ == '__main__':
    # run()