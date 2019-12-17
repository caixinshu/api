# coding=utf-8
from unittestcase import BaiduPage
from unittestaddtest import BaiduPage003
import unittest
import HTMLTestRunner

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

suit=unittest.TestSuite()
# suit.addTest(BaiduPage('test_001'))
# suit.addTest(BaiduPage('test_002'))
# suit.addTest(BaiduPage('test_003'))
# suit.addTest(BaiduPage001('test_001'))
# suit.addTest(BaiduPage001('test_002'))
# suit.addTest(BaiduPage('test_003'))
# unittest.TextTestRunner(verbosity=2).run(suit)


suit0=unittest.TestSuite(unittest.makeSuite(BaiduPage))
suit1=unittest.TestSuite(unittest.makeSuite(BaiduPage003))
suit.addTest(suit0)
suit.addTest(suit1)


# suit=unittest.TestLoader().loadTestsFromTestCase(BaiduPage)
# suit1=unittest.TestLoader().loadTestsFromTestCase(BaiduPage001)
# unittest.TextTestRunner(verbosity=2).run(suit)
# unittest.TextTestRunner(verbosity=2).run(suit1)

#suit=unittest.defaultTestLoader.discover('D:\\PycharmProjects\\studyselenium02\\testcase',pattern='unittestcase*.py',top_level_dir=None)
#unittest.TextTestRunner(verbosity=2).run(suit)

outfile = file("D:\\PycharmProjects\\studyselenium02\\Report\\testreport.html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=u'自动化测试报告',
                description=u'P2P电子商务系统测试报告'
                )
runner.run(suit)
