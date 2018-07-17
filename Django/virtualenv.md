
# VIRTUALENV虚拟环境创建指南

>Auth: 李东兵
>
>Data：2018-04-22
>
>Email：634163114@qq.com
>
>github：https://github.com/Asenli/knowledge

---

##### 前言
 1. 本教程中使用到的python版本均为python3.x版本，由于本人安装的是python3.6.3版本。
　<br>
 2. virtualenv使用场景:当开发成员负责多个项目的时候，每个项目安装的库又是有很多差距的时候，会使用虚拟环境将每个项目的环境给隔离开来。
　<br>

	比如，在有一个老项目已经开发维护了3年了，里面很多库都是比较老的版本了。例如python使用的是2.7版本的。但是新项目使用的python版本是3.6的。为了解决这种项目执行环境的冲突，所以引入了虚拟环境virtualenv。

　	当然除了virtualenv可以起到隔离环境的作用，还有其他技术方案来实现，而且上线流程简单，大大减轻运维人员的出错率，比如每一个项目使用一个docker镜像，在镜像中去安装项目所需的环境，库版本等等

### python环境的配置

1. 在cmd中能通过python去启动，如果不行直接跳到第三步
>python
![图](images/python.png)
<br>

2. 在cmd中能通过pip3启动安装软件，如果不行直接跳到第三步
>pip3
![图](images/pip3.png)
<br>

3.配置python环境和pip环境
![图](images/python_pip_envir.png)

4. 确认pip安装成功，如果Scritp文件夹下没有pip可执行文件，则执行第五步。

5. 由于python3.6安装以后，在Scripts文件中没有pip的可执行软件，需要输入一下命令进行安装

```
python -m ensurepip
```
![图](images/ensurepip.png)
注：现在在python的安装文件夹Scripts下就有pip.exe以及easy_install.exe等可执行文件了，就可以使用pip安装啦~


### windows中安装使用

1. 安装virtualenv
```
pip install  virtualenv
```
![图](images/pip_virtualenv.png)

2. 创建虚拟环境

先查看一下安装虚拟环境有那些参数，是必须填写的
>virtualenv --help
<br>
![图](images/virtualenv_help.png)
注意两个参数：
--no-site-packages和-p参数

这里venv是安装的文件名
```
virtualenv --no-site-package venv
```
以下是指定安装虚拟环境中的python版本的安装方式：
![图](images/virtualenv_env_p.png)
<br>

3. 进入/退出env
```
进入　cd env/Scripts/文件夹  在activate命令

退出　deactivate
```


### ubuntu中安装使用

1. 安装virtualenv

```
apt-get install python-virtualenv
```

2. 创建包含python3版本的虚拟环境
```
virtualenv -p /usr/bin/python3 env
```
env代表创建的虚拟环境的名称


3. 进入/退出env
```
进入　source env/bin/activate

退出　deactivate
```

4. pip使用

	查看虚拟环境下安装的所有的包　
	```
	pip list
	```
	
	查看虚拟环境重通过pip安装的包
	```
	pip freeze
	```

