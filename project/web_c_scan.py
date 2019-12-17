# coding=utf-8

from Queue import Queue
import requests
import time
import threading
import sys
from IPy import IP

Headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

class DirScan(threading.Thread):
	"""docstring for DirScan"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():			
			url = self._queue.get()
			try:
				print url
			except:
				pass
			# try:
			# 	r = requests.get(url=url,timeout=6,headers=Headers)
			# 	if r.status_code == 200:
			# 		print "[*] Web service Found %s" %url
			# except Exception, e:
			# 	pass

def create(ips):
	queue = Queue()
	ip = IP(ips,make_net=True)
	ports = ['80','8080','3443']

	for i in ip:
		for j in ports:
			queue.put('http://'+str(i)+':'+str(j))
	return queue

def main(ips):
	queue = create(ips)
	threads = []

	thread_counts = 100
	for i in range(thread_counts):
		threads.append(DirScan(queue))

	for t in threads:
		t.start()
	for t in threads:
		t.join()
if __name__ == '__main__':
	if len(sys.argv) == 2:
		start = time.time()
		main(sys.argv[1])
		print time.time().start
		sys.argv(0)
	else:
		print 'Usage:%s 192.168.1.1/24'%(sys.argv[0])
		sys.exit(-1)




