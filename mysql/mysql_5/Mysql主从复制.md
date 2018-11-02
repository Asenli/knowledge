# Mysql主从实验

## 主从的概念

## 操作步骤

1. 关闭selinuxs

   ```mysql
   #以下针对两台服务器同时操作
   chkconfig selinux off  
   #关闭开机启动
   setenforce 0    
   #关闭selinuxvim /etc/selinux/config 
   #编辑配置文件
   SELINUX=disabled 修改这一行chkconfig iptables off 
   #关闭防火墙的开机启动
   service iptables stop   #关闭防火墙
   getenforce  #检测是否关闭
   ```


1. 修改主服务器的配置

   ```mysql
   vim /etc/my.cnf
   ```

   修改如下行

   ```mysql
   [mysqld]#添加在mysqld模块下
   log-bin=mysql-bin   #要开启
   server-id=5 #建议改成服务器ip地址的后一位
   #master端：
   binlog-do-db= python #二进制需要同步的数据库名
   binlog-ignore-db=mysql  #避免同步 mysql 用户配置，以免不必要的麻烦
   #slave端:
   replicate-do-db= python        #(do这个就是直接指定的意思) 
   replicate-ignore-db=mysql
   #重启服务器
   service mysqld restart
   ```

   2.数据库结构一致

   ```mysql
   mysql -uroot -p
   #连接两台服务器的mysql，进行相同的操作。
   create database python;
   use python;
   #master端：
   create table user (  
     id int primary key  auto_increment,  
     username varchar(30))engine=innodb;
   #slave端:
   create table user ( 
     id int primary key  auto_increment,
     username varchar(30))engine=myisam;
   ```

​    3.查看主数据库信息

```mysql
#进入mysql 
mysql -uroot -p #连接主服务器  
#查看主服务器状态
show master status\G
*************************** 1. row ***************************             File: mysql-bin.000012  #master_log_file=mysql-bin.000012       
Position: 554           #pos master_log_pos= 554      
Binlog_Do_DB: python 
Binlog_Ignore_DB: mysql
Executed_Gtid_Set: 
```

4.配置从服务器

```mysql
mysql -uroot -p #连接从服务器
#查看监听语句
? change master;
#? 自醒的意思
? change
#stop slave 必须是从服务器关闭的状态下
change master to
master_host='10.11.51.85',
master_user='ruidong',
master_password='123456',
master_log_file='mysql-bin.000012',  #需要做交换的文件名
master_log_pos=723;

start slave;    #开启从服务器
show slave status \G;  
#查看状态#==================#当看到
Slave_IO_Running: Yes
Slave_SQL_Running: Yes
#===================
```