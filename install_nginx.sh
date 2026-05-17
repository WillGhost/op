#!/bin/bash

installdir="/opt/nginx"

# 动态获取最新 Legacy 版本
version=$(curl -s http://nginx.org/en/download.html | grep -A 10 "Legacy version" | grep -oP 'nginx-\K[0-9]+\.[0-9]+\.[0-9]+(?=\.tar\.gz)' | head -1)

# 如果获取失败，使用默认版本
if [ -z "$version" ]; then
    version=1.26.3
    echo "Warning: Failed to fetch latest legacy version, using default: $version"
else
    echo "Using Nginx legacy version: $version"
fi

version=1.30.1

#dnf -yq pcre-devel openssl-devel gcc make wget

apt install -yq gcc wget libpcre3-dev libssl-dev zlib1g-dev make

cd /tmp
wget -q  http://nginx.org/download/nginx-$version.tar.gz
tar zxf nginx-$version.tar.gz

cd nginx-$version


./configure \
--prefix=$installdir \
--with-threads \
--with-file-aio \
--with-pcre-jit \
--with-http_ssl_module \
--with-http_v2_module \
--with-http_v3_module \
--with-http_realip_module \
--with-http_stub_status_module \
--with-http_gzip_static_module \
--with-http_gunzip_module \
--with-http_sub_module \
--with-http_slice_module \
--with-http_secure_link_module \
--with-stream \
--with-stream_ssl_module \
--with-stream_ssl_preread_module \
--with-stream_realip_module \
&& make -j$(nproc) && make install 

curl -L -o /opt/nginx/conf/nginx.conf  https://cdn.jsdelivr.net/gh/WillGhost/op/nginx.conf

/opt/nginx/sbin/nginx

grep nginx /etc/rc.local || echo '/opt/nginx/sbin/nginx' >> /etc/rc.local


