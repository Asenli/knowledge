# python3.6编译安装

```python
1.centos7 的yum源目前支持的python版本是3.5,所以要安装3.6版本只能在官网下载

yum -y install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel

2.#wget是网络下载获取的工具

yum -y install wget

wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz

3.#gcc是C语言的编译工具,我们的linux和python或者其它的文件都是由C语言构成的.所以要使用gcc作为依赖包
yum -y install  gcc 

4.#python的编译依赖

yum -y install zlib zlib-devel 

5.#tgz压缩包解压 
tar -zxvf Python-3.6.4.tgz

cd  Python-3.6.4
yum -y install  gcc 

6.把Python3.6安装到 /usr/local 目录

./configure --prefix=/usr/local  [--with=ssl]

make install

========================================================

cd /usr/local/bin

./python3.6
./pip3




yum安装python3
sudo yum install epel-release
sudo yum install python35
```

