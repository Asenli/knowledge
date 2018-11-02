#centos7_3
___

##1、用户和组

```python
用户
切换用户  su
	root用户切换到普通用户   su ruidong   不用输入密码
	普通用户切换到root用户   su       需要输入密码
	切换完之后，使用exit退出那个用户即可
	whoami   查看当前用户名
	sudo  指令   临时使用root用户执行这条命令，需要输入密码
组

查看组
cat /etc/group


添加
	groupadd  组名
	-g   指定组id
修改
	groupmod
	-g  修改组id
	-n  修改组名   groupmod -n 新名字 旧名字   将tang组名字修改为tangke
删除
	groupdel 组名
	如果一个组是某个用户的主组，那么这个组不允许被删除，你需要首先删除这个用户
	如果一个组是系统自动为用户创建的，那么删除用户的时候会自动将这个同名的组给删除掉
```

##2、文件权限

```python

r：可读		w：可写		x：可执行		-：没有权限
权限的表示法：  
---		000		0    没有权限
--x		001		1    可执行
-w-		010		2    可写
-wx		011		3    可写可执行
r--		100		4    只读
r-x		101		5    可读可执行
rw-		110		6    可读写
rwx		111		7    可读可写可执行


该用户的权限        组内用户的权限		组外用户的权限
rwx    				r-x    				r-x
7                   5                   5 

修改权限    chmod
	格式：  chmod   权限   文件路径
	chmod 0755 1.txt
	7:user
	5:group
	5:other
    #不推荐使用,毛病多
	chmod u+x 1.txt
	chmod g-x 2.txt
	chmod o+w 1.txt
	chmod u-x,g-w,o-w 1.txt
	
	chmod -R 777 test/
	修改目录权限的时候，添加-R选项，递归的修改子文件的权限和该目录权限一致
    
修改用户
	chown  用户名  文件路径
	chown ruidong 1.txt             修改用户
	chown ruidong:ruidong 1.txt       修改用户和组
	chown :ruidong 1.txt            修改组
修改组
	chgrp   组名   文件路径
	chgrp ruidong 1.txt             仅仅修改组
umask
	文件的默认权限是   644  （文件默认都没有执行权限）
	目录的默认权限是   755
	777-022 = 755
	umask就能决定文件或者目录的默认权限是什么
	umask -S  查看默认权限
	如果想修改默认权限
```

##3、文件搜索

```python

find    可以找到你想要的文件
格式：  find [目录] [选项] [选项值]
目录：去哪找，可以不写，默认代表当前目录
选项：怎么找
	>> -name   按照名字找
		可以使用通配符
	-size   按照大小找
		单位为  kmg   10k（等于10k）   +10k（大于10k）   -10k（小于10k）
	-user   按照用户名
	-group  按照组名
	-maxdepth  -mindepth   限制查找的目录层级，默认递归查找所有
	-ctime  按照创建时间查找
		单位是天
选项值：找什么
	find / -name demo.txt
	find / -name \*.txt
	find / -size +10k
	find / -user demo.txt
	find / -group demo.txt
	find / -mindepth 4 -name \*.txt
	find / -mindepth 3 -maxdepth 5 -name \*.txt
```

##4、文件内容搜索

```python

grep   查找的内容   文件路径
grep movie demo.txt
grep that ~/*.txt

选项
	--color=auto   将颜色高亮显示
		给 grep 指令起一个别名   vi ~/.bashrc
		添加一行     alias grep='grep --color=auto'
		让配置文件立即生效       source ~/.bashrc
	-c         得到内容的个数
	-i         不区分大小写的查找
	-n		   显示在文档中的行号
	-r         递归查找，但是不能限制后缀，只能遍历所有
		grep -r that ~/*
	-l		   只显示文件名，不显示内容
	grep -l 你好 ~/test/*.txt
	
	
正则表达式进行查找(少用)
	\w(数字字母下划线)   
	\W(除了上面)
	\d(数字)
	\D(非数字)
	.(除了换行符)
	*(任意多个)
	+(至少1个)
	?(0个或者1个)
	te-st@163.com   abc_def@qq.com   lala@sina.cn   benben@meme.net
	
	grep -E .*? demo.txt 
	
	-E   使用正则表达式来进行匹配
```

##5、管道

```python
前一个管道的输出是后一个管道的输入
前一个指令的输出是后一个指令的输入
格式：
	指令1 | 指令2
	指令1的结果作为指令2的输入，然后将指令2的输出显示到屏幕中
常用的管道指令

	#ll=select /etc=table  |  less = page
	ll /etc | less
	ll /etc | grep sudo   常用格式
	ll /etc | head -10 | tail -5   显示前10条的后5条
	
```

##6、搭建主机信任

```python
10.11.58.35
root
123456

#协议 22
#语法 ssh 帐户@IP地址:端口号(但是,默认的是22,如果端口号被修改过,那么需要带上)
ssh root@10.11.53.58

#scp上传和下载
#scp是基于ssh协议的
#下载
#语法:scp  帐号@ip:需要下载的文件路径  下载到本地的路径
scp username@servername:/path/filename /tmp/local_destination
    
#上传
#语法:scp 需要上传的文件路径 帐户@IP:上传的路径
scp /path/local_filename username@servername:/path  
    
    
    
密码学：加密，解密
rsa 非对称加密
加密和解密的时候，用到一个东西，密钥
加密和解密的时候，密钥是否相同，如果相同，称之为对称加解密，如果不相同，非对称加解密
公钥：公开的，你们都能拿到
私钥：私有的，只有我知道
这一对，成对出现

ssh免密码登录
主机1通过ssh协议登录主机2
1、在主机1上面生成公钥和私钥
	ssh-keygen -t rsa    敲回车生成即可
	在 ~/.ssh 中生成两个文件   id_rsa(私钥)
	
	=====================
Enter file in which to save the key (/root/.ssh/id_rsa):    #显示密钥对的位置
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.    #私钥的位置
Your public key has been saved in /root/.ssh/id_rsa.pub   #公钥的位置
The key fingerprint is:
64:42:ba:35:e7:fb:4d:cf:6c:ad:e8:d5:df:14:f5:1b 
	=====================
	

2、将公钥粘贴到主机2中

cd .ssh/;ls

=========================
id_rsa  id_rsa.pub  known_hosts

#把id_rsa.pub文件发送到对方主机上去
=========================

scp id_rsa.pub root@172.16.61.137:/root/.ssh
#需要输入密码，显示100%就表示成功了。
#如果对方的主机里面没有.ssh文件夹，那么久手动创建一个

#本人在root目录操作的,其它人如操作不当,本人一概不负责

3.#重定向到authorized_keys
cat id_rsa.pub.back >> .ssh/authorized_keys

rm -f id_rsa.pub
#把id_rsa.pub写入到authorized_keys文件中

cat authorized_keys
#查看写入成功没有

3、在主机1再次通过ssh登录实现免密码，免密码传输
```

##7、重定向

```python
标准输入（stdin，键盘就是其标准输入）、标准输出（stdout，屏幕就是标准输出）
输出重定向
	ls > demo.txt   先清空，再写入
	ll >> demo.txt  追加
错误重定向
	将指令错误提示信息写到文件中
	ls 100 2> error.txt   
	ls 300 2>> error.txt
输入重定向（不常用）
	linux默认从键盘获取输入
	cat > 1.txt
	从键盘获取输入，完毕之后，敲 ctrl+d  结束输入
重定向
	cat > 1.txt < 2.txt  # = cat 2.txt > 1.txt
```

##8、挂载

```python
挂载是什么意思
windows
买了一电脑，有个硬盘，给硬盘搞了几个分区，然后再电脑中就会冒出几个盘符
	c   d   e   f
u盘   弹出一个盘符  打开这个盘符就是操作这个u盘
linux
没有盘符，只有一个  /  
桌面端，这种弹出盘符操作也已经集成好了
在字符界面，问，盘符如何弹出，需要你手动挂载，挂载就是将linux中的一个目录和你的u盘对应的过程，该目录称之为挂载点，以后你操作这个目录就是操作这个u盘
取消挂载，用完之后，取消挂载即可

插上u盘
选择 虚拟机->可移动设备->找到移动储存的名字->连接

1.查找设备   fdisk -l

一般第一块盘叫sda 第二块叫sdb 第三块 sdc 以此类推

	/dev/sda    这是你的第一块硬盘 
		/dev/sda1   第一个分区 
		/dev/sda2   第二个分区 
	/dev/sdb    这是你的第二块硬盘
		/dev/sdb1   第一个分区

#普通的fat32可以直接挂载
#ntfs 不能直接挂在
#exfat 不能直接挂载
mount

	格式   mount [参数] 设备 挂载点
	-t   指定格式
		msdos===>fat16
		vfat====>fat32
		nfs=====>网络文件系统格式
		auto====>自动识别
		ntfs====>ntfs
	-o
		iocharset=utf8
	mount -o iocharset=utf8 /dev/sdb1 /mnt/usb
	mount -t vfat -o iocharset=utf8 /dev/sdb1 /mnt/usb/
		
umount
	umount /dev/sdb1 /mnt/usb
	umount /dev/sdb1
	umount /mnt/usb
```

挂载exFAT格式的优盘

```python

需要安装epel库，Nux Dextop库，再安装fuse-exfat和exfat-utils包，即可识别exfat格式。   

Nux Dextop是类似CentOS、RHEL、ScientificLinux的第三方RPM仓库（比如：Ardour，Shutter等等）。目前，Nux Dextop对CentOS/RHEL 6|7可用。

1.#Nux Dextop库依赖于EPEL库，所有要先安装EPEL库(需要管理员权限)。
#如果安装过则跳过。

yum -y install epel-release


2.#对于RHEL/CentOS 7(复制/粘贴):
$ rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

3.检查Nux Dextop是否安装成功：

$ yum repolist

如果仓库列表中有Nux Dextop就安装成功。

4.由于Nux Dextop仓库可能会与其他第三方库有冲突，比如（Repoforge和ATrpms）。
所以，建议默认情况下不启用Nux Dextop仓库。

#打开vim /etc/yum.repos.d/nux-dextop.repo，将"enabled=1" 修改为 "enabled=0"。

vim /etc/yum.repos.d/nux-dextop.repo


5.#安装exfat支持库文件
yum --enablerepo=nux-dextop  install fuse-exfat exfat-utils -y

6.#现在可以挂载了
#如果有sdb1 那个就挂载sdb1  如果没有那么就挂载sdb
mount -o iocharset=utf8 /dev/sdb1 /mnt/usb
#取消挂载
umount /mnt/usb
```
