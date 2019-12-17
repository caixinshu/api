#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.w3school.com.cn/tiy/t.asp?f=html_frame_mix")
#窗口最大化
driver.maximize_window()
time.sleep(2)
# print driver.find_element_by_id("id1").text
# driver.switch_to.frame(0)
# #driver.switch_to.frame("idname")
# print driver.find_element_by_name("inside").get_attribute("value")
# driver.switch_to.default_content()
# print driver.find_element_by_id("name").get_attribute("value")

#复杂的frame的练习

driver.switch_to.frame("i")
driver.switch_to.frame(0)
print driver.find_element_by_xpath("//h3").text
driver.switch_to.default_content()
driver.switch_to.frame("i")
driver.switch_to.frame(1)
print driver.find_element_by_xpath("//h3").text
driver.switch_to.default_content()
driver.switch_to.frame("i")
driver.switch_to.frame(2)
print driver.find_element_by_xpath("//h3").text
driver.switch_to.default_content()
print driver.title


#切到当前窗口
# driver.switch_to.window(driver.current_window_handle)
#
# #获取所有浏览器的句柄
# handlslist=driver.window_handles
# for hand in handlslist:
#     driver.switch_to.window(hand)
#     print driver.title