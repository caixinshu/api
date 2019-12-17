# coding=utf-8
from selenium import webdriver
import unittest
from lib import HTMLTestRunner
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
        self.assertEqual(u"百度一下，你就知道", self.driver.title)
    def test_002(self):
        '''验证url是否正确'''
        self.assertEqual("https://www.baidu.com/",self.driver.current_url)
    def test_003(self):
        '''验证搜索功能是否正确'''
        self.driver.find_element_by_id("kw").send_keys(u"selenium")
        self.driver.find_element_by_id("su").click()
        self.assertTrue(u"selenium" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    #考虑下是否可以重构
    suit=unittest.TestSuite()
    suit.addTest(BaiduPage('test_001'))
    suit.addTest(BaiduPage('test_002'))
    suit.addTest(BaiduPage('test_003'))
    outfile = file("testreport.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=u'自动化测试报告',
                description='P2P电子商务系统测试报告'
                )

    runner.run(suit)
    unittest.main()