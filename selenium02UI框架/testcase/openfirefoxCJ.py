# -*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from  log001 import logprint

profilepath = r"C:\Users\liyingfeng\AppData\Roaming\Mozilla\Firefox\Profiles\c1r4vm2f.default"
#打开火狐浏览器
profile = webdriver.FirefoxProfile(profilepath)
logprint().info("设置配置所有数据的配置文件")
driver=webdriver.Firefox(profile)
logprint().info("打开火狐浏览器")
#打开谷歌浏览器
#driver = webdriver.Chrome('lib//chromedriver.exe')
#打开ie浏览器
#driver = webdriver.Ie('lib//IEDriverServer.exe')
#打开赶集网
driver.get('http://bj.ganji.com/')
logprint().info("打开赶集网站")
driver.forward()

#赶集网页面最大化
driver.maximize_window()
#输出页面的title
print driver.title
#输出当前url
print driver.current_url
#页面后退
driver.back()
#刷新页面
driver.refresh()
#关闭浏览器
# driver.close()
#
# driver.quit()

