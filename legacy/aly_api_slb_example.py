#!/usr/bin/env python
#coding:utf-8
import requests
import datetime
import hashlib
import base64
import hmac
import json
import urllib


AccessKey = 'vjfwefVwefwmse'
AccessSecret = '0VwJrwefo7DnergerwepH3l'
URL = 'https://slb.aliyuncs.com'


def percent_encode(res):
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return urllib.quote(res)

def sign(pars):
    k = pars.keys()
    k.sort()
    rr = '&'.join(['%s=%s'%(_, percent_encode(pars[_])) for _ in k])
    rr = 'GET&%2F&' + percent_encode(rr)
    h = hmac.new(AccessSecret + "&", rr, hashlib.sha1)
    return base64.encodestring(h.digest()).strip()


def action(pars_do):
    utc = datetime.datetime.utcnow()
    utc = utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    pars = {
        'Format': 'JSON',
        'Version': '2014-05-15',
        'AccessKeyId': AccessKey,
        'SignatureMethod': 'HMAC-SHA1',
        'SignatureVersion': '1.0',
        'SignatureNonce': utc,
        'Timestamp': utc,
    }
    pars.update(pars_do)
    pars['Signature'] = sign(pars)
    rep = requests.get(URL, params=pars,)
    print rep.url
    rep = json.loads(rep.text)
    print json.dumps(rep, indent=4)

def main():
    hehe = {'Action': 'DescribeLoadBalancers', 'RegionId': 'cn-beijing'}
    action(hehe)


if __name__ == '__main__':
    main()


