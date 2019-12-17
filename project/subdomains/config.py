# coding=utf-8

import sys
import random

# 是否开启https服务器的证书校验
allow_ssl_verify = False
# 超时时间
timeout = 10
# 是否允许url重定向
allow_redirects = True
# 是否允许http Request类的session
allow_http_session = True
# 是否允许使用随机user-agent
allow_random_useragent = False
# 是否允许随机X-forwarded-for
allow_random_x_forward = False

USER_AGENT = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
]

def random_useragent(conditon=False):
    if conditon:
        return random.choice(USER_AGENT)
    else:
        return USER_AGENT[0]

def random_x_forward_for(conditon=False):
    if conditon:
        return '%d,%d,%d,%d' % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
    else:
        return '8.8.8.8'

headers = {
    'User-Agent': random_useragent(allow_random_useragent),
    'Referer': 'https://www.baidu.com/',
    'Cookie': '',
    'X-FORWARD-FOR': random_x_forward_for(allow_random_x_forward)

}