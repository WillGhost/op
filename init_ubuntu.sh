#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

#sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

apt update
#apt upgrade
#apt install -y tzdata
ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone


apt install -y lrzsz tree vim dnsutils zip unzip wget curl telnet sysstat tar less screen tmux jq iptables
# iputils-ping iproute2 git
#apt install -y  python3 python3-dev python3-pip mysql-client libmysqlclient-dev 

curl -s -o /tmp/vimrc https://cdn.jsdelivr.net/gh/WillGhost/op/vimrc && \
  grep -n =========== /tmp/vimrc |awk -F: '{print $1}' |xargs -I {} sed -n '{},1000p' /tmp/vimrc > ~/.vimrc && \
  rm -f /tmp/vimrc

#curl -s -o /tmp/bashrc https://cdn.jsdelivr.net/gh/WillGhost/op/bashrc && \
#  cat ~/.bashrc |grep history-search-backward || cat /tmp/bashrc >> ~/.bashrc
cp  ~/.bashrc  ~/.bashrc_$(date +%Y%m%d%H%M%S)
curl -s -o ~/.bashrc https://cdn.jsdelivr.net/gh/WillGhost/op/bashrc

ls /etc/iptables.sh || curl -L -o /etc/iptables.sh  https://cdn.jsdelivr.net/gh/WillGhost/op/iptables.sh


#mkdir /root/.pip/ && echo '[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple' > ~/.pip/pip.conf
#pip3 install ipython && \

ls /etc/rc.local || echo '#!/usr/bin/bash' > /etc/rc.local
chmod +x /etc/rc.local
systemctl enable rc-local

curl -L -o /usr/local/sbin/nexttrace https://github.com/sjlleo/nexttrace/releases/download/v1.1.2/nexttrace_linux_amd64
chmod +x /usr/local/sbin/nexttrace 

#RUN wget -q https://gomirrors.org/dl/go/go1.16.3.linux-amd64.tar.gz && \
#  rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz && \
#  rm -f go1.16.3.linux-amd64.tar.gz
#ENV PATH=$PATH:/usr/local/go/bin

grep bbr /etc/sysctl.conf || echo 'net.core.default_qdisc=fq'  >> /etc/sysctl.conf
grep tcp_congestion_control  /etc/sysctl.conf || echo 'net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.conf
sysctl -p

sed -i 's/#ClientAliveInterval 0/ClientAliveInterval 30/' /etc/ssh/sshd_config


exit 0

echo "vm.swappiness = 10
fs.file-max = 1000000
fs.inotify.max_user_instances = 8192
fs.pipe-max-size = 1048576
fs.pipe-user-pages-hard = 0
fs.pipe-user-pages-soft = 0
net.ipv4.conf.all.rp_filter = 0
net.ipv4.conf.default.rp_filter = 0

# socket status
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_tw_timeout = 10
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.tcp_keepalive_probes = 3
net.ipv4.tcp_keepalive_intvl = 15
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_max_tw_buckets = 3000
net.ipv4.route.gc_timeout = 100
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_synack_retries = 2

# tcp window
net.core.wmem_default = 262144
net.core.wmem_max = 67108864
net.core.somaxconn = 3276800
net.core.optmem_max = 81920
net.core.rmem_default = 262144
net.core.rmem_max = 67108864
net.core.netdev_max_backlog = 400000
net.core.netdev_budget = 600
net.ipv4.tcp_max_orphans = 3276800

# forward
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1

# ipv4
net.ipv4.tcp_no_metrics_save=1
net.ipv4.tcp_ecn=0
net.ipv4.tcp_frto=0
net.ipv4.tcp_mtu_probing=0
net.ipv4.tcp_rfc1337=0
net.ipv4.tcp_sack=1
net.ipv4.tcp_fack=1
net.ipv4.tcp_window_scaling=1
net.ipv4.tcp_adv_win_scale=1
net.ipv4.tcp_moderate_rcvbuf=1
net.ipv4.tcp_mem = 786432 2097152 3145728 
net.ipv4.tcp_rmem = 4096 524288 67108864
net.ipv4.tcp_wmem = 4096 524288 67108864
net.ipv4.udp_rmem_min=8192
net.ipv4.udp_wmem_min=8192
net.core.default_qdisc=fq
net.ipv4.tcp_congestion_control=bbr

# netfiliter iptables
net.netfilter.nf_conntrack_tcp_timeout_fin_wait = 30
net.netfilter.nf_conntrack_tcp_timeout_time_wait = 30
net.netfilter.nf_conntrack_tcp_timeout_close_wait = 15
net.netfilter.nf_conntrack_tcp_timeout_established = 350
net.netfilter.nf_conntrack_max = 25000000
net.netfilter.nf_conntrack_buckets = 25000000" >/etc/sysctl.d/98-optimize.conf
echo -e "${Font_Green}已开启BBR和系统调优, 配置文件 /etc/sysctl.d/98-optimize.conf${Font_Suffix}"

echo "* soft nofile 1048576
* hard nofile 1048576
* soft nproc 1048576
* hard nproc 1048576
* soft core 1048576
* hard core 1048576
* hard memlock unlimited
* soft memlock unlimited" > /etc/security/limits.conf
echo -e "${Font_Green}已解除系统ulimit限制, 配置文件 /etc/security/limits.conf${Font_Suffix}"


