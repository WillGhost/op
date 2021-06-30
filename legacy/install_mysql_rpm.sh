#!/bin/bash


datadir="/zz_Data/mysql"
downversion="mysql-5.6.26"


if [ -f /etc/my.cnf ];then
        echo "Please remove file /etc/my.cnf"
        exit 1
fi


yum -y install perl-Data-Dumper wget

cd /tmp

wget http://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-5.6.26-1.el7.x86_64.rpm-bundle.tar
tar xvf MySQL-5.6.26-1.el7.x86_64.rpm-bundle.tar

rpm -ivh MySQL-client-5.6.26-1.el7.x86_64.rpm
rpm -ivh MySQL-devel-5.6.26-1.el7.x86_64.rpm
rpm -ivh MySQL-shared-5.6.26-1.el7.x86_64.rpm
rpm -e mariadb-libs
rpm -ivh MySQL-server-5.6.26-1.el7.x86_64.rpm


cd /etc/ && wget https://raw.githubusercontent.com/WillGhost/op/master/my.cnf
rm -fr /var/lib/mysql
mkdir $datadir
chown -R mysql:mysql $datadir
mysql_install_db --datadir /zz_Data/mysql  --user mysql


/etc/init.d/mysql restart

echo "my.cnf is in /etc/my.cnf"
echo "Run /etc/init.d/mysql restart"


