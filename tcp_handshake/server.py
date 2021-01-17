#!/opt/python34/bin/python3
import time
import socket


sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('0.0.0.0',8000))
sk.listen(10)
#sk.setblocking(0)


count = 0
def repo():
	global count
	reponse = '''HTTP/1.1 200 OK\nServer: Python socket server\n\n<h1>Hello world %d</h1>'''%count
	count += 1
	#time.sleep(3)
	return reponse.encode('utf-8')

while 1:
	client,addr = sk.accept()
	data = client.recv(1024)
	print('======= Receive data\t%d\n%s'%(count,data.decode('utf-8')))
	client.send(repo())
	#client.send(b'heheeeeeeeeeeee')
	time.sleep(1)
	client.close()
	print('======= Client address port\t%d\n%s'%(count,str(addr)))




