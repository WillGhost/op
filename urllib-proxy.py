#!/usr/bin/python
import urllib2


proxy_info = {'http':'218.108.168.68:80'}
proxy_info = {'http':'125.39.66.67:80'}

proxy_support = urllib2.ProxyHandler(proxy_info)
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)


ip = urllib2.urlopen('http://api.willghost.com/ip').read()
print ip
