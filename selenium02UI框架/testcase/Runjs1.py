#coding=utf-8
from selenium import webdriver
#高亮
dirver = webdriver.Firefox()
dirver.get( "http://www.baidu.com")
dirver.implicitly_wait(5)
dirver.maximize_window()
dirver.find_element_by_id("kw").send_keys(u"测试")
dirver.execute_script("q = document.getElementById('kw');" + "q.style.border = '1px solid red';")
dirver.execute_script("button= document.getElementById('su');" + "button.click();")
# dirver.execute_script("alert(\"hello,this is a alert!\");value=\"Alert\" ")
