#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export TZ=Asia/Shanghai

sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list \
  && apt update \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
  && apt install -y tzdata


apt install -y lrzsz tree vim dnsutils zip unzip wget curl git telnet sysstat tar less iputils-ping iproute2 \
  python3 python3-dev python3-pip

curl -s -o /tmp/vimrc https://cdn.jsdelivr.net/gh/WillGhost/op@master/vimrc && \
  grep -n =========== /tmp/vimrc |awk -F: '{print $1}' |xargs -I {} sed -n '{},1000p' /tmp/vimrc > ~/.vimrc && \
  rm -f /tmp/vimrc

curl -s https://cdn.jsdelivr.net/gh/WillGhost/op@master/bashrc >> ~/.bashrc

#RUN wget -q https://gomirrors.org/dl/go/go1.16.3.linux-amd64.tar.gz && \
#  rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz && \
#  rm -f go1.16.3.linux-amd64.tar.gz
#ENV PATH=$PATH:/usr/local/go/bin

mkdir /root/.pip/ && echo '[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple' > ~/.pip/pip.conf
#pip3 install ipython && \


touch /etc/rc.local
chmod +x /etc/rc.local
systemctl enable rc-local
