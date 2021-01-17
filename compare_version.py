#!/usr/bin/python

a = '3.6.70.4.85.1'
b = '3.6.700.4.85.10'

def diff(a,b):
	if a == b:
		print a,'=',b
		return

	sa,sb = a.split('.'),b.split('.')

	if len(sa) < len(sb):
		minc = len(sa)
	else:
		minc = len(sb)

	for i in range(minc):
		ia,ib = int(sa[i]),int(sb[i])
		if ia < ib:
			print b+'\tnewer\t'+a
			return
		elif ia > ib:
			print a+'\tnewer\t'+b
			return
		elif ia == ib and i == minc-1:
			if minc == len(sa):
				print b+'\tnewer\t'+a
			else:
				print a+'\tnewer\t'+b

diff(a,b)




