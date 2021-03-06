#!/bin/bash

installdir="/opt/nginx"
version=1.16.1

dnf -yq pcre-devel openssl-devel gcc make wget

cd /tmp
wget -q  http://nginx.org/download/nginx-$version.tar.gz
tar zxf nginx-$version.tar.gz

cd nginx-$version

./configure \
--prefix=$installdir \
--with-http_ssl_module \
--with-http_stub_status_module \
--with-http_realip_module \
--with-http_gzip_static_module \
--with-http_v2_module > /dev/null \
&& make > /dev/null && make install > /dev/null


/opt/nginx/sbin/nginx

grep nginx /etc/rc.local || echo '/opt/nginx/sbin/nginx' >> /etc/rc.local


