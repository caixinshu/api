# coding=utf-8
from selenium import webdriver
import unittest
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
        self.driver.find_element_by_id("kw").send_keys(u"测试")
        self.driver.find_element_by_id("su").click()
        self.assertTrue(u"测试" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    suit=unittest.defaultTestLoader.discover('D:\\PycharmProjects\\studyselenium02\\',pattern='test_*.py',top_level_dir=None)
    unittest.TextTestRunner(verbosity=2).run(suit)