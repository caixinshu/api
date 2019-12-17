# coding=utf-8
from selenium import webdriver
import time, csv


##########打印字符串##########
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


def openBrowser():
    browser = webdriver.Firefox()
    browser.get("http://www.zjgt.com/")
    browser.maximize_window()

    return browser


#########输入用户名密码，登录系统##########
def readCsv2():
    driver = openBrowser()
    # 每一行返回一个字典
    for d in csv.DictReader(open("data/csvdata2.csv", "rb")):
        print d
        print d.get("UserName")
        # 通过id方式定位
        driver.find_element_by_id("DengLu").click()
        # 通过id方式定位
        driver.find_element_by_id("login_userName").send_keys(d.get("UserName"))
        driver.find_element_by_id("login_userPassWorld").send_keys(d.get("PassWord"))
        driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        a = driver.find_element_by_id("TuiChu").text
        driver.find_element_by_id("TuiChu").click()
        print a
        #########检查是否登录成功##################
        if a == u"[退出]":
            printme("登录成功！")
        else:
            printme("登录失败！")
        time.sleep(1)



readCsv2()
