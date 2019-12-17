#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/index.htm")
#点击打开搜索设置
driver.find_element_by_link_text("Alert Test").click()
time.sleep(10)
#点击打开搜索设置
driver.find_element_by_name("b1").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
alert.dismiss()
alert.send_keys("ddddd")
#driver.quit()