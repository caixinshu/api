# -*- encoding: utf-8 -*-
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#开启一个空的浏览器
driver = webdriver.Firefox()
#driver = webdriver.Chrome('F:\\driver\\chromedriver.exe')
#driver = webdriver.Ie('F:\\driver\\chromedriver.exe')
#打开要测试的页面
driver.get('http://localhost:63342/studyselenium02/demo/control.html')
#浏览器最大化
driver.maximize_window()
driver.find_element_by_id("accountID").send_keys(u"张三")

print driver.find_element_by_id("accountID").get_attribute("value")

driver.find_element_by_id("accountID").clear()

driver.find_element(By.ID,"accountID").send_keys(u"lisi")

driver.find_element_by_id("passwordID").send_keys("123456")

print driver.find_element_by_xpath("html/body/div[1]/form/div[1]").text

Select(driver.find_element_by_id("areaID")).select_by_index(2)

print driver.find_element_by_id("areaID").text

driver.page_source