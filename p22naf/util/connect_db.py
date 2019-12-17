#coding:utf-8
import pymysql.cursors
import json
class OperationMysql:
	def __init__(self):
		self.conn = pymysql.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='root',
			db='test',
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		result = json.dumps(result)
		return result

	#插入一条数据
	def insert_one(self,sql,params):
		self.cur.execute(sql,params)
		self.conn.commit()

	def delete_one(self,sql,params):
		self.cur.execute(sql,params)

if __name__ == '__main__':
	op_mysql = OperationMysql()
	# res = op_mysql.search_one("select * from username where username='lisi'")
	# print(res)
	pa = 'sunhou'
	re = op_mysql.insert_one("insert into username(username) values (%s)",pa)
