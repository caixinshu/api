# coding=utf-8
from selenium import webdriver
import time, csv
def readCsv1(filename):
    myData = csv.reader(file(filename, "r"))
    rows=[]
    for line in myData:
        print line
        rows.append(line)
    return rows

