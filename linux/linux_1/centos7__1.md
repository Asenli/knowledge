#centos7_1
___

##简述

1991年，芬兰的一个研究生linus trovslds（李纳斯脱袜子）购买了自己的第一台电脑，并且决定开始开发自己的操作系统。这个想法非常的偶然，最初只是为了满足自己读写新闻和邮件的需求。他选择了minix作为自己的研究对象。而minix是一个开放的模型操作系统。最终取名为 linux（linus 的 minix），最终在全世界形成了巨大的回响。

优点

```python

1、开源免费
2、多用户、多任务
3、良好的界面（图形化界面、字符界面）
	Ubuntu、deepin(中国开发的)
```

版本号说明

```python
输入指令查看   uname -r
2.6.32-642.el6.x86_64
linux的内核版本分为两种：一种叫做开发版，一种是稳定版
2：内核主版本
6：奇数代表开发版，偶数代表稳定版，小版本号
32：该版本修复的次数
```

发行版本

```python

常见的linux系统，只要是基于linux内核的系统都称之为linux的发行版本
发行版本有很多，不同的发行版本基本指令都是一样的，软件安装方式不一样
Debian（大便系列）
Gentoo（贱兔系列）
Ubuntu（乌班图），是大便系列的衍生版
RedHat（红帽系列）
CentOS  是红帽系列的发行版本
```

##安装系统

首先在下载centos7.2之前，我们需要一个容器，我们使用VMware，我们使用破解版。

vmware是收费的，但是我们使用的是破解版的。

打开VMware

点击创建虚拟机 -> 选择自定义 -> 下一步 -> 稍后安装操作系统 -> 点击Linux 选择CentOS 64位 -> 名字自己取 位置自己选 -> 处理器核心数量1核就够了 -> 内存1024MB -> 使用桥接网络 -> 下一步 -> 下一步 -> 下一步 -> 磁盘大小自己分配   将磁盘存储为单个文件 -> 下一步 -> 完成

现在centOS的容器就创建完毕了

右键选择容器的设置->找到CD/DVD->选择 使用ISO映像文件 然后找到.iso文件就可以了。

然后就可以点击开机就可以安装了。

```python
开机以后直接选择install centos 7

test this media & install centos 7是先测试镜像有误错误在安装

Troubleshoopting 是用来测试内存和启动救援模式修复已经存在的centos。

随后进入到了语言选择的界面：选择中文提示，点击continue

安装程序需要用户设置信息分为三个部分：本地化、软件和系统，完成这些配置可以继续安装

时区 我们使用默认的 亚洲/上海 
键盘 就是汉语
语言 中文

注意：即使是英文作为默认语言，也因该安装中文支持，否则一些中文文件无法正常的去显示。

最小安装只安装系统最基本的组件


安装位置：
我们默认只有一个硬盘区域，我们在网络开启后，可以选择添加硬盘来增加额外的存储空间。

最后在其它存储选项中，可以选择手动分区和系统是否加密。选择“我要配置分区”然后点击完成。

这个时候会进入到手动分区的页面。

点击下方的“+”添加分区

第一项挂载点就是系统目录。第二项是期望容量，这里的默认单位是MB，你也可以写2GB、100MB。

依次添加挂载点为“/boot”的引导分区，空间为1024MB。
载点为“swap”，分2GB。
最后一个挂载点“/”，不写默认把剩下的空间全部分配过去。

然后点击完成 接受更改

最后我们配置网络和主机名

点击进去以后看到“eno16777736”的网卡是关闭状态的,将它打开

在左下角看到“localhost.localdomain”，我将主机名改成我自己的名字

如果网络还需要配置IP地址信息的，可以单点配置按钮，在弹出的窗口中选着“IPV4设置”，可以看到系统默认使用DHCP的方式自动回去IP地址。

如果需要设置IP地址可以在方法中选择手动，然后添加相应的IP、子网掩码和网关。DNS服务器地址应该填写在“附加DNS服务区”选项中，如果有多个DNS需要使用逗号割开。点击完成。

确认无误以后点击“开始安装”

然后可以看见root密码。root用户通常称为根用户，在linux系统中拥有最高权限。root密码一般要设置安全级别高一些的。

由于root用户的权限太高，分给每一个管理员的时候，可能会出现一些不必要的问题和麻烦。

点击创建用户，输入用户名和密码，我们现在是学习阶段，可以分配管理员权限。一般不给管理员权限，必要的时候向root用户申请权限。

安装完毕以后点击重启
```



##为什么使用CentOS7了？和6版本有什么不同

centos7与6之间最大的差别就是初始化技术的不同，7采用的初始化技术是Systemd,并行的运行方式，除了这一点之外，服务启动、开机启动文件、网络命令方面等等，都说6有所不同。让我们先来了解一下系统初始化技术的演变过程。

###1.系统初始化技术
```python
Sysvinit技术
Upstart技术
Systemd技术

Sysvinit技术

特点：

1.系统第1个进程为init;
2.init进程是所有进程的父进程，不可kill；
3.大多数Linux发行版的init系统是和SystemV相兼容的，被称为sysvinit
4.代表系统：CentOS5 CentOS6

优点：

sysvinit运行非常良好，概念简单清晰。它主要依赖于shell脚本。

缺点：

1.按照一定顺序执行——>启动太慢。
2.很容易hang住，fstab与nfs挂载问题
```
```python
Upstart技术

CentOS6采用了upstart技术代替sysVinit进行引导，Upstart对rc.sysinit脚本做了大量的优化，缩短了系统初始化的启动时间。但是CentOS6为了简便管理员的操作，upstart的很多特性并没有凸显或直接不支持。
```
代表系统：CentOS6, Ubuntu14, 从CentOS7, Ubuntu15开始使用systemd

```python
Systemd技术

新系统都会采用的技术（RedHat7,CentOS7,Ubuntu15等）；
设计目标是克服sysvinit固有的缺点，提高系统的启动速度；
和Sysvinit兼容，降低迁移成本；
最主要优点：并行启动
Pid为1的进程
```

###2.在yum源上的优化

```python
在centos6的时候，默认是从官方源下载rpm包的，由于是国外的yum源很慢不能用，CentOS7在这里做了优化，当我们使用yum安装软件的时候，默认不会再从官方下载，而是自动寻找离自己地理位置最近的yum源开始下载。
```

###3.命令

```python
如果在安装系统的时候选择minimal，会比之前6的时候以更小的包来安装，比如：vim、ifconfig、route、setup、netstat等等很多命令都没有了。。在安装系统后可加入以下软件包：

yum install lrzsz tree net-tools nmap vim bash-completion lsof dos2unix nc telnet ntp wget rng-tools psmisc screen -y
```
比如ifconfig是查看网卡信息的，centos7中没有，那么我们使用yum安装`net-tools`来提供一些网络的命令。

```python
bash-completion 自动命令补全的工具

psmisc 这个包含有killall命令。
 
screen 可以新建一个窗口，把任务放在后台运行。

rng-tools   生成随机数嫡池的一个工具，有了这个工具tomcat 启动会变得非常快

lrzsz 支持windowns平台的上传下载linux。在windowns远程连接工具上可以使用。
```
###4.字符集修改

centos6的时候修改字符集：

```python
vim /etc/locale.conf  #字符集配置文件
localectl set-locale LANG=zh_CN.UTF-8  
```
而centos7只需要一行命令搞定

```python
localectl set-locale LANG=zh_CN.UTF-8

localectl status
```

###5.开机启动管理

centos6依靠`/etc/rc.local`对开机启动进行管理的，但是这个文件的权限是开放的。


而centos7

```python
/etc/rc.local  # 这个文件还是存在，不过如果我们还想继续使用这种方式需要给它加执行权限chmod +x /etc/rc.d/rc.local

# system一统天下 snapshot(支持快照)

systemctl status cron.service #查看定时任务状态
systemctl stop cron.service   #关闭定时任务
systemctl status cron.service  #查看操作情况
systemctl  list-unit-files|grep enable  #查看当前正在运行的服务
systemctl   disable postfix.service #关闭邮件服务
systemctl  list-unit-files|grep postfix #查看邮件服务是否开启
systemctl stop firewalld.service #关闭防火墙
systemctl  is-enable #开启的服务 
systemctl  disable   #关闭的服务
```
centos7 通过/etc/rc.d/rc.local/开机自启动

```python
centos7中/etc/rc.d/rc.local需要执行如下命令赋予可执行权限
chmod +x /etc/rc.d/rc.local
```

###6.运行级别runlevel

centos6   "/etc/inittab" 在centos7中是无效的。

centos7  system target 替代 了inittab

```python
##永久生效下次登录生效
systemctl get-default graphical.target 切换到5
systemctl get-default multi-user.target 切换到3
##临时生效的话 
init3


#查看运行级别
ls -lh /usr/lib/systemd/system/runlevel*.target
```

运行级别（Runlevel）指的是Unix或者Linux等类Unix操作系统下不同的运行模式。运行级别通常分为7等，分别是从0到6，但如果必要的话也可以更多。

例如在大多数linux操作系统下一共有如下6个典型的运行级别：

```python
0 停机
1 单用户，Does not configure network interfaces, start daemons, or allow non-root logins
2 多用户，无网络连接 Does not configure network interfaces or start daemons
3 多用户，启动网络连接 Starts the system normally.
4 用户自定义
5 多用户带图形界面
6 重启
```

##ssh进行访问
windows下安装xshell来进行可以远程访问。

而mac 是用ssh命令 

```python
ssh 用户名@ip地址:端口号

默认的端口号22可以不写
ssh root@10.11.51.117
```

首先我们先下载‘net-tools’，这样可以使用ifconfig查看网卡信息，它的作用和DOS命令ipconfig一样。

下载完成以后输入：ifconfig

然后可以找到你的ip地址

如果ssh链接被拒绝：

1.验证openssh-server
```python
首先，要确保CentOS7安装了  openssh-server，在终端中输入

yum list installed | grep openssh-server

如果出现了结果那么表示已经安装


没有安装输入

yum install openssh-server -y
```
2.配置你的ssh文件

```python
找到了  /etc/ssh/  目录下的sshd服务配置文件 sshd_config，用Vim编辑器打开

如果没有vim编辑器那么执行：

yum install vim -y

vim编辑器比vi编辑器增加了颜色识别

vim /etc/ssh/sshd_config

直接输入/Port 

可以看见：
================
1.将文件中，关于监听端口、监听地址前的 # 号去除

Port 22
#AddressFamily any
ListenAddress 0.0.0.0 #任意地址
ListenAddress ::
================
去上面3行的注释

要想编辑的话需要按键盘i，代表insert，取消输入按esc

================
2.然后开启允许远程登录
PermitRootLogin yes
================

================
3.开启使用用户名密码来作为连接验证
PasswordAuthentication yes
================

最后保证在取消输入的状态下
输入
================
：wq! 
================
代表强制保存退出

配置完成后需要重新启动一下sshd服务

开启  sshd  服务，输入 sudo service sshd start
检查  sshd  服务是否已经开启，输入ps -e | grep sshd
或者输入netstat -an | grep 22  检查  22 号端口是否开启监听
```
##简单操作

```python
ifconfig    查看ip地址
		ping  ip地址     用来测试网络是否联通
			通过ctrl + c 来停止这个进程
		ls 
			显示当前文件夹（目录）下面的所有文件
		pwd
			显示当前目录的路径
			根目录   /
		cd   目录的路径
			切换到指定目录
		绝对路径、相对路径
			绝对路径：相对于根目录的路径
			相对路径：相对于当前目录的路径
			.       : 代表的就是当前目录
			..      ：代表的就是上一级目录
			cd      : 直接来到家目录下面
			cd -    : 回到之前的目录（回看）
		[root@localhost /]#
			root：当前用户名
			localhost：主机名
			/：   当前所在目录
			#：   代表超级管理员在执行指令
			$:    代表普通管理员在执行指令
		拍快照（恢复到快照）
			纯净水系统
		tab键（自动补全）
			指令和路径都可以自动补全
			
		clear 清理屏幕
	目录：
			/：根目录
		~	: 家目录（就是你可以肆意妄为的地方）
			linux每一个用户都有一个家目录，那意思就是说你这个用户在你的家目录下面拥有至高无上的权限
			root的家目录就在   /root
			普通用户的家目录在   /home/ruidong   
		. 	：当前目录
		..  ：上一级目录    cd ../../（上一级的上一级）
```

##指令

```python
关机：poweroff   halt   
		shutdown  now
		shutdown -h +5   'woyaoguanjile'    5分钟之后关机
		shutdown -h 16:10    下午4点10分关机
	重启：reboot   
		shutdown -r now
	date
		查看当前时间日期
	cal
		查看当月日历
		cal 8 2017   查看2017年8月的日历
		cal 2017     查看2017年所有的日历
	上下方向按键
		快速的调出历史指令
```