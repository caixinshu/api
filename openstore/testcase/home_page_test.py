#!/usr/bin/env python
# -*- coding=utf-8 -*-

def retry(func):
    def warp():
        for i in range(3):
            try:
                func()
            except:
                pass
    return warp

@retry
def test_login():
    print('test')
    error = 1/0

# test_login()

