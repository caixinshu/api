#coding=utf-8
import time
import win32api
import win32con
from selenium import webdriver
from loggingstusy.loggingsty import logtest002
from tools import uploadfile
driver=webdriver.Firefox()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
driver.maximize_window()
# html_div3s=driver.find_elements_by_xpath('/html//div')
# l3=[]
# for html_div3 in html_div3s:
#     print html_div3.get_attribute('id')
#     l3.append('html_div3')
# print len(l3)
logtest002().info("aaaaaaaaaaaaaaaaaa")
driver.find_element_by_id("file").click()
uploadfile.setText("D:\log.txt")
win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
win32api.keybd_event(86,0,0,0)  #v键位码是86
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(2)
logtest002().warning("bbbbbbbbbbbbbbbbbbb")
win32api.keybd_event(13,0,0,0)  #回车位码是13
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
logtest002().debug("cccccccccccccccc")
logging.info("ssssssssssssssss")