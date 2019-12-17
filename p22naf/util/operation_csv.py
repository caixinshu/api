#!/usr/bin/env python
# -*- coding=utf-8 -*-

import csv

def readcsv():
    with open('E:\p22naf\dataconfig\case2.csv','r') as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            print(i)

def readcsvDit():
    with open('E:\p22naf\dataconfig\case2.csv','r') as f:
        reader = csv.DictReader(f)
        for i in reader:
            print(i)

if __name__ == '__main__':
    readcsvDit()