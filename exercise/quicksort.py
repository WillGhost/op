#!/usr/bin/env python3
import sys

inp = sys.argv[1:]
for i in range(len(inp)):
	inp[i] = int(inp[i])


def qs(xx):
	if len(xx) <= 1:
		return xx
	else:
		pivot = xx[0]
		return qs([x for x in xx[1:] if x < pivot]) +\
		[pivot] +\
		qs([x for x in xx[1:] if x > pivot])

print(inp)
print(qs(inp))





