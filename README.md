# api测试用例编写



# -*- coding: UTF-8 -*-
from config import url
import unittest
import requests
import l_db
import HTMLTestRunner
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class bookapi():

    def setUp(self):
        data={'token':'a724636d6dba10a8e92d351e9d783ebcc3a4de79','id':1}

    def Test_1(self):
        data={'token':'a724636d6dba10a8e92d351e9d783ebcc3a4de79','id':1}
        l_db.updatabook(1,0)

        r=requests.post(url.lendbookurl,json=data)
        print r.content
        l_db.searchbook(1)[0][6]
        self.asserEqual(1,l_db.searchbook(1)[0][6])
        #self.asserEqual('sucess',r.json()['result']['status'])

    def test_002(self):
        data1 = {'token':'990f30e4eacae25ed9e11b8d573d95e62725af71','id':1}
        r=requests.post('http://127.0.0.1:8000/ltcs/api/book/lend',json=data1)
        print r.content


# #coding:utf-8
# import MySQLdb
# import requests
# import unittest
# from config import url
# from test.util import lib_db
# class API(unittest.TestCase):
#     def test_01(self):
#       data1 = {'token':'990f30e4eacae25ed9e11b8d573d95e62725af71','id':1}
#       lib_db.updatebook(1,0)
#       r=requests.post(url.lendbookurl,json=data1)
#       print r.content
#       self.assertEqual(1,lib_db.searchbook1(2)[0][6])
#       # self.assertEqual('failed',r.json()['result']['status'])
#     # def test_02(self):
#     #     ''''''
#
#     def test_002(self):
#        data1 = {'token':'990f30e4eacae25ed9e11b8d573d95e62725af71','id':1}
#        r=requests.post('http://127.0.0.1:8000/ltcs/api/book/lend',json=data1)
#        print r.content

#congfig配置文件&URL 
# -*- coding: UTF-8 -*-
host="127.0.0.1"
user="root"
password="root"
database="ltcs"
port=3306
#登录系统的用户名，密码
loginusername="root"
loginpassword="root"

#数据库操作
# -*- coding: UTF-8 -*-
from config import config
import MySQLdb
'''数据库的操作'''
def query_db(sql):
    try:
        connection=MySQLdb.connect(config.host,config.user,
                                   config.password,config.database,charset='utf-8')
        cursor=connection.cursor()
        cursor.execute(sql)
        cursor.close()
        connection.commit()
        connection.close()
    except Exception,e:
        print str(e)
        exit(0)


def select_db(sql):
    try:
        connection=MySQLdb.connect(config.host,config.user,
                                   config.password,config.database,charset='utf-8')
        print connection
        cursor=connection.cursor()
        cursor.execute(sql)
        rs=cursor.fetchall()
        cursor.close()
        connection.close()
    except Exception,e:
        print str(e)
        exit(0)
    return  rs
def searchbook(bookid):
    sql="select * from ltcs_book where id=%d"%(bookid)
    db= select_db(sql)
    return db
def updatabook(bookid,num):
    sql="updata ltcs_book set lend_num=%d where id=%d"%(num,bookid)
    query_db(sql)




