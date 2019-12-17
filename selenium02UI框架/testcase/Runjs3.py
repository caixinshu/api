#coding=utf-8
from selenium import webdriver
#操作日期控件
dirver = webdriver.Firefox()
dirver.get( "http://localhost:63342/studyselenium02/demo/Time/date.html")
dirver.implicitly_wait(5)
dirver.maximize_window()
startJs="$(\"input[placeholder='开始时间≥当前时间']\").removeAttr('readonly');$(\"input[placeholder='开始时间≥当前时间']\").attr('value','2016-06-23 00:00')"
endJs="$(\"input[placeholder='结束时间>开始时间']\").removeAttr('readonly');"
dirver.execute_script(startJs)
dirver.execute_script(endJs)
dirver.find_element_by_xpath("/html/body/div[1]/ul[2]/li/div[2]/input[2]").send_keys("2016-06-24 00:00")
dirver.find_element_by_link_text("基础信息").click()