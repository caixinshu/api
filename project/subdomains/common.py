# coding=utf-8

from config import *
import re
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import requests


def http_requests_get(url, allow_redirects=allow_redirects):
    try:
        result = requests.get(
            url=url,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify
        )
        return result
    except Exception,e:
        return requests.models.Response()

def http_requests_post(url, payload, allow_redirects=allow_redirects):
    try:
        result = requests.get(
            url=url,
            data=payload,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify
        )
        return result
    except Exception,e:
        return requests.models.Response()

def is_domain(domain):
    domain_regex = re.compile(
        r'(?:[A-Z0-9_](?:[A-Z0-9-]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}[A-Z0-9-]{2,}(?<!-))\z',
        re.IGNORECASE)
    return True if domain_regex.match(domain)else False
