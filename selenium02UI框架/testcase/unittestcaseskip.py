# coding=utf-8
from selenium import webdriver
import unittest


class BaiduPage001(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.baidu.com/")

    def test_001(self):
        '''验证title是否正确'''
        self.assertEqual(u"百度一下，你就知道", self.driver.title)
    @unittest.skip(u"暂时不运行")
    def test_002(self):
        '''验证url是否正确'''
        self.assertEqual("https://www.baidu.com/", self.driver.current_url)

    def test_003(self):
        '''验证搜索功能是否正确'''
        self.driver.find_element_by_id("kw").send_keys(u"测试")
        self.driver.find_element_by_id("su").click()
        self.assertTrue(u"测试" in self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
