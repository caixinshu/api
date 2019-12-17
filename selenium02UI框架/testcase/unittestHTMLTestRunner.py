# coding=utf-8
from selenium import webdriver
import unittest
import HTMLTestRunner
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class BaiduPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.baidu.com/")
    def test_001(self):
        '''验证title是否正确'''
        print "1111111111111111111111111"
        self.assertEqual(u"百度一下，你就知道", self.driver.title)
    def test_002(self):
        '''验证url是否正确'''
        self.assertEqual("https://www.baidu.com/",self.driver.current_url)
        print "222222222222222222222"
    def test_003(self):
        '''验证搜索功能是否正确'''
        self.driver.find_element_by_id("kw").send_keys(u"selenium")
        self.driver.find_element_by_id("su").click()
        self.assertTrue(u"selenium" in self.driver.page_source)
        print "33333333333333333333333"
    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    print "bbbbbbbbbbbbbbbbbbbb"
    #考虑下是否可以重构
    suit=unittest.TestSuite()
    suit.addTest(BaiduPage('test_001'))
    suit.addTest(BaiduPage('test_002'))
    suit.addTest(BaiduPage('test_003'))
    print "aaaaaaaaaaaaaaaaaa"
    outfile = file("D:\\PycharmProjects\\studyselenium02\\Report\\testreport.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=u'自动化测试报告',
                description=u'P2P电子商务系统测试报告'
                )
    runner.run(suit)
    print "ssssssssssssssssssss"
