# coding=utf-8
from selenium import webdriver
import time, csv
def readCsv1():
    myData = csv.reader(file("data/csvdata1.csv", "r"))
    for line in myData:
        # 第一列
        print line[0].decode('GB2312') + u"第一列的吧~"
        # 第二列
        print line[1].decode('GB2312')
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8081/examonline/index.jsp")
        driver.maximize_window()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(line[0].decode('GB2312'))
        driver.find_element_by_id("userpass").clear()
        driver.find_element_by_id("userpass").send_keys(line[1].decode('GB2312'))
        driver.find_element_by_id("tvery").clear()
        driver.find_element_by_id("tvery").send_keys("1234")
        driver.find_element_by_id("btnsubmit").click()
        time.sleep(1)
        driver.close()


readCsv1()
