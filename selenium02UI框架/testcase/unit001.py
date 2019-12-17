# coding=utf-8
import unittest
import HTMLTestRunner
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class BaiduPageDemo(unittest.TestCase):

     # suit=unittest.TestLoader().loadTestsFromTestCase(BaiduPage)
    # unittest.TextTestRunner(verbosity=2).run(suit)
    suit=unittest.defaultTestLoader.discover('D:\\PycharmProjects\\studyselenium02\\testcase',pattern='unittestcase*.py',top_level_dir=None)
    #unittest.TextTestRunner(verbosity=2).run(suit)
    outfile = file("D:\\PycharmProjects\\studyselenium02\\Report\\testreport.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=u'自动化测试报告',
                description='P2P电子商务系统测试报告'
                )
    runner.run(suit)