iptables -F
iptables -I INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -p icmp -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
iptables -A INPUT -p tcp --dport 8900 -j ACCEPT
iptables -A INPUT -p tcp --dport 3724 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -s 172.24.5.0/24  -j ACCEPT
iptables -A INPUT -j REJECT --reject-with icmp-host-prohibited



ip6tables -F INPUT
ip6tables -I INPUT -i lo -j ACCEPT
ip6tables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
ip6tables -A INPUT -p ipv6-icmp -j ACCEPT
ip6tables -A INPUT -p tcp --dport 80 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 443 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 8000 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 8900 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 3724 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT
ip6tables -A INPUT -j REJECT

