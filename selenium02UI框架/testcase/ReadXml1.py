#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse(r'E:\pythonforthstudy\framwork\studyselenium02\data\abc.xml')

#得到文档元素对象
root = dom.documentElement

bb = root.getElementsByTagName('maxid')
b= bb[0]
print b.nodeName

bb = root.getElementsByTagName('login')
b= bb[0]
print b.nodeName