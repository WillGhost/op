#!/bin/bash
installdir="/opt/nginx"

# 动态获取最新 Stable 版本
version=$(curl -s https://nginx.org/en/download.html | grep -A 5 "Stable version" | grep -oP 'nginx-\K[0-9]+\.[0-9]+\.[0-9]+(?=\.tar\.gz)' | head -1)

if [ -z "$version" ]; then
    version=1.30.2
    echo "Warning: Failed to fetch latest stable version, using default: $version"
else
    echo "Using Nginx stable version: $version"
fi

# 判断是否已安装
if [ -f "$installdir/sbin/nginx" ]; then
    echo "Nginx already installed, upgrading..."
    $installdir/sbin/nginx -s quit 2>/dev/null || true
    sleep 2
    UPGRADE=1
else
    echo "Fresh install..."
    UPGRADE=0
fi

apt install -yq gcc wget libpcre3-dev libssl-dev zlib1g-dev make

cd /var/tmp/
wget -q http://nginx.org/download/nginx-$version.tar.gz
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
|| { echo "Configure failed"; exit 1; }

make -j$(nproc) || { echo "Build failed"; exit 1; }

if [ "$UPGRADE" -eq 1 ]; then
    cp $installdir/sbin/nginx /var/tmp/nginx.bak
    make install
else
    make install
    curl -L -o $installdir/conf/nginx.conf https://cdn.jsdelivr.net/gh/WillGhost/op/nginx.conf
fi

$installdir/sbin/nginx -t || { echo "Config test failed, nginx not started"; exit 1; }
$installdir/sbin/nginx

grep -q nginx /etc/rc.local || echo "$installdir/sbin/nginx" >> /etc/rc.local

echo "Done. Nginx $version installed at $installdir"
$installdir/sbin/nginx -v
