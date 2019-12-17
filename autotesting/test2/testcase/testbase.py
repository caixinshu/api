#  -*- coding: utf-8 -*
import requests

from suds.client import Client
from config import url
from tools import readexceldata

#初始化url

class test:
      def __init__(self,url,file,colnameindex,by_name):
          self.url=url
          self.file=file
          self.colnameindex=colnameindex
          self.by_name=by_name

      def getclient(self):#生成客户端
          client=Client(self.url)
          return client
      def getdata(self):#获得excel表单数据
          data=readexceldata.excel_table_byname(self.file,self.colnameindex,self.by_name)
          return data
def main():
  test1=test(url.loginurl,"E:\\workspacepython\\apiteststudy\\data\\study.xls",0,"login")
  print "111"
  print test1.getdata()

if __name__=="__main__":
    main()




