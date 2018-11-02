#centos7_5

rpm安装

redhat系列的包后缀名为 .rpm，yum安装的也是使用rpm包，只不过yum为你解决了依赖问题，如果你想自己通过rpm指令安装，你需要手动解决依赖关系

安装

```python

安装
	rpm -ivh 包名
卸载
	rpm -e 包名
	rpm -e wget-1.12-10.el6.x86_64    【不带后缀】
	rpm -e wget
其它选项
	-ql : 查询包安装路径
		rpm -ql wget
	-qa : 列出系统所有的软件
		rpm -qa | grep wget
	-qi : 显示包的详细信息
```
源码安装(编译安装)

```python
在linux里面，几乎所有的软件都是c或者c++来编写的，这种语言写的程序，首先得自己编译一下，生成一个可执行文件，然后再执行这个文件
要写编译代码，你得有编译器，在linux里面编译器就是gcc，gcc-c++
yum install -y gcc gcc-c++

源代码从网上下载，下载下来之后一般都是  .tar.gz  .tar.bz2
源码安装三部曲
1、配置
	./configure [--prefix=安装路径] [--with=关联的其它依赖包]
2、编译
	使用里面自带的makefile，   make 
3、安装
	make install
安装过程中，查看上一步是否成功，输入 echo $?  输出0表示成功，其它失败
make && make install
```

2、shell简介

```python

shell就是一个命令解释器，将用户输入的指令翻译一下，结果显示给你
两种交互形式
1、指令交互式
	平常学的就是这种格式
2、脚本交互式
	需要写个脚本，然后执行这个脚本即可
	来个简单脚本看看
	shell脚本的后缀  .sh
	开头写这个
	#!/bin/bash
	#bash是linux默认自带的shell解释器   sh   csh。。。。
	
	执行脚本，要分是否在当前目录
	是：  ./test.sh
	否：  /root/test.sh
	
	shell编程
```

##3、screen

```python
在linux中，管理员通常会通过ssh协议远程登录服务器，然后去安装一些软件，执行一些程序等工作，但是有时候安装软件过程非常的长，或者程序就是死循环，这时候管理员什么也做不了，只能干等着，所以出现了screen这个软件，解决了这种问题
安装
	yum install -y screen
使用
	新建会话   screen -S one
	去往会话   screen -r two
	查看会话   screen -ls
	
在new会话中的快捷键(ctrl + a)(现在的支持不是很好)
	退出回话   ctrl + a + d
	新建窗口   ctrl + a + c
	显示所有窗口   ctrl + a + w
	上一个窗口  ctrl + a + p
	下一个窗口  ctrl + a + n
	杀死窗口    ctrl + a + k   (找准那个点)
窗口全部关闭之后，这个会话就会结束	

#如何杀死一个已经Detached的screen会话？
screen -X -S session_name quit
```

