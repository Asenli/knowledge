# samba

## 简介

samba主要运用与windows电脑与linux主机之间进行文件共享

## 软硬件环境

linux 主机s1一台，关闭selinux和防火墙，192.168.199.236

windows主机 c1一台，192.168.199.2

搭建之前：关闭防火墙和selinux
	service iptables stop
	setenforce 0

## 操作步骤

1. 在s1上面安装samba服务

   ```shell
   yum install -y samba samba-client	#安装samba服务端与客户端
   ```

2. 编辑samba的配置文件，/etc/samba/smb.conf

   ```ini
   [global]					#全局的配置
           workgroup = MYGROUP	#window里面的工作组，默认是WORKGROUP
           server string = Samba Server Version %v
           security = user
           passdb backend = tdbsam
           load printers = yes
           cups options = raw
   [homes]	#模块的配置
           comment = Home Directories
           browseable = no
           writable = yes
   [printers]	#模块的配置
           comment = All Printers
           path = /var/spool/samba
           browseable = no
           guest ok = no
           writable = no
           printable = yes
   ```

   [global] 定义全局的配置，workgroup用来定义工作组，相信如果你安装过windows的系统，你会对这个workgroup不陌生。一般情况下，需要我们把这里的MYGROUP改成WORKGROUP（windows默认的工作组名字）。

   security = user #这里指定samba的安全等级。关于安全等级有四种：

   share：用户不需要账户及密码即可登录samba服务器

   user：由提供服务的samba服务器负责检查账户及密码（默认）

   server：检查账户及密码的工作由另一台windows或samba服务器负责

   domain：指定windows域控制服务器来验证用户的账户及密码。

   passdb backend = tdbsam # passdb backend（用户后台），samba有三种用户后台：smbpasswd, tdbsam和ldapsam.

   smbpasswd：该方式是使用smb工具smbpasswd给系统用户（真实用户或者虚拟用户）设置一个Samba密码，客户端就用此密码访问Samba资源。smbpasswd在/etc/samba中，有时需要手工创建该文件。

   tdbsam：使用数据库文件创建用户数据库。数据库文件叫passdb.tdb，在/etc/samba中。passdb.tdb用户数据库可使用 `smbpasswd -a` 创建Samba用户，要创建的Samba用户必须先是系统用户。也可使用pdbedit创建Samba账户。pdbedit参数很多，列出几个主要的：

   pdbedit -a username：新建Samba账户。

   pdbedit -x username：删除Samba账户。

   pdbedit -L：列出Samba用户列表，读取passdb.tdb数据库文件。

   pdbedit -Lv：列出Samba用户列表详细信息。

   pdbedit -c “[D]” -u username：暂停该Samba用户账号。

   pdbedit -c “[]” -u username：恢复该Samba用户账号。

   ldapsam：基于LDAP账户管理方式验证用户。首先要建立LDAP服务，设置 “passdb backend = ldapsam:ldap://LDAP Server”

   load printers 和 cups options 两个参数用来设置打印机相关。

   除了这些参数外，还有几个参数需要你了解：

   netbios name = MYSERVER # 设置出现在网上邻居中的主机名

   hosts allow = 127. 192.168.12. 192.168.13. # 用来设置允许的主机，如果在前面加 ”;” 则表示允许所有主机

   log file = /var/log/samba/%m.log #定义samba的日志，这里的%m是上面的netbios name

   max log size = 50 # 指定日志的最大容量，单位是K

   [homes] 该部分内容共享用户自己的家目录，也就是说，当用户登录到samba服务器上时实际上是进入到了该用户的家目录，用户登陆后，共享名不是homes而是用户自己的标识符，对于单纯的文件共享的环境来说，这部分可以注视掉。

   [printers] 该部分内容设置打印机共享。

## samba实践

1. **共享一个目录，任何人都可以访问，即不用输入密码即可访问，要求只读**

   修改全局的设置
   vim /etc/samba/smb.conf


```ini
  [global]
  WORKGROUP = WORKGROUP
  security = share
```

   然后在配置文件的末尾添加一行

```ini
   [share]#文件夹的名字
           comment = share all
           path = /var/www/html
           browseable = yes
           public = yes
           writable = no
```

   启动samba共享服务

```shell
   /etc/init.d/smb start
   
   service smb start
   
   testparm	#测试配置文件
```

   在windows主机c1上面打开浏览器或者资源管理器地址栏中输入

```shell
   file://10.11.58.179/share	#可查看
   
   liunx 访问smbclient
```

1. **共享一个目录，使用用户名和密码登录后才可以访问，要求可以读写**

   修改全局配置文件

   ```ini
   [global]
           workgroup = WORKGROUP
           server string = Samba Server Version %v
           security = user
           passdb backend = tdbsam
           load printers = yes
           cups options = raw
   ```

   添加一个新的共享设置

   ```ini
   [myshare]
           comment = share for users
           path = /var/www/html
           browseable = yes 
           writable = yes
           public = no
   ```

   保存配置文件，修改共享目录权限

   ```shell
   mkdir /samba
   chmod 777 /samba
   ```

   然后添加用户

   ```shell
   useradd user1	#创建测试用户
   useradd user2	#创建测试用户

   pdbedit -a user1	#添加用户为samba的用户
   pdbedit -a user2	

   pdbedit -L	#列出所有的samba用户

   service smb restart	#重启samba服务
   ```

   在windows主机上面打开浏览器或者资源管理器进行查看

2. **使用linux访问samba服务器**

   在另一台的linux的客户端c2主机上面进行操作

   ```shell
   yum install -y samba-client	#安装samba客户端

   smbclient //IP/共享名 -U 用户名
   smbclient //10.11.53.133/myshare -U user1

   #常用命令，使用help + 命令进行查看命令用法
   cd, ls, rm, pwd, tar, mkdir, chown, get, put
   #手动进行挂载
   mount -t cifs //10.11.53.133/myshare /mnt/smb -o username=user1,password=123456
   #在/etc/fstab上面进行挂载
   //10.11.53.133/myshare /mnt/smb cifs username=user1,password=123456 0 0

   file://10.11.53.133
   ```

## linux挂载windows的共享目录

1. 要在linux系统执行以下命令

   ```shell
   yum install -y cifs-utils	#必须要安装这个组件，才可以完美支持
   ```

2. 使用sbmclient来进行查看

   ```shell
   smbclient //192.168.2.103/share -U ruidong
   ```

3. 使用mount进行挂载

   ```shell
   mount -t cifs //192.168.2.103/myshare /mnt/smb -o username=ruidong,password=rd920128
   ```