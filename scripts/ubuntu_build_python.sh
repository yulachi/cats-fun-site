#!/bin/bash
sudo apt-get install gdebi-core
sudo apt-get build-dep python
sudo apt-get install libffi-dev libgdbm-dev libsqlite3-dev libssl-dev zlib1g-dev

export PYTHON_VERSION=3.10.0
export PYTHON_MAJOR=3.10

curl https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz --output Python-${PYTHON_VERSION}.tgz
tar xvf Python-${PYTHON_VERSION}.tgz
rm Python-${PYTHON_VERSION}.tgz
cd Python-${PYTHON_VERSION} || exit

./configure \
    --prefix=/opt/python/${PYTHON_VERSION} \
    --enable-loadable-sqlite-extensions \
    --enable-shared \
    --enable-optimizations \
    --enable-ipv6 \
    LDFLAGS=-Wl,-rpath=/opt/python/${PYTHON_VERSION}/lib,--disable-new-dtags

make
sudo make altinstall

curl -O https://bootstrap.pypa.io/get-pip.py
sudo /opt/python/${PYTHON_VERSION}/bin/python${PYTHON_MAJOR} get-pip.py
