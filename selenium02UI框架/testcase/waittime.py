#coding=utf-8
from selenium import webdriver
#导入WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
#导入time 包
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#添加隐性等待
driver.implicitly_wait(30)
#显性等待
#element=WebDriverWait(driver, 50).until(lambda driver :driver.find_element_by_id("kw"))
#等待某元素可见
#element=WebDriverWait(driver, 50).until(expected_conditions.element_to_be_clickable(By.ID,"kw"))
#等待某文本值出现
ss=WebDriverWait(driver, 50).until(expected_conditions.text_to_be_present_in_element((By.LINK_TEXT,u"把百度设为主页"),u"把百度设为主页"))
# #元素可见后再执行
# element=WebDriverWait(driver, 50).until(expected_conditions.visibility_of_element_located(By.ID,"kw"))
# element.send_keys("selenium")
print type(ss)
# #另一种写法
#
#
# driver.find_element_by_id("su").click()
# #添加固定休眠时间
# time.sleep(5)
# driver.quit()
