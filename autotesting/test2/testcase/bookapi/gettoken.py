# -*- coding: utf-8 -*
'''
Created on 2015-2-2

@author: 胡晓燕
'''
from config import url
from config.url import loginurl
from data import datapath
import requests
from config import config
def get_token():
    "获取正确的token"
    logindata={"username":config.loginusername,"password":config.loginpassword}
    r=requests.post(loginurl,json=logindata)
    return r.json()["result"]["token"]

if __name__=='__main__':
    print get_token()