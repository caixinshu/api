import sys
from zipfile import ZipFile


if len(sys.argv) <= 2:
	print('\n  Usage:')
	print('         python unzip.py text.zip password.txt\n\n')
	sys.exit(0)

# print(len(sys.argv))
# sys.exit()

def z_file(filename,password):

	zFile = ZipFile(filename)	
	zFile.extractall(pwd=password)
	


def main():
	filename = sys.argv[1]
	passwords = sys.argv[2]

	f = open(passwords,'r')
	for pw in f.readlines():
		try:
			z_file(filename,pw.strip('\n'))
		except Exception, e:
			print('Error :',e)
		else:
			print('PassWord is:',pw.strip('\n'))

if __name__ == '__main__':
		
	main()