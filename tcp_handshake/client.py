#!/usr/bin/env python3
import socket
import time

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'hk.willghost.com'
port = 8000

sk.connect((host,port))
sk.sendall(b'GET / HTTP/1.1')
rep = sk.recv(1024)
print(rep)
time.sleep(10)
#sk.close()

