# -*- coding: utf-8 -*-
#
# author: oldj <oldj.wu@gmail.com>
#
 
from selenium import webdriver
import time
 
#保存到当前目录下
def capture(url, save_fn="capture.png"):
  driver = webdriver.Firefox() # Get local session of firefox
  driver.implicitly_wait(30);
  driver.set_window_size(1200, 900)
  driver.get(url) # Load page
  driver.save_screenshot(save_fn)
  driver.close()

#保存到E盘下
def capture1(url, save_fn="e:/capture.png"):
  browser = webdriver.Firefox() # Get local session of firefox
  browser.implicitly_wait(30);
  browser.set_window_size(1200, 900)
  browser.get(url) # Load page
  browser.get_screenshot_as_file(save_fn)
  browser.close()
 
if __name__ == "__main__":
 
  capture("http://baidu.com")
  capture1("http://baidu.com")