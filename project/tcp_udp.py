# coding:utf-8

import socket

def tcp_socket():
	'''
	tcp客户端
	'''
	target_host = "www.baidu.com"
	target_port = 80

	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((target_host,target_port))
	client.send("GET /HTTP/1.1\r\nHost:baidu.com\r\n\r\n")
	response = client.recv(4096)
	# print response
	return response

def udp_socket():
	'''
	udp客户端
	'''
	target_host = "127.0.01"
	target_port = 80

	client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	client.sendto('AAAABBBBBCCCC',(target_host,target_port))
	data,addr = client.recvfrom(4096)
	# print data
	return data



