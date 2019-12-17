#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get(r"E:\pythonforthstudy\framwork\studyselenium02\demo\control.html")
#窗口最大化
driver.maximize_window()
divsen=driver.find_element_by_xpath("/html/body/div/form/div[2]")
# print divsen.text
#
# divlist =driver.find_elements_by_xpath("//form/div")
# print len(divlist)
#
# divlist1 =driver.find_elements_by_xpath("//div")
# print len(divlist1)
#

# lastinput=driver.find_element_by_xpath("//input[@class='stuname' and @type='text']")
# lastinput.send_keys(u"龙腾测试")
#
# mentlist=driver.find_elements_by_xpath("//*[@class]")
#
# for ment in mentlist:
#     print ment.tag_name
#
#

#print driver.find_element_by_xpath("//div").text



elementlist = driver.find_elements_by_xpath("//*[contains(@type,'ckb')]")
#print elementlist.get_attribute("type")
for elmet in elementlist:
    print elmet.get_attribute("type")



elementlist1 = driver.find_elements_by_xpath("//div[contains(text(),'本书')]")
for elm in elementlist1:
    print elm.text



element2 = driver.find_elements_by_xpath("//input[starts-with(@id,'a')]")
for ment in element2:
    print ment.tag_name

# list=driver.find_elements_by_xpath("/html//div")
# print(len(list))
#list1=driver.find_elements_by_xpath("//div")
#print(len(list1))

# list2=driver.find_elements_by_xpath("//input[contains(@id,'u') and @type='checkbox']")
# print(len(list2))
#list3=driver.find_elements_by_xpath("//input[contains(@type,'check')]")
# list3.index()
# print(len(list3))
#
# print driver.find_element_by_xpath("//div[text()='第三个div']").text
#
#
# driver.close()


# list2=driver.find_elements_by_xpath("//input[not(contains(@type,'checkbox'))]")
# list2[3].click()
# print(len(list2))