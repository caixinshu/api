#coding:utf-8

from selenium.webdriver.support.expected_conditions import NoSuchElementException

class BasePage(object):
	def __init__(self,driver):
		self.driver=driver

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException,e:
			print 'Error details :%s'%(e.args[0])

	def findElements(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException,e:
			print 'Error details :%s'%(e.args[0])

















