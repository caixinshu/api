#!/usr/bin/env python
# -*- coding=utf-8 -*-

import random
import time
import calendar
import math
import string

# 11 有点难度
# for i in range(1,6):
#     for j in range(i+1,7):
#         if j > 1+i and j <6 and i >1:
#             print(" " ,end=" ")
#         else:
#             print("*",end=" ")
#     print()

# 13
# l = []
# while True:
#     a = int(input('输入数字：'))
#
#     if a%2 == 0:
#         l.append(a)
#         print(l)
#         if len(l)==3:
#             l.sort()
#             print(l)
#             break
#     else:
#         print(l)
#         continue

# 15
# s = 0
# for i in range(1,101):
#     if i%3 == 0:
#         s = i+s
# print(s)

# 16
# n = 100
# for i in range(1,n):
#     s = (1+n)*(n/2)
#
# print(int(s))

# 17
# while True:
#     n = int(input('输入:'))
#     if n**2 <50:
#         print(n**2)
#         break
#     else:
#         print(n**2)
#         continue

# 23
# s = input('输入字符串：')
# n = 0
# for i in s:
#     if i == 'b':
#         n += 1
# print(n)

# 24
# s = input('输入字符串：')
# n = {}
#
# for i in s:
#     if i in n:
#         n[i] += 1
#     else:
#         n[i] = 1
#
# print(n)

# 25
# i = 0
# for num in range(1,101):
#     if num>1:
#         for j in range(2,num):
#             if num%j == 0:
#                 break
#         else:
#             i += num
#
# print(i)

# 26

# for num in range(1,2100):
#     if (num%4==0) and (num%100!=0) or (num%400==0):
#         print('{}为闰年'.format(num))
#     else:
#         print('{}为非闰年'.format(num))
#
#
# for n in range(1000,2000):
#     check_year=calendar.isleap(n)
#     if check_year == True:
#         print ("{}年是闰年".format(n))
#     else:
#         print ("{}年是平年".format(n))

# 30
# a = float(input('输入数字：'))
# b = float(input('输入数字：'))
# c = float(input('输入数字：'))
#
# p = (a+b+c)/2
# s = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(s)

#31
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,end=' ')
#     print()

# for x in range(1,10000):
#     i = math.sqrt(x + 100)
#     if float.is_integer(i):
#         j = math.sqrt(x + 268)
#         if float.is_integer(j):
#             print(x)

# 34
# y = int(input('输入年份：'))
# m = int(input('输入月份：'))
# d = int(input('输入日子：'))
#
# days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
# check_year=calendar.isleap(y)
# if check_year == True:
#     if m>2:
#         day = days[m-1]+d+1
#     else:
#         day = days[m-1]+d
# else:
#     day = days[m-1]+d
#
# print(day)

# 35
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# r = [[0,0,0],
#     [0 ,0,0],
#     [0 ,0,0]]
#
# for i in range(3):
#     for j in range(3):
#         r[i][j] = X[i][j] + Y[i][j]
#
# print(r)

# 36
# s = 'are you ok ! 黎明。'
# s_n = 0
# z_n = 0
# o_n = 0
# for i in range(len(s)):
#     if s[i].isspace():
#         s_n += 1
#     if s[i].isalpha():
#         z_n += 1
#     else:
#         o_n += 1
#
# print('空格个数为{},字符个数为{}，特殊个数为{}'.format(s_n,z_n,o_n))

# 37
# s = '1234567890'
#
# for i in s:
#     if i.isalnum():
#         print('{}是数字'.format(i))

# s = "你好，我好，大家好才是真的好！"

# n_s = s[:7]+s[8:]
# print(n_s)
# for i in range(len(s)):
#     if s[i] == '好':
#         s1 = s.replace('好','*')
# print(s1)



#
# numb = []
# for i in range(0, 200):
#     l = string.ascii_letters
#     l = list(l)
#     random.shuffle(l)
#     l=''.join(l[:8])
#     numb.append(l)
# print(numb)

# l = string.ascii_letters
# F = set()
#
# while len(F)<200:
#     c=set()
#     while len(c)<8:
#         c.add(random.choice(l))
#     c = ''.join(c)
#     F.add(c)
# for i in F:
#     print(i)
#
# 40

def draw(x=5,y=5,z='*'):
    for i in range(x+1):
        for j in range(y):
            if i==x:
                print(i*(z+' '))

if __name__ == '__main__':
    draw(3,4,'@')






