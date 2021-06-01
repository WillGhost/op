FROM ubuntu:20.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV TZ=Asia/Shanghai

RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list \
  && apt update \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
  && apt install tzdata


RUN apt install -y lrzsz tree vim dnsutils zip unzip wget curl git telnet sysstat tar less ping \
  mysql-client libmysqlclient-dev reids \
  librdkafka-dev \
  python3 python3-dev python3-pip

RUN curl -s https://cdn.jsdelivr.net/gh/WillGhost/op@master/vimrc > /tmp/vimrc && \
  grep -n =========== /tmp/vimrc |awk -F: '{print $1}' |xargs -I {} sed -n '{},1000p' /tmp/vimrc > ~/.vimrc && \
  rm -f /tmp/vimrc

RUN curl -s https://cdn.jsdelivr.net/gh/WillGhost/op@master/bashrc >> ~/.bashrc

RUN wget -q https://gomirrors.org/dl/go/go1.16.3.linux-amd64.tar.gz && \
  rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz && \
  rm -f go1.16.3.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin

RUN mkdir /root/.pip/ && echo '[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple' > ~/.pip/pip.conf
RUN pip3 install requests && \
  pip3 install mysqlclient && \
  pip3 install sqlalchemy && \
  pip3 install elasticsearch && \
  pip3 install numpy && \
  pip3 install matplotlib && \
  pip3 install kafka-python

RUN apt install -y default-jre && \
  wget -q https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/2.7.0/kafka_2.12-2.7.0.tgz && \
  tar zxf kafka_2.12-2.7.0.tgz && \
  mv kafka_2.12-2.7.0 /opt/kafka && \
  rm -f kafka_2.12-2.7.0.tgz

