# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class YidongTest(unittest.TestCase):
	"""docstring for BaiduTest"""

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()		
		cls.driver.get("https://shop.10086.cn/mall_100_100.html")
		cls.driver.implicitly_wait(30)
		time.sleep(2)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_yidong_01(self):
		pass
		'''移动搜索'''
		# now_handle = self.driver.current_window_handle # 获取当前窗口句柄
		# self.driver.find_element_by_id("skeywords").clear()
		# self.driver.find_element_by_id("skeywords").send_keys(u'华为')
		# # t1 = self.driver.find_element_by_id("skeywords").text()
		# # self.driver.find_element_by_class_name('b').click()
		# all_handles = self.driver.window_handles # 获取所有窗口句柄
		# # print t1
	# 	for handle in all_handles:
	# 		if handle != now_handle:
	# 			# print handle  # 输出待选择的窗口句柄
	# 			self.driver.switch_to_window(handle)
	# 			t1 = self.driver.find_element_by_id("search").getText()  # 输出待选择的窗口句柄
	# 			print t1
    #
		# self.assertEquals(t1,u"华为")
	def test_yidong_02(self):
		'''悬浮定位'''
		# chain = ActionChains(driver)
		# implement = driver.find_element_by_link_text()
		# chain.move_to_element(implement).perform()
		chain = ActionChains(self.driver)
		ele = self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[4]/div[1]/a[1]")
		chain.move_to_element(ele).perform()		
		ele1 = self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[4]/div[2]/dl[2]/dd/a[1]")
		ele1.click()
		time.sleep(3)
		ele2 = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/ul/li[1]/div[2]/p/a")
		elw2.click()
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
	
		