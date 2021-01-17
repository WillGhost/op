#!/usr/bin/env python3

def qsort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		return qsort([x for x in arr[1:] if x < pivot]) +\
		[pivot] +\
		qsort([x for x in arr[1:] if x > pivot])


a = [32,7,9,0,3,34,-5,23,2,3]
print(a)
print(qsort(a))
