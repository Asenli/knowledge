#centos7__4
___

(自己研究的范围)

grep后面的正则表达式有三种风格
	-E  扩展的正则表达式
	-P  perl风格的正则表达式

http://www.cnblogs.com/chengmo/archive/2010/10/10/1847287.html



vmware 关机->设置->硬盘->添加[+]->新硬盘->大小自己定->后面全部默认  



##1.磁盘管理

```python

du
	查看当前目录的子目录和文件大小
	-h  以人性化的方式显示大小
df
	显示当前磁盘设备的使用情况
	-h  人性化方式显示大小 
    
    
    
    
磁盘分区
	主分区、扩展分区、逻辑分区
	一个硬盘至少要有一个主分区，系统必须安装到主分区中
	扩展分区，是主分区以外的分区，但是扩展分区不能直接使用，需要将其分成多个逻辑分区，来使用逻辑分区
	主分区最多4个
	扩展分区一般就一个
	逻辑分区可以随便分
给虚拟机添加硬盘，首先关机，给其添加一块硬盘，我加个1G的硬盘
	1、关机
	2、右键设置
	3、点击存储
	4、在你的已有的vdi的下面再添加一个硬盘
		创建新的硬盘
		分配大小
		立即创建
	5、开机
	
```
分区

```python
开始分区
	fdisk  分区设备
	主分区两个
		/dev/sdb1   200M
		/dev/sdb2   200M
	扩展分区（只能1个）
		/dev/sdb3   600M
	逻辑分区（理论上分无数多个，我们分两个）
		/dev/sdb5   300M
		/dev/sdb6   300M
```
操作过程
​	
```python
	#1.列出挂载点信息
	df -lh
	
	#2.查看硬盘信息，第二个挂载点，应该是sdb
	fdisk -l
	
	#3.对新盘进行分区，新盘的是一个G，那个大小先用500M
	fdisk /dev/sdb
	===========================================
	m   查看帮助
	1.n   新建分区
	2.p   创建主分区
	3.默认直接敲回车  (p是主分区，e是扩展分区，l逻辑分区)
	4.默认直接敲回车 （主分区和扩展分区：1-4）（逻辑分区：5或者以上）
	5.默认直接敲回车  （扇形区）	起始
	  默认直接敲回车  （扇形区）	结尾
	6.p   查看分区信息 这个时候已经创建了好了
    
	7.t  选择格式
	8.l  查看格式
	9.8e    Linux LVM 
	10.p 在此查看去报改为 LVM
	11.w 保存设置
	===========================================
	
	#3.使用 pvcreate 命令创建物理卷
		pvcreate  /dev/sdb1   （--force或-f，有错误提示信息的时候再用
		#使用pvs打印新创建的物理卷
		pvs
		#查看物理卷信息
		pvdisplay 
		
	#4.使用 vgextend 命令把/dev/vdc1加入到centos磁盘组
		vgextend centos /dev/sdb1 
		#使用 vgdisplay 查看卷组信息，下图显示卷组名为centos，空闲大小为0：
		lvdisplay
		
	#5.使用 lvcreate 命令从卷组里划分一个新的逻辑卷，这里创建了名称为hal，大小1000MB的逻辑卷分区；
		lvcreate -L 1019M -n hal centos
		#使用lvdisplay 查看逻辑卷信息：
		lvdisplay 

	#####如果VG有未知错误
	#vgreduce --removemissing  磁盘组名
	vgreduce --removemissing centos_hal
		
	#6.格式化分区
		#将分区格式为你所需要的格式   ext4
		mkfs.xfs /dev/centos/hal   
		
		
		#挂载分区
		mount /dev/centos/hal /mnt/dev1
		
		#输入  df -h   查看分区使用信息
		
	7.设置开机挂载
		vim /etc/fstab
		添加一行
		/dev/centos/hal      /mnt/dev1      xfs        defaults        0 0
		设备名         挂载点        系统格式     默认           默认
		
		让配置文件立即生效
		mount -a
	
	
	
	8.删除分区
		fdisk /dev/sdb
		d  分区号
		挨个删除即可
```

##2、scp

```python
基于ssh协议copy
格式：   scp    源路径   目的路径
10.0.142.84   root   123456
#上传命令
scp demo.txt root@10.0.142.84:/root/test

#下载命令

#scp 用户名@IP地址：/对方文件路径加名字  /我的文件路径或单个文件名

scp   root@172.16.61.137:/root/test/demo.txt /root/test/demo.txt


拷贝目录的话需要加上 -r

scp  -r root@172.16.61.137:/root/test /root/test


如果配置了免密码的登录，scp的时候就不用输入密码了

winscp、flashFXP
	安装一下
	通过这个软件可以将windows里面的东西直接发送给linux
```

##3、软硬连接
为了解决文件共享的问题，以软连接居多（在ll显示详情的时候，在文件类型显示l的字样），硬链接了解.(link)

硬链接

```python
	指令格式：  ln  源文件  目标文件
	相当于给文件起了一个别名，修改其中一个文件，本质上是修改的都是同一个文件，通过ll可以查看硬链接的个数
	【注】硬链接不能给目录创建
	【注】硬链接创建之后，用户和组信息不变
```
软连接（常用的  soft）

```python
	就可以理解为windows下面的快捷方式
	指令格式：  ln   -s    源文件   目标文件
	修改其中一个文件，另外一个也改变
	【注】软连接可以给目录创建
	【注】当源文件丢失的时候，该软连接就会变成一个死链接，当重新创建了一个和目标文件同名文件的时候，该软连接原地满血复活
	【注】新建的软连接，用户和组信息是创建时候的用户和组信息
```
文件结构：
	在linux里面，一个文件有三部分组成，第一部分是文件名（是用户看的），第二部分是索引节点（inode，给linux系统看的），第三部分是文件的内容
	区别，详见百鸟朝凤图

##4、压缩解压

```python
在linux里面，常见的压缩格式有两种，一种叫gz，一种叫做bz2

gzip、gunzip 
	gzip 文件名
	（1）不保存源文件
	（2）不能打包压缩
	
bzip2、bunzip2
	bzip2 文件名
	（1）不能打包压缩
	-k：保留源文件并且压缩
    
tar（解压和压缩一块承包）
	比gzip和bzip2功能强大的就是打包压缩
	（1）如果使用tar指令对文件进行打包并且使用gzip压缩，那么文件后缀名为.tar.gz
	（2）如果使用tar指令对文件进行打包并且使用bzip2压缩，后缀名为.tar.bz2
	参数：
	-c : 打包文件或者文件夹
	-z ：使用gzip格式进行压缩
	-j : 使用bzip2格式进行压缩
	-f : 放到最后面，来指定压缩后的文件名
	-v : 压缩或者解压缩的时候显示过程
	-x : 解压缩
		
#bzip2理论上是没有的
#现在yum寻找

yum search bzip2 

yum install bzip2.x86_64

yum install gzip.x86_64

1、打包并且使用gzip压缩和解压
	压缩： tar -zcvf test.tar.gz test #(test 是要压缩的文件)
	解压缩： tar -xvf test.tar.gz
2、打包并且使用bzip2压缩和解压
	压缩： tar -jcvf txt.tar.bz2 *.txt
	解压缩：tar -jxvf txt.tar.bz2
```

##5、服务和进程

```python

linux的用户等级   vim /etc/inittab
	0 : 关机模式
	1 : 单用户模式
	2 : 无网络的多用户模式
	3 : 有网络的多用户模式
	4 : 保留模式
	5 : 带图形界面的多用户模式
	6 : 重启模式
切换等级
	init 等级号
	init 0      关机
	init 6      重启
查看当前等级
	runlevel
	who -r
查看随开机启动的服务
	chkconfig --list
	控制服务的开启与关闭
    iptables #防火墙
		service iptables stop | start | restart | status
		#/etc/init.d/iptables start
        #yum 默认的安装路径
	假如：你现在自己安装了一个软件，是nginx，你想通过service这个指令控制服务的开启与关闭，你需要将nginx的启动脚本放到  /etc/init.d/ 这个文件夹中，并且修改权限
		service nginx restart | start | stop
        #apache
        service httpd  restart | start | stop
	设置开机启动
		chkconfig nginx on   默认这个服务在2345模式开机启动
		chkconfig --level 35 nginx on  指定模式开机启动
top，可以实时的查看系统的运行状态，尤其是内存的使用情况
	输入大写的M  将进程按照内存利用率排序
	按q退出查看
w，查看当登录该系统的所有用户
free，查看当前系统内存使用情况   -h 以人性化的方式显示
ps，查看进程相关信息
	ps -ef | grep ssh
	ps aux | grep ssh
kill，杀死一个进程，根据进程id号杀死进程
	kill -9 进程id号
	service sshd start
在linux里面，随开机启动的服务，我们称之为守护进程（daemon）
netstat -lnp
```

top详解

```python

第一行：
13:42:59 当前系统时间
6 days, 9:29 系统已经运行了6天6小时29分钟（在这期间没有重启过）
3 users 当前有3个用户登录系统
load average: 3.06,3.01, 1.79 load average后面的三个数分别是1分钟、5分钟、15分钟的负载情况。
load average数据是每隔5秒钟检查一次活跃的进程数，然后按特定算法计算出的数值。如果这个数除以逻辑 CPU的数量，结果高于5的时候就表明系统在超负荷运转了。

第二行： Tasks 任务（进程）
系统现在共有131个进程，其中处于运行中的有3个，127个在休眠（sleep），stoped状态的有0个，zombie状态（僵尸）的有1个。

第三行：cpu状态
10.6% us 用户空间占用CPU的百分比。
2.2% sy 内核空间占用CPU的百分比。
0.0% ni 改变过优先级的进程占用CPU的百分比
84.5% id 空闲CPU百分比
2.5% wa IO等待程序占用CPU的百分比
0.1% hi 硬中断（Hardware IRQ）占用CPU的百分比
0.0% si 软中断（Software Interrupts）占用CPU的百分比
在这里CPU的使用比率和windows概念不同，如果你不理解'用户空间'和'内核空间'，需要充充电了。

第四行：内存状态
8300124k total 物理内存总量（8GB）
5979476k used 使用中的内存总量（5.7GB）
2320648k free 空闲内存总量（2.2G）
455544k buffers 缓存的内存量 （434M）

第五行：swap交换分区
8193108k total 交换区总量（8GB）
41568k used 使用的交换区总量（40.6M）
8151540k free 空闲交换区总量（8GB）
4217456k cached 缓冲的交换区总量（4GB）

这里要说明的是不能用windows的内存概念理解这些数据，如果按windows的方式此台服务器危矣：8G的内存总量只剩下530M的可用内存。Linux的内存管理有其特殊性，复杂点需要一本书来说明，这里只是简单说点和我们传统概念（windows）的不同。

第四行中使用中的内存总量（used）指的是现在系统内核控制的内存数，空闲内存总量（free）是内核还未纳入其管控范围的数量。纳入内核管理的内存不见得都在使用中，还包括过去使用过的现在可以被重复利用的内存，内核并不把这些可被重新使用的内存交还到free中去，因此在linux上free内存会越来越少，但不用为此担心。

如果出于习惯去计算可用内存数，这里有个近似的计算公式：第四行的free + 第四行的buffers + 第五行的cached，按这个公式此台服务器的可用内存： 2320648+455544 +4217456 = 6.6GB。

对于内存监控，在top里我们要时刻监控第五行swap交换分区的used，如果这个数值在不断的变化，说明内核在不断进行内存和swap的数据交换，这是真正的内存不够用了。

第六行是空行

第七行以下：各进程（任务）的状态监控
PID 进程id
USER 进程所有者
PR 进程优先级
NI nice值。负值表示高优先级，正值表示低优先级
VIRT 进程使用的虚拟内存总量，单位kb。VIRT=SWAP+RES
RES 进程使用的、未被换出的物理内存大小，单位kb。RES=CODE+DATA
SHR 共享内存大小，单位kb
S 进程状态。D=不可中断的睡眠状态 R=运行 S=睡眠 T=跟踪/停止 Z=僵尸进程
%CPU 上次更新到现在的CPU时间占用百分比
%MEM 进程使用的物理内存百分比
TIME+ 进程使用的CPU时间总计，单位1/100秒
COMMAND 进程名称（命令名/命令行）
```

##6、下载
（1）curl（自带的）
	curl -O https://mirrors.tuna.tsinghua.edu.cn/apache/httpd/httpd-2.2.34.tar.bz2
（2）wget（是一个软件，需要安装）

	yum -y install wget

	wget 地址
	-c：断点续传，通俗的理解，就是下载一半，网络断了，要不要接着上次的继续下载

##7、软件安装
yum安装

```python
	说明：
	yum是什么，yum就是你电脑上的电脑管家里面的软件管理，就是小米手机里面的应用商店，就是苹果手机appstore，就是一个软件中心
	在linux里面，很多软件之间都存在着依赖关系，如果安装软件的依赖关系来安装是一项非常复杂的工作，yum源的出现就很好的解决了这个问题
	常见的yum源：
		网易源，清华源，阿里源，搜狐源，中科大源
	配置yum源
		#这是阿里的源
		wget http://mirrors.aliyun.com/repo/Centos-7.repo
		cd /etc/yum.repos.d/
		mv CentOS-Base.repo CentOS-Base.repo.back
		curl -O http://mirrors.aliyun.com/repo/Centos-7.repo
		mv Centos-7.repo CentOS-Base.repo
		
		配置好之后
		yum clean all    清空所有
		yum makecache    生成缓存
		yum update       更新yum源
	常见yum指令
		yum install -y wget   安装
		yum uninstall -y  wget 卸载 
		yum remove -y wget    卸载
		yum list              显示所有
		yum search vim        搜索
	常用选项
		-y   过程全部yes
		--downloadonly   只下载不安装
        #使用rpm -ivh 包名 安装
		--downloaddir    指定下载的目录
		yum install -y --downloadonly --downloaddir=./ wget
```
rpm安装

yum是依赖rpm的，rpm下载和yum下载几乎一样

源码安装

先下载，在编译安装，一般依赖于gcc和make或者其他的依赖包，较为复杂





oneinstack 安装

安装nginx  mysql redis