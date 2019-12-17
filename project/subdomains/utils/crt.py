# coding=utf-8

from subdomains.common import http_requests_get

class Crt(object):
    def __init__(self, domain):
        self.domain = domain
        self.site = "https://crt.sh/?q=%25"
        self.result = []
    def run(self):
        url = self.site + self.domain
        try:
            r = http_requests_get(url=url)
            self.result.append(r.text)
            return self.result
        except Exception,e:
            return self.result
