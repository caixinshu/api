# coding=utf-8

import zipfile
import threading
import optparse
import random
# def extractFlie(zFile,password):
# 	'''
# 	用字典暴力破解zip压缩文件密码
# 	'''
# 	try:
# 		zFile.extractall(pwd=password)
# 		print("Found password:",password)
# 		return password
# 	except :
# 		pass

# def main():
# 	zFile=zipfile.ZipFile('unzip.zip')
# 	passFile=open('dictionary.txt')
# 	for line in passFile.readlines():
# 		passFile=line.strip('\n')
# 		t=threading.Thread(target=extractFlie,args=(zFile,password))
# 		t.start()

# if __name__ == '__main__':
# 	main()

def extractFlie(zFile,password):
	'''
	zip压缩文件破解密码增加，指定破解的文件和字典，多线程破解
	'''
	try:
		zFile.extractall(pwd=password)
		print("Found password:",password)
		return password
	except :
		pass

def main():
	parser=optparse.OptionParser('usage%prog -f <zipfile> -d <dictionary>')
	parser.add_option('-f',dest='zname',type='string',help='specify zip file')
	parser.add_option('-d',dest='dname',type='string',help='specify dictionary file')
	options,args=parser.parse_args()
	if options.zname == None and options.dname == None:
		print(parser.usage)
		exit(0)
	else:
		zname=options.zname
		dname=options.dname
	zFile = zipfile.ZipFile(zname)
	dFile = open(dname,'r')
	for line in dFile.readlines():
		password = line.strip('\n')
		t = threading.Thread(target=extractFlie,args=(zFile,password))
		t.start()


if __name__ == '__main__':
	main()




