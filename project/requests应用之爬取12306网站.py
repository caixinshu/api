# coding=utf-8
import requests
import re
import json


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}
url = 'https://kyfw.12306.cn/otn/leftTicket/query'
params = {
    'leftTicketDTO.train_date': '2017-07-28',
    'leftTicketDTO.from_station': 'SZQ',
    'leftTicketDTO.to_station': 'WHN',
    'purpose_codes': 'ADULT'
    }

r = requests.get(url, params=params, headers=headers, verify=False)

rJson = r.json()

if rJson["httpstatus"] == 200:
    result = rJson["data"]["result"]
    
    m1 = re.compile(r"\|预订\|\w{12}\|(\w+)\|")
    m2 = re.compile(r"(\d{8}\|)(\S+?)(\|\w+\|\w+$)")
   
    d = dict()    
    for v in result:
        datas = []        

        # 取车次号
        plate_data = m1.search(v)
        if plate_data:
            plateNumber = plate_data.group(1)

        # 取各座位剩余数量
        seat_data = m2.search(v)
        if seat_data:
           seat_data = seat_data.group(2)
           seat_nums = seat_data.split('|')[6:]          

        # 将每趟列车的座位情况，以车次号为Key值,座位数量的数组做为value写入字典d中，
        d[plateNumber] = seat_nums

        
    for (k,v) in d.items():
        print('车次{0}:座位数量:{1}'.format(k,v))


"""
说明：还有三个数据没有分析出来位置：“ 动卧， 其它， 软座”

0
1  高级软卧  grw
2
3 软卧  rw
4       
5
6 无座  wz
7    
8 硬卧  yw
9 硬座  yz
10 二等座 tz
11 一等座 oz
12 商务座 sz
13    

"""