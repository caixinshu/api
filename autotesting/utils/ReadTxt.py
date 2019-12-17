# coding=utf-8
from selenium import webdriver
import time
def readTxt():
    file = open("data/textdata.txt", "rb")
    lines = file.readlines()
    for line in lines:
        print line
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8081/examonline/index.jsp")
        driver.maximize_window()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(line.decode('GB2312'))
        driver.find_element_by_id("userpass").clear()
        driver.find_element_by_id("userpass").send_keys("123456")
        driver.find_element_by_id("tvery").clear()
        driver.find_element_by_id("tvery").send_keys("1234")
        driver.find_element_by_id("btnsubmit").click()
        time.sleep(1)
        driver.close()
    file.close()

readTxt()
