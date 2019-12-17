# coding=utf-8
from selenium import webdriver
import unittest
class BaiduPage003(unittest.TestCase):
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

# if __name__=='__main__':
#     #考虑下是否可以重构
#
#     unittest.TextTestRunner(verbosity=2).run(BaiduPage.unitcase())

    #支持suit嵌套suit
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(BaiduPage))
    # suite.addTest(BaiduPage('test_003'))
    # unittest.TextTestRunner(verbosity=2).run(suite)