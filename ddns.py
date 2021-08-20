#!/usr/bin/env python
import requests

# https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records

key = 'sUZHID'
zone = '4653b6b34'
name = '6pi.xxxxxx.com'


url = "https://api.cloudflare.com/client/v4"

headers = {
    "Authorization": "Bearer " + key,
}


uri = f'{url}/zones/{zone}/dns_records'
dd = {
    'name': name,
    'type': 'AAAA',
}

r = requests.get(uri, headers=headers, params=dd)
print(r.json())


gg = r.json()
identifier = gg['result'][0]['id']
old =  gg['result'][0]['content']

myip = requests.get('http://v6.ipv6-test.com/api/myip.php').text
print('--------myip', myip)

if old != myip:
    uri = f'{url}/zones/{zone}/dns_records/{identifier}'
    dd = {
        'type': 'AAAA',
        'content': myip,
        'name': name,
    }
    r = requests.put(uri, headers=headers, json=dd)
    print(r.json())





#curl -X GET "https://api.cloudflare.com/client/v4/zones/023e105f4ecef8ad9ca31a8372d0c353/dns_records?type=A&name=example.com&content=127.0.0.1&proxied=undefined&page=1&per_page=20&order=type&direction=desc&match=all" \
#     -H "X-Auth-Email: user@example.com" \
#     -H "X-Auth-Key: c2547eb745079dac9320b638f5e225cf483cc5cfdda41" \
#     -H "Content-Type: application/json"

#curl -X PUT "https://api.cloudflare.com/client/v4/zones/023e105f4ecef8ad9ca31a8372d0c353/dns_records/372e67954025e0ba6aaa6d586b9e0b59" \
#     -H "X-Auth-Email: user@example.com" \
#     -H "X-Auth-Key: c2547eb745079dac9320b638f5e225cf483cc5cfdda41" \
#     -H "Content-Type: application/json" \
#     --data '{"type":"A","name":"example.com","content":"127.0.0.1","ttl":120,"proxied":false}'
