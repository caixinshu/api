#python2
#coding=utf-8

import sys, time
from zipfile import ZipFile

if len(sys.argv) <= 2:
	print('\n  Usage:')
	print('         python unzip2.py text.zip password.txt\n\n')
	sys.exit(0)

def z_file(file,fileName,password):
	file.extract(member=fileName,path='./',pwd=password)

def z_fileFast(file,fileName,password):
	info = file.getinfo(fileName)
	source = file.open(name=info,pwd=password)
	source.read(10)
	source.close()

def z_fileList(zFile,fileList,password):
	for fileName in fileList:
		try:
			z_fileFast(zFile,fileName,password)
			#z_file(zFile,fileName,password)
		except Exception, e:
			#print(e)
			return False
	return True

def z_fileOne(zFile,fileName,password):
	try:
		z_fileFast(zFile,fileName,password)
		#z_file(zFile,fileName,password)
	except Exception, e:
		#print(e)
		return False
	return True

def main():
	filename = sys.argv[1]
	passwords = sys.argv[2]

	t1 = time.time()

	zFile = ZipFile(filename)
	namelist = zFile.namelist();

	#fileList = []
	zFileName = ''
	for name in namelist:
		if name[-1] != '/':
			#fileList.append(name)
			zFileName = name
			break
	if zFileName == '':
		print('No Valid File In Zip \n')
		sys.exit(0)

	f = open(passwords,'r')
	content = f.readlines()
	f.close()

	for pw in content:
		if z_fileOne(zFile,zFileName,pw.strip('\n')):
		#if z_fileList(zFile,fileList,pw.strip('\n')):
			print('PassWord is: %s' % pw.strip('\n'))
			break
	t2 = time.time()
	print('Used time is %d ms' % int((t2-t1)*1000))

if __name__ == '__main__':
	main()