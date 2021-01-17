#!/bin/bash

port=3306
masterdir="/opt/mysql"
downversion="mysql-5.6.26"

installdir="$masterdir"
#installdir="${masterdir}_$port"
datadir="$installdir/data"

if [ -f /etc/my.cnf ];then
        echo "Please remove file /etc/my.cnf"
        exit 1
fi

grep mysql /etc/passwd || groupadd -g 27 mysql
grep mysql /etc/passwd || useradd -M -s /sbin/nologin -u 27 -g 27 mysql

yum install -y -q cmake make ncurses-devel gcc-c++ wget perl
wget -q http://cdn.mysql.com/Downloads/MySQL-5.6/$downversion.tar.gz
tar zxf $downversion.tar.gz
cd $downversion

cmake \
-DCMAKE_INSTALL_PREFIX=$installdir \
-DMYSQL_DATADIR=$datadir \
-DMYSQL_UNIX_ADDR=$datadir/mysql.sock \
-DSYSCONFDIR=$installdir/my.cnf \
&& make -j 4 && make install

if [ $? -ne 0 ];then
        echo "cmake, make, make install, ERROR"
        exit 1
fi

cd $installdir/scripts/
./mysql_install_db  --user=mysql --basedir=$installdir --datadir=$datadir

if [ $? -ne 0 ];then
        exit 1
        echo "mysql_install_db ERROR"
fi

echo
echo
echo
echo "Show more options in  http://dev.mysql.com/doc/refman/5.6/en/source-configuration-options.html"
echo "my.cnf is in $installdir/my.cnf"
echo "Run $installdir/support-files/mysql.server restart"
