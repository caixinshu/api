# coding=utf-8

import re


n = 0 
m = 0
for i in range(365):
	m = m + 1
	n = n + i
	if n > 10000:
		print m
		break
print n	

