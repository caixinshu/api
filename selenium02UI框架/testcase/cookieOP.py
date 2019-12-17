#coding=utf-8

# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# #向cookie的name 和value添加会话信息。
# driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
#
# #遍历cookies中的name 和value信息打印，当然还有上面添加的信息
# for cookie in driver.get_cookies():
#    print( "%s -> %s" % (cookie['name'], cookie['value']))
#
# # print(driver.get_cookie("name"))
# # 下面可以通过两种方式删除cookie
# # 删除一个特定的cookie
# #driver.delete_cookie("CookieName")
# # 删除所有cookie
# #driver.delete_all_cookies()
#
# time.sleep(2)
# driver.close()


# 交互动作    将动作附加到动作链中串行执行
from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()