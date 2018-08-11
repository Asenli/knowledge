**主：**(master)

```
找到windows里面的my.ini文件增改下面的
server-id=200
innodb-flush_log-at_trx_commit=2
sync_binlog=1                 #开启binlog日志同步功能
log_bin=mysql-bin-200  #binlog日志文件名

#下面这个不写就可以同步随意的库
binlog-do-db=xxx #这个表示之同步某个库

重启主库mysql
net stop mysql57
net start mysql57 

mysql -uroot -p #登录mysql


grant replication slave on *.* to 'ldb'@'10.7.152.145' identified by '123456';

#ldb 是下面测试登录主成功的账户名 
#ip是从的ip  密码是从连接的密码


show master status;  #查看主库的状态
```

**从（slave):**

```
配置：
找到windows里面的my.ini文件增改下面的

server-id=201                #设置主服务器的ID
innodb_flush_log_at_trx_commit=2  
 #操作系统崩溃或者系统断点的情况下，上一秒钟所有事务数据才可能丢失
sync_binlog=1                 #开启binlog日志同步功能
log_bin=mysql-bin-201  #binlog日志文件名


net stop mysql57
net start mysql57 
# 重启Mysql  

从：
mysql -u ldb -h 10.7.152.138 -p

#主那里设置的名字ldb账户 ip是 自己的ip（但是必须主要设置这个Ip权限）  输入密码是主那里设置的123456
```

再退出 进入自己的mysql

```
mysql -uroot -p

change master to master_host='10.7.152.138',master_user='ldb',master_password='123456',master_log_file='mysql-bin-200.000001',master_log_pos=660;       
#master_host自己的ip
#660是主 show master status；查看的数字  master_log_file也是


start slave;
show slave status \G；
此时如果是两个YES就成功了
```

现在主（master）那边，从新开个命令窗口，进入mysql 创建个数据库，从里面也要有个同名的数据库 在新开的命令窗口新建表 在从里面show 数据库表就可以看到刷新