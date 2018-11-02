# Git

版本控制系统,SVN ,GIT



一个项目由多人开发



```python
SVN不支持多分支 它是本地的仓库,但是,近年它开始做线上分享
GIT支持多分支
GIT的功能更加强大,由于国外的github,国内的 码云,使程序员的代码更加具有开源性.
```



Git是一款免费、开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目.

可以有效、高速的处理从很小到非常大的项目版本管理。[2][ ](undefined) Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。



安装命令

yum -y install git



### README.md

```python
README.md 作用是书写项目的简洁,目录结构,实现的功能,或者可以添加开发团队信息
```





```python
#克隆
git clone https://gitee.com/ruidong/lyb.git
    
    
#如果是第一次提交需要绑定你的邮箱和用户昵称
#最少提交一次,下班之前
git config --global user.name 'ruidong'
git config --global user.email 'this_my_email@126.com'


#怎么保持同步
写了新文件/更新了文件,需要提交
#添加到本地缓存系统
git add demo.txt  #添加到单个文件到缓存
git add .         #将所有文件添加到缓存
# 提交到远程git仓库缓存
git commit -m '备注信息'
#远程git仓库缓存 -推(更新/提交)
git push --all



#如果别人提交了代码,或者对某个文件进行了修改,并再次提交,你就需要拉取最新的代码
#每天早上开机,git pull
git pull

#git有个规则
#谁提交的xxx.py,git默认只能由这个人修改,如果是别人修改的,那么会代码冲突.
#冲突的话

demo.py
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print(123)
====================================
print(000123)

#git status 查看状态
查看当前代码包状态
```

