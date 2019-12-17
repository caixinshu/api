#coding=utf-8
from selenium import webdriver
import time,csv

def readCsv2():
    #每一行返回一个字典
  for d in csv.DictReader(open("data/csvdata2.csv","rb")):
   print d
   print d.get("UserName")
   driver = webdriver.Firefox()
   driver.get("http://127.0.0.1:8081/examonline/index.jsp")
   driver.maximize_window()
   driver.find_element_by_id("username").clear()
   driver.find_element_by_id("username").send_keys(d.get("UserName").decode('GB2312'))
   driver.find_element_by_id("userpass").clear()
   driver.find_element_by_id("userpass").send_keys(d.get("PassWord").decode('GB2312'))
   driver.find_element_by_id("tvery").clear()
   driver.find_element_by_id("tvery").send_keys("1234")
   driver.find_element_by_id("btnsubmit").click()
   time.sleep(1)
   driver.close()
readCsv2()