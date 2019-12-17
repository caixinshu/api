#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://localhost:63342/studyselenium02/demo/control.html")
#窗口最大化
driver.maximize_window()
#在父亲元件下找到label内容
divnum =driver.find_element_by_class_name('fathdiv')
labellist=divnum.find_elements_by_tag_name('label')
for label in labellist:
    print(label.text)
#driver.close()