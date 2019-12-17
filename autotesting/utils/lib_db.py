# -*- coding: utf-8 -*
'''
Created on 2015-5-28

@author: 胡晓燕
'''
# 连接数据库
import MySQLdb
from config import config

# class DBUnit:
#  def __init__(self,user=None,passwd=None,host=None,database=None):
#   try:
#    self.connection = pymssql.connect(host=host, user = user, password =passwd, database=database)
#    self.cursor= self.connection.cursor()
#   except:
#    print "Could not connect to DB server."
#    exit(0)

def query_db(sql):
  try:
   connection = MySQLdb.connect(config.host,config.user, config.password,config.database,charset='utf8')
   cursor= connection.cursor()
   cursor.execute(sql)
   cursor.close()
   connection.commit()
   connection.close()
  except Exception,e:
   print str(e)
   exit(0)


def select_db(sql):
  try:
   connection = MySQLdb.connect(config.host,config.user, config.password,config.database,charset='utf8')
   print connection
   cursor= connection.cursor()
   cursor.execute(sql)
   rs = cursor.fetchall()
   cursor.close()
   connection.close()
  except Exception,e:
    print str(e)
    exit(0)
  return rs


#对数据库的操作，可用于数据库断言，操作数据后更新便于数据复用
# 更新语句样列
# def updatematch(match,id):
#   sql="update stepcaifu set matchNo=%s where id=%s"%(match,id)
#   query_db(sql)
# updatematch("233334","220")


# 查询语句样列
# def selectmatch(id):
#     sql="select * from stepcaifu where id=%s"%(id)
#     db=select_db(sql)
#     return db
# print selectmatch("220")

#插入语句样列
# def insertmatch(id,product):
#       sql="insert into stepcaifu(id,product) values('%d','%s')"%(id,product)
#       query_db(sql)
#
# insertmatch(702,"huxiaoyan")

#查询图书
def searchbook():
    sql="select count(id) from ltcs_book"
    db=select_db(sql)
    return db
#根据bookid查询图书
def searchbook1(bookid):
    sql="select * from ltcs_book where id=%d"%(bookid)
    db=select_db(sql)
    print db
    return db
#更新图书
def updatebook(bookid,num):
    sql="update ltcs_book set lend_num=%d where id=%d"%(num,bookid)
    query_db(sql)
#删除一条图书记录
def deletebook():
    sql="delete from ltcs_book order by id desc limit 1"
    query_db(sql)
#清空表里的数据
def deletetable():
    sql="TRUNCATE TABLE ltcs_book"
    query_db(sql)
#插入表中数据
def insertbook(name,author,publishing,isbn,total_num,lend_num):
    sql="insert into ltcs_book(name,author,publishing,isbn,total_num,lend_num)values('%s','%s','%s','%s','%d','%d')"%(name,author,publishing,isbn,total_num,lend_num)
    query_db(sql)
#insertbook('xiaoye','ss','s','ssd',1,2)
