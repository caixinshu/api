# coding=utf-8

import requests
from Queue import Queue
import sys
import threading
from agent_proxy import user_agent_list

class DirScan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
            try:
                r = requests.get(url=url,headers=user_agent_list.get_user_agent(),timeout=8)
                if r.status_code == 200:
                    print '[*]'+url
            except Exception,e:
                pass

def start(url,ext,count):
    queue = Queue()