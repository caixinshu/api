# -*- coding: utf-8 -*- 

import xlrd
import sys
import re


'''
Created on 2015-4-27
读取excel
@author: 胡晓燕
'''
def open_excel(file,encoding="utf-8"):
   try: 
      data = xlrd.open_workbook(file) 
      return data
   except Exception,e:
         print str(e)


#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行，by_index：表的索引
def excel_table_byindex(file,colnameindex=0,by_index=0):
     data = open_excel(file)
     table = data.sheets()[by_index]
     nrows = table.nrows #总行数
     ncols = table.ncols #总列数
     colnames =  table.row_values(colnameindex) #表头所在行
     list =[]
     for rownum in range(1,nrows):
           row = table.row_values(rownum)
           if row:
              app = {}
              for i in range(1,len(colnames)):
                  app[colnames[i]] = row[i]                               
              list.append(app)

     return list
      
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行  ，by_name：Sheet1名称
def excel_table_byname(file,colnameindex=0,by_name="sheet1"):
     data = open_excel(file)
     table = data.sheet_by_name(by_name)
     nrows = table.nrows #总行数
     nclos=table.ncols #总列数
     colnames =  table.row_values(colnameindex)#打印第一行的数据
     list =[]
     for rownum in range(1,nrows):
          row = table.row_values(rownum)
          if row:
            app = {}
            for i in range(1,nclos):
                 app[colnames[i]] = row[i]                  
            list.append(app)
     return list
      
def main():
  #tables = excel_table_byindex("D:/workspace/apitest/data/dianqian.xls",0,0)
  #for row in tables:
  #print type(row)
  #print row
  # print tables[0]
  # print tables[1]

#   xx= tables[2]['Parameter']
#   print xx
#   print vrifyPara("requestinfo",xx)
#   print type (xx)
#   print xx['requestinfo'.decode('utf8')]
  tables = excel_table_byname("D:\\pythonworkspace\\autotesting\\data\\study.xls",0,"login")
  print tables
  print type(tables)
#
if __name__=="__main__":
  print excel_table_byname(r'E:\pythonforthstudy\framwork\autotesting\data\study1.xls',by_name='addbook')
#
import suds


        