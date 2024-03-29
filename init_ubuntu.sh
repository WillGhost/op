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


if [ ! -f "~/.vimrc" ]; then
    echo "set vimrc"
    curl -s -o /tmp/vimrc https://cdn.jsdelivr.net/gh/WillGhost/op/vimrc && \
    grep -n =========== /tmp/vimrc |awk -F: '{print $1}' |xargs -I {} sed -n '{},1000p' /tmp/vimrc > ~/.vimrc && \
    rm -f /tmp/vimrc
fi


grep history-search-backward ~/.bashrc || ( cp  ~/.bashrc  ~/.bashrc_$(date +%Y%m%d%H%M%S) && curl -s -o ~/.bashrc https://cdn.jsdelivr.net/gh/WillGhost/op/bashrc )

ls /etc/iptables.sh || curl -L -o /etc/iptables.sh  https://cdn.jsdelivr.net/gh/WillGhost/op/iptables.sh


#mkdir /root/.pip/ && echo '[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple' > ~/.pip/pip.conf
#pip3 install ipython && \

ls /etc/rc.local || echo '#!/usr/bin/bash' > /etc/rc.local
chmod +x /etc/rc.local
systemctl enable rc-local

curl -L -o /usr/local/sbin/nexttrace https://github.com/sjlleo/nexttrace/releases/download/v1.2.9/nexttrace_linux_amd64
chmod +x /usr/local/sbin/nexttrace 

# apt-get install tcptraceroute
# wget http://www.vdberg.org/~richard/tcpping


#RUN wget -q https://gomirrors.org/dl/go/go1.16.3.linux-amd64.tar.gz && \
#  rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz && \
#  rm -f go1.16.3.linux-amd64.tar.gz
#ENV PATH=$PATH:/usr/local/go/bin

groupadd -g 2000 hehe && useradd -m -g 2000 -u 2000 hehe -s /bin/bash && cp /root/.bashrc /home/hehe/.bashrc && cp /root/.vimrc /home/hehe/.vimrc && chown -R hehe /home/hehe/

grep '^ClientAliveInterval' /etc/ssh/sshd_config || sed -i 's/#ClientAliveInterval 0/ClientAliveInterval 120/' /etc/ssh/sshd_config


grep "* soft nofile  1000000" /etc/security/limits.conf || echo "
* soft nofile  1000000
* hard nofile  1000000
* soft nproc   1000000
* hard nproc   1000000
* soft core    1000000
* hard core    1000000
* hard memlock unlimited
* soft memlock unlimited

root soft nofile  1000000
root hard nofile  1000000
root soft nproc   1000000
root hard nproc   1000000
root soft core    1000000
root hard core    1000000
root hard memlock unlimited
root soft memlock unlimited
" > /etc/security/limits.conf


sed -i '/net.ipv4.tcp_rmem/d' /etc/sysctl.conf
sed -i '/net.ipv4.tcp_wmem/d' /etc/sysctl.conf
sed -i '/net.core.rmem_max/d' /etc/sysctl.conf
sed -i '/net.core.wmem_max/d' /etc/sysctl.conf
sed -i '/net.ipv4.udp_rmem_min/d' /etc/sysctl.conf
sed -i '/net.ipv4.udp_wmem_min/d' /etc/sysctl.conf

cat >> /etc/sysctl.conf << EOF
net.core.rmem_max=8519680
net.core.wmem_max=8519680
net.ipv4.tcp_rmem=4096 131072 16777216
net.ipv4.tcp_wmem=4096 16384 16777216
net.ipv4.udp_rmem_min=8192
net.ipv4.udp_wmem_min=8192
EOF

grep bbr /etc/sysctl.conf || echo 'net.core.default_qdisc=fq'  >> /etc/sysctl.conf
grep tcp_congestion_control  /etc/sysctl.conf || echo 'net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.conf
sysctl -p

ls ~/.ssh/ || (mkdir ~/.ssh && chmod 700 ~/.ssh)



