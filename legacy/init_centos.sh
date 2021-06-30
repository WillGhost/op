#!/bin/bash

dnf update -yq
dnf install -yq tree vim lrzsz gcc gcc-c++ make bind-utils zip unzip wget curl openssl-devel git telnet sysstat tar
dnf install -yq nmap
dnf install -yq python3



chmod +x /etc/rc.local

echo "
set expandtab
set ts=4
set shiftwidth=4
set ignorecase
command WQ wq
command Wq wq
command Vs vs
command W w
command Q q
" >  ~/.vimrc


