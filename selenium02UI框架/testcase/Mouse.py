#coding=utf-8

#引入ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
driver.implicitly_wait(5)
#定位元素的原位置
element = driver.find_element_by_id("dragger")
#定位元素要移动到的目标位置
# target = driver.find_element_by_xpath("/html/body/div[3]")
# #定位到第二个目标源
# target1 = driver.find_element_by_xpath("/html/body/div[4]")
# #执行元素的移动操作
# ActionChains(driver).drag_and_drop(element, target).perform()
# time.sleep(3)
#
# ActionChains(driver).drag_and_drop(element, target1).perform()
target = driver.find_elements_by_class_name('item')
for i in target:
    ActionChains(driver).drag_and_drop(element, i).perform()



#练习悬浮
# driver.implicitly_wait(10)
# driver.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d6c490f6ed0a43bdaea6ebbc9a8b961c')
# # target = driver.find_element_by_link_text(u'我的京东')
#
# ActionChains(driver).move_to_element(driver.find_element_by_link_text(u'我的京东')).perform()
# time.sleep(5)
# driver.find_element_by_link_text(u'我的理财').click()