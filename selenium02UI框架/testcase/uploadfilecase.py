# -*- encoding: utf-8 -*-
from selenium import webdriver
from tools.uploadfile import setText,getText
import time
import win32api
import win32con
import win32clipboard as board
import win32con
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#打开火狐浏览器
driver = webdriver.Firefox()
#打开谷歌浏览器
#driver = webdriver.Chrome('lib//chromedriver.exe')
#打开ie浏览器
#driver = webdriver.Ie('lib//IEDriverServer.exe')
#打开赶集网
driver.get('http://localhost:63342/studyselenium02/demo/uplad.html')
driver.maximize_window()
driver.find_element_by_name("file").click()
time.sleep(2)
setText("C:\Users\yezhixi\Desktop\study.txt")
win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
win32api.keybd_event(86,0,0,0)  #v键位码是86
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键v
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) #释放ctrl
win32api.keybd_event(13,0,0,0)  #模拟回车键盘
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)  #释放回车键盘