
# -*- coding: utf-8 -*-

import os

import xlwt
from xlutils.copy import copy

import readexceldata

'''
Created on 2015-4-27
'写入excel'
@author:
'''

FILEPATH ='E:/name1.xls'  #定义读取excel的路径
#该路径下自动创建excel，增加一张sheet表单
def createxce(sheetname,file=FILEPATH):
  try:
     file =xlwt.Workbook(encoding="utf-8")
     sheet1=file.add_sheet(sheetname, cell_overwrite_ok=True)
     file.save(file)
     print "done"
  except Exception,e:
   print str(e)

#在该路径下更新指定对应的excel，根据行号，列号，sheet表索引
def write_excel(file,sheetindex,rownum,colnum,value):
       sourcedata= readexceldata.open_excel(file)
       wb=copy(sourcedata)
       w_sheet=wb.get_sheet(sheetindex)
       w_sheet.write(rownum,colnum,value)
       wb.save(file)
