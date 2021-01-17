#!/usr/bin/env python3
import sys

inp = sys.argv[1:]
for i in range(len(inp)):
	inp[i] = int(inp[i])


def bubble(xx):
	length = len(xx)
	for i in range(length-1):
		for j in range(length-1-i):
			if xx[j] > xx[j+1]:
				xx[j],xx[j+1] = xx[j+1],xx[j]
	return xx

print(inp)
print(bubble(inp))





