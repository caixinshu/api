# -*- coding:utf-8 -*-

import exrex
import crypt
'''
用于unix暴力破解，文件字典和密码文件
'''

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dicfile = open('xxx.txt','r')
	for word in dicfile.readlines():
		word = word.strip('\n'	)# 去空格
		cryptWord = crypt.crypt(word,salt)
		if cryptPass == cryptWord:
			print ('Found passwd:',word)
			return
		print('Passwd not found')
		return

def main():
	passfile = open('password.txt','r')
	for line in passfile.readlines():
		user = line.split(':')[0]
		cryptPass = line.split(':')[1].strip('')
		print ('Cracking Passswd for:',user)
		testPass(cryptPass)


if __name__ == '__main__':
	main()