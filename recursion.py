#!/usr/bin/python
#coding:utf-8
import os

os.chdir('/tmp/2')

def lls():
	a = os.listdir('.')
	for i in a:
		print i
		if os.path.isdir(i):
			os.chdir(i)
			print os.getcwd()
			lls()
			os.chdir('..')



lls()






