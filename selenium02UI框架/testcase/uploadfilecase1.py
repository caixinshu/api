#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://localhost:63342/studyselenium02/demo/uplad.html')
#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\1.jpg')
time.sleep(2)
driver.quit()
