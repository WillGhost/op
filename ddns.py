#!/usr/bin/env python3
import socket
import requests

# https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records

key = 'sUZF4G2B87YHID'
zone = '46d2353b6b34'
name = '6v.w3r32.com'

url = "https://api.cloudflare.com/client/v4"


myipv6url = 'http://v6.ipv6-test.com/api/myip.php'
#myipv6url = 'https://6.ipw.cn'

headers = {
    "Authorization": "Bearer " + key,
}

def get_myipv6():
    ipv6_address = ''
    try:
        ipv6_addresses = socket.getaddrinfo(name, None, socket.AF_INET6)
        for addr_info in ipv6_addresses:
           ipv6_address = addr_info[4][0]
    except socket.gaierror:
        print("Could not resolve the domain namexxxxxxx")
    return ipv6_address


def get_from_dns():
    uri = f'{url}/zones/{zone}/dns_records'
    dd = {
        'name': name,
        'type': 'AAAA',
    }
    r = requests.get(uri, headers=headers, params=dd)
    gg = r.json()
    identifier = gg['result'][0]['id']
    old =  gg['result'][0]['content']
    return old, identifier

def get_current():
    myip = requests.get(myipv6url, timeout=4).text
    return myip

def flush_dns(new_ip, identifier):
    uri = f'{url}/zones/{zone}/dns_records/{identifier}'
    dd = {
        'type': 'AAAA',
        'content': new_ip,
        'name': name,
    }
    r = requests.put(uri, headers=headers, json=dd)
    print(r.json())

def main():
    myipv6, identifier = get_from_dns()
    current_ip = get_current()
    if myipv6 != current_ip:
        flush_dns(current_ip, identifier)


if __name__ == '__main__':
    main()



#curl -X GET "https://api.cloudflare.com/client/v4/zones/023e105f4ecef8ad9ca31a8372d0c353/dns_records?type=A&name=example.com&content=127.0.0.1&proxied=undefined&page=1&per_page=20&order=type&direction=desc&match=all" \
#     -H "X-Auth-Email: user@example.com" \
#     -H "X-Auth-Key: c2547eb745079dac9320b638f5e225cf483cc5cfdda41" \
#     -H "Content-Type: application/json"

#curl -X PUT "https://api.cloudflare.com/client/v4/zones/023e105f4ecef8ad9ca31a8372d0c353/dns_records/372e67954025e0ba6aaa6d586b9e0b59" \
#     -H "X-Auth-Email: user@example.com" \
#     -H "X-Auth-Key: c2547eb745079dac9320b638f5e225cf483cc5cfdda41" \
#     -H "Content-Type: application/json" \
#     --data '{"type":"A","name":"example.com","content":"127.0.0.1","ttl":120,"proxied":false}'
