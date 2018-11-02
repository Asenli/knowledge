**编译安装pureFTP**

## 安装openssl支持

关闭防火墙

service iptables stop
setenforce 0

FTP的默认端口是21

```shell
#安装开源协议系统(开源安全证书)
wget -c https://www.openssl.org/source/openssl-1.1.0c.tar.gz
tar -zxvf openssl-1.1.0c.tar.gz
cd openssl-1.1.0c
./config --prefix=/usr/local/openssl
make && make install
```

## 安装pureftp

```shell
#下载pureftpd，解压，然后进入该目录

./configure 

--prefix=/usr/local/pureftpd \

--without-inetd \  #不支持超级服务器

--with-altlog \  #支持选择日志格式(类似Apache)  

--with-puredb \  #支持虚拟用户 (FTP登陆用户而非系统用户)

--with-throttling \  #支持带宽控制

--with-tls=/usr/local/openssl  #启用 SSL/TLS 支持 

#上面是解释，复制下面这一行执行
./configure --prefix=/usr/local/pureftpd --without-inetd --with-altlog --with-puredb --with-throttling --with-tls=/usr/local/openssl

make && make install	#编译并且安装
```

1. 复制配置文件

```shell
cd configuration-file	#进入目录

mkdir -p /usr/local/pureftpd/etc/	#创建配置文件目录

cp pure-ftpd.conf /usr/local/pureftpd/etc/pure-ftpd.conf #把配置文件复制到软件安装目录的配置文件目录下

cp pure-config.pl /usr/local/pureftpd/sbin/pure-config.pl	#复制启动程序

chmod 755 /usr/local/pureftpd/sbin/pure-config.pl	#修改启动程序的权限
```

6 . 修改 /usr/local/pureftpd/etc/pure-ftpd.conf 配置项

```ini
	ChrootEveryone              yes  #限定在自己的家目录
	BrokenClientsCompatibility  no
	MaxClientsNumber            50   #最大连接数目
	Daemonize                   yes
	MaxClientsPerIP             8     #每个IP最大连接数目
	VerboseLog                  no
	DisplayDotFiles             yes
	AnonymousOnly               no
	NoAnonymous                 no     #不允许匿名登录
	SyslogFacility              ftp
	DontResolve                 yes
	MaxIdleTime                 15
	PureDB                        /usr/local/pureftpd/etc/pureftpd.pdb
	LimitRecursion              3136 8
	AnonymousCanCreateDirs      no
	MaxLoad                     4
	AntiWarez                   yes
	Umask                       133:022
	MinUID                      100
	AllowUserFXP                no
	AllowAnonymousFXP           no
	ProhibitDotFilesWrite       no
	ProhibitDotFilesRead        no
	AutoRename                  no
	AnonymousCantUpload         no
	PIDFile                     /usr/local/pureftpd/var/run/pure-ftpd.pid
	MaxDiskUsage               99
	CustomerProof              yes
```

1. 启动

   ```shell
   service pureftpd start | stop  | restart
   ```


1. 添加帐号

   ```shell
   useradd test
   mkdir -p /var/www/html/
   chown -R test:test /var/www/html/
   #指定这个用户可以使用FTP hensha是昵称
   #把刚才添加的test用户生成为FTP用户
   /usr/local/pureftpd/bin/pure-pw useradd hensha -utest -d /var/www/html/
   ```


10.   常用操作


```shell
 #生成数据库
 /usr/local/pureftpd/bin/pure-pw mkdb
 #查看用户组
 /usr/local/pureftpd/bin/pure-pw list
 /usr/local/pureftpd/bin/pu re-pw userdel 用户
```



