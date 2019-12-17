#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('data/abc.xml')

#得到文档元素对象
root = dom.documentElement

itemlist = root.getElementsByTagName('login')
item = itemlist[0]
un=item.getAttribute("username")
print un
pd=item.getAttribute("passwd")
print pd

ii = root.getElementsByTagName('item')
i1 = ii[0]
i=i1.getAttribute("id")
print i

i2 = ii[1]
i=i2.getAttribute("id")
print i