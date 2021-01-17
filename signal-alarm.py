#!/usr/bin/python
import signal, time

def handler(signum,frame):
	print signum,frame
	#raise RuntimeError('Run timeout...')
	raise Exception('Run timeout...')

def foo():
	print '111'
	time.sleep(7)
	print '222'
	time.sleep(3)

signal.signal(signal.SIGALRM, handler)

signal.alarm(5)

try:
	foo()
except Exception,e:
	print e

#signal.alarm(0)
print '333'
