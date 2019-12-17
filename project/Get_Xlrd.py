#coding=utf-8


import xlrd


'''dicts = {'a':1,'b':2}
i = json.dumps(dicts)# 字典变字符串
print i
print type(i)
s = json.loads(i)# 字符串变字典
print s,type(s)'''
# tables = xlrd.open_workbook('../project/mail_list.xls')
# sheet_data = tables.sheets()[0]
# print sheet_data.nrows
# print sheet_data.cell(3,3).value
class OpereEXcel():
	
	def __init__(self, file_path=None):
		if file_path == None:
			self.file_path = '../project/mail_list.xls'
		else:
			self.file_path = file_path
		self.excel = self.get_excel()

	def get_excel(self):
		tables = xlrd.open_workbook(self.file_path)
		return tables

	def get_sheet(self,i=None):
		if i == None:
			i=0
		sheet_data = self.excel.sheets()[i]
		return sheet_data

	def get_lines(self):
		return self.get_sheet().nrows

	def get_cell(self,row,cell):
		return self.get_sheet().cell(row,cell).value

if __name__ == '__main__':
	book = OpereEXcel()
	# print book.get_lines()
	print book.get_cell(4,4)