#!/usr/bin/env python3
def decorate_p(func):
	def func_wrapper(name):
		return '<p>{0}</p>'.format(func(name))
	return func_wrapper

def decorate_h(nu):
	def _decorate_h(func):
		def func_wrapper(name):
			return '<h{1}>{0}</h{1}>'.format(func(name), nu)
		return func_wrapper
	return _decorate_h

def nohtml(cc):
	return cc

no_dec = decorate_p(nohtml)
no_dec2 = decorate_p(decorate_h(2)(nohtml))

print(no_dec('hehe'))
print(no_dec2('hei'))

print('Use decorator syntax...............................')

@decorate_h(3)
@decorate_p
def html(cc):
	return cc

print(html('haha'))



