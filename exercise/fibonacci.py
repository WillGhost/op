#!/usr/bin/env python3
import sys

max = int(sys.argv[1])

def fibonacci(max):
	a,b = 0,1
	while a <= max:
		print(a,end=' ')
		a,b = b,a+b
	print()

fibonacci(max)

