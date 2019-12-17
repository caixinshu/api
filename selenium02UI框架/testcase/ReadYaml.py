# -*- coding: utf-8 -*-
import os
import yaml
def get_value(key,configname):
    B_DIR = os.path.dirname(__file__)
    print B_DIR
    #通过yaml文件获取定位信息
    file_path = os.path.join(B_DIR,"data",configname)
    print file_path
    file = open(file_path)
    value = yaml.load(file)
    print value
    file.close()
    try:
        data = value[key]
        print data
        return data
    except KeyError:
        print '文件中找不到%s' %key

get_value("UserName","yamldata.yaml")