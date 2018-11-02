# python3.6编译安装 （Ubuntu）

```python
Ubuntu16.0.4

apt-get -y install openssl libssl-dev bzip2 expat python-gdbm libreadline6-dev

#wget是网络下载获取的工具

apt-get -y install wget

wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz

#gcc是C语言的编译工具,我们的linux和python或者其它的文件都是由C语言构成的.所以要使用gcc作为依赖包
apt-get -y install  gcc 

#python的编译依赖

apt-get-y install zlib1g zlib1g.dev

#tgz压缩包解压 
tar -zxvf Python-3.6.4.tgz

cd  Python-3.6.4

把Python3.6安装到 /usr/local 目录

./configure --prefix=/usr/local  

make install

========================================================

cd /usr/local/bin

./python3.6
./pip3


```

