powerDesigner  企业建模工具

name 表命

code : 新建表的名字

主键这里没有任何意义

powerDesigner  设计表  导出 sql语句表 ---- mysql 导入sql语句建表 --

进入django项目 -- 反向建模 生成Models

快速反向建表三大步骤

工具： powerDesigner  、mysql 、用到django

1.设计表- tools-

![img](E:/youdaoyun/Asen634163114@163.com/19cd4afa35b64664824264c55f0dd0f3/clipboard.png)

![img](E:/youdaoyun/Asen634163114@163.com/ac188101d90c403297476449cec2b2eb/clipboard.png)

![img](E:/youdaoyun/Asen634163114@163.com/93ce5a0c9a994b45a2d144781eff4cba/clipboard.png)

这样就可以生成sql表文件了

2.命令窗口进入mysql:

输入命令： 

​    set PATH= C:\Program Files\MySQL\MySQL Server 5.7\bin;%PATH%

进入数据库

创建数据库：

create database school2 default character  set utf8;

show databases;

use  school2;

source  + 刚刚sql数据文件.sql

查看刚刚生成的表

show tables;

查看lesson 的表

desc lesson;

3.Django里面真正反向建表

在django项目里面

先进入虚拟环境下-进入到项目文件夹下- 

 d:\qianfeng\test5>python manage.py inspectdb > school2(刚刚的表命)/models.py