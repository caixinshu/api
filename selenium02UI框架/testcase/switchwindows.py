#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://bj.ganji.com/")
#窗口最大化
driver.maximize_window()
#获得当前窗口
currhandle=driver.current_window_handle
print(u'sssss~~~~'+currhandle)
print driver.title
#打开租房页面
driver.find_element_by_link_text(u"租房").click()

driver.maximize_window()
#获得所有窗口的handles
allhandles=driver.window_handles
#循环判断窗口是否为当前窗口
for handle in allhandles:
  if handle != currhandle:
    driver.switch_to.window(handle)
    print u'找到了想要的窗口~~~'
    time.sleep(5)
    #切换租房详细页面
    driver.find_element_by_link_text(u"海淀").click()
    # driver.close()
#回到原先的窗口
driver.switch_to.window(currhandle)
driver.find_element_by_link_text(u"合租").click()
print 12345555
time.sleep(3)
# driver.quit()


def swithWin(title):
  allhandles=driver.window_handles
  #循环判断窗口是否为当前窗口
  for handle in allhandles:
    #if handle != currhandle:
      driver.switch_to.window(handle)
      if title in driver.title:
        print u'找到了想要的窗口~~~'

#
# swithWin(u"二手手机")
# swithWin(u"整租")