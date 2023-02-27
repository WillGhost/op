#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

#sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

apt update 
apt install -y tzdata
ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone


apt install -y lrzsz tree vim dnsutils zip unzip wget curl git telnet sysstat tar less iputils-ping iproute2 screen tmux jq
#apt install -y  python3 python3-dev python3-pip mysql-client libmysqlclient-dev 

curl -s -o /tmp/vimrc https://cdn.jsdelivr.net/gh/WillGhost/op/vimrc && \
  grep -n =========== /tmp/vimrc |awk -F: '{print $1}' |xargs -I {} sed -n '{},1000p' /tmp/vimrc > ~/.vimrc && \
  rm -f /tmp/vimrc

curl -s -o /tmp/bashrc https://cdn.jsdelivr.net/gh/WillGhost/op/bashrc && \
  cat ~/.bashrc |grep history-search-backward || cat /tmp/bashrc >> ~/.bashrc


mkdir /root/.pip/ && echo '[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple' > ~/.pip/pip.conf
#pip3 install ipython && \

ls /etc/rc.local || touch /etc/rc.local
chmod +x /etc/rc.local
systemctl enable rc-local

curl -L -o /usr/local/sbin/nexttrace https://github.com/sjlleo/nexttrace/releases/download/v1.1.2/nexttrace_linux_amd64
chmod +x /usr/local/sbin/nexttrace 

#RUN wget -q https://gomirrors.org/dl/go/go1.16.3.linux-amd64.tar.gz && \
#  rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz && \
#  rm -f go1.16.3.linux-amd64.tar.gz
#ENV PATH=$PATH:/usr/local/go/bin
