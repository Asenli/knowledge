# Lesson_18

## MySql

### 1.数据库介绍

数据库是用来存放数据的,数据不是直接存放在数据库中的,数据库中存放的是表,表中存放的才是数据.

  ![图片1](images\图片1.png)

所以我们学习就是分为数据的操作,表的操作,数据库的操作.

### 2.数据库的发展史

#### 2.1萌芽阶段(文件)

所有的存储数据的文件都属于数据库.安全性低.

#### 2.2层次模型

```python
1.优点:查询分类的数据效率比较高
2.缺点:
    导航结构,如果查找不同类型的数据,那么效率非常低
    数据的不完整(如下图)
```



  ![图片2](images\图片2.png)

`注意:在数据库中,数据本身是没有对错之分的,如果数据不正确的话我们称之为'数据不完整'或'失去了数据的完整性'`

#### 2.3网状模型

  ![图片3](images\图片3.png)



`注意:网状模型解决了数据的不完整性,但是没有解决导航问题.`

#### 2.4关系模型

现在的主流数据库都是关系型数据库

`特点:每个表都是独立的,没有导航结构,表与表之间通过公共的字段建立关系.`

`注意:公共字段的名字可以不一样,但是数据类型必须一样.数据类型一样的但它不一定是公共字段.两个字段必须数据类型必须一样,字段的含义必须一样`

  ![![图片5](file:///C:/Users/ruidong/Desktop/1802-mysql/mysql_1/images/%E5%9B%BE%E7%89%875.png?lastModify=1523841995)](images\图片4.png)

 `建表语句` ![![图片5](file:///C:/Users/ruidong/Desktop/1802-mysql/mysql_1/images/%E5%9B%BE%E7%89%875.png?lastModify=1523841995)](images\图片5.png)

```python
谨记:关系模型在多表查询的时候并且数据量很大的时候,它的执行效率很低.
    在项目中,我们通过非关系型数据库来解决此问题(NoSql),redis.MongoDB.
```



### 3.记录.行.列.字段.属性.字段的属性.数据

```python
1.一行我们通常称为一条记录
2.一列称为一个字段,也叫一个属性 
  就表结构层面而言:表分为行和列
  就数据层面而言:表分为记录和字段
3.数据冗余:相同的数据储存在不同的地方
```

 ![图片6](images\图片6.png)

```python
1.冗余只能减少,不能完全杜绝
2.冗余减少了,表的体积也就减小了,更新的速度加快了,保存了数据的完整性.
3.但是减少了冗余,那么肯定增加了表,多表查询的效率又降低了,在项目中有的时候宁可让数据冗余也要保证查询的效率.(但效率和规范起冲突的,效率要大于规范,保证实用性)
```



### 4.数据的完整性

正确性+准确性 = 数据的完整性

```python
分析:学生的年龄字段(age int),储存到1000,问正确性如何?准确性又如何?
    正确但是不准确
```

`正确性:描述数据类型是否准确`

`准确性:描述数据的范围是否合理(准确)`



### 5.windows命令行运行客户端

#### (1).启动MySql

使用`CMD`开启客户端

如果你使用的是`原生`的mysql5.7,那么先要开启 命令是:`net start(stop) mysql57`

如果你是用的是第三方服务性,那么你就按规则操作.

```python
或者进入到mysql的bin目录下,电机mysqld.exe进行开启
```

#### (2).连接MySql服务器

`mysql -hlocalhost -uroot -proot -P3306`

```mysql
localhost 代表本地的IP地址
host 主机 -h
username  用户名 -u
password  密码   -p
port   端口号    -P
```



#### (3).断开连接

```mysql
1.quit
2.exit
3.\q
```



#### (4)SQL语句



[SQL](https://baike.baidu.com/item/SQL)即结构化查询语言(Structured Query Language)，是一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统；同时也是数据库脚本文件的扩展名。SQL语句无论是种类还是数量都是繁多的，很多语句也是经常要用到的，SQL查询语句就是一个典型的例子，无论是高级查询还是低级查询，SQL查询语句的需求是最频繁的。



| 关系型数据库     | 公司   | 扩展     |
| ---------- | ---- | ------ |
| access     | 微软   | SQL    |
| SQL-Server | 微软   | T-SQL  |
| Oracle     | 甲骨文  | PL/SQL |
| MySql      | 甲骨文  | MySql  |

```mysql
思考:已知SQL是标准SQL,那么在oracle上编写的PL/SQL能否在MySql上运行?
答案:不能,能相互运行的只是标准SQL.
```



#### (5)数据库操作

##### a.创建数据库

```mysql
语法:create database [if not exists] `数据库名` charset=字符的编码(utf8);
```

##### b.创建已经存在的数据库会报错

##### c.指定数据库的字符编码

```mysql
create database `数据库名` charset=字符的编码(utf8);
```

##### d.创建数据库,数据库名要加上反引号(``),你使用关键字作为数据库名可以防止报错,并创建成功.

##### e.显示数据库

语法:`show databases;`

##### f.显示创建数据库的语句

```mysql
语法:show create database `数据库名`;
```

#### (6)修改数据库

只能修改数据库的字符编码

##### 修改数据库字符集

```mysql
alter database `数据库名` charset=字符集选项;
```

#### (7)删除数据库

```mysql
drop database [if exists] `数据库名`;
```

如果删除一个不存在的数据库会报:

`1008 - Can't drop database '$%@'; database doesn't exist`

加上[if exists]

```mysql
drop database if exists `数据库名`;
#可以避免报错
#作用:判断指定的数据库存不存在,存在则删除.
```

#### (8)选择数据库

```mysql
use `数据库名`;
```

----

----

### 6.表的操作

#### (1)创建表

```mysql
create table [if not exists] `表名`(
    -> id int not null auto_increment  primary key comment'主键字段',
    -> username char(64) comment'用户名' default'root',
    -> password varchar(64) comment'密码'
    -> )engine=myisam charset=utf8;
```

注意:最后一局不能加逗号,如果加了,那么表示没写完

```mysql
1.null|not null   字符是否为空
2. default        默认值
3.auto_increment  自动增长
4.primary key     设为主键
5.engine   表的存储引擎(innodb | myisam) 
```

#### (2)常用的引擎

`innodb`,`myisam`不同的储存引擎就是储存数据的格式不一样.

IO模型,是针对硬盘的  curd  insert->create  update  read->select  delete

I  写   innodb  在写的时候更加的有优势      del  update  insert

o 读   myisam 读的时候更加的有优势         select 

#### (3)给指定的数据库建表

```mysql
 create table 数据库名.表名(
    -> id int,
    -> p char(32)
    -> );
```

#### (4)中文乱码

```mysql
create table 数据库名.表名(
    -> id int,
    -> name char(32) default'你好' #default 默认不能使用中文
    -> );
#1067 - Invalid default value for 'name'

#windows默认的是GBK

set names gbk
```



#### 7.数据库文件

一个数据库对应一个文件夹,一个表对应一个文件

#### (1)myisam引擎

```mysql
MySQL\data\python->mysql的路径

比如在python数据库文件夹下有一个user表

myisam会默认创建三个文件

user.frm  -> 表结构
user.MYD  -> 储存表数据
user.MYI  -> 储存表的索引
```

#### (2)innodb引擎

```mysql
user_info 文件是innodb的

user_info.frm  表结构.索引都是在一起的

在MySQL\data

ibdata1 ->它是储存innodb数据的,如果ibdata1满了,他会自动创建ibdata2\ibdata3
```

```mysql
总结:myisam引擎的表可以任意的移动,innodb不能任意移动.

默认的情况下,innodb的数据都存放在ibdata1文件中,可以在创建表的时候指定innodb和myisam一样,表和数据不存放在一起(后面提到)
```



### 8.表的操作

#### (1)显示表

`show tables;`

```mysql
+------------------+
| Tables_in_python |
+------------------+
| user             |
| user_info        |
+------------------+
2 rows in set
```



#### (2)显示建表结构

`show create table user\G`

```mysql
*************************** 1. row ***************************
       Table: user
Create Table: CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT COMMENT '涓婚敭瀛楁'
  `username` char(64) DEFAULT NULL COMMENT '鐢ㄦ埛鍚?,
  `password` varchar(64) DEFAULT NULL COMMENT '瀵嗙爜',
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
```



#### (3)删除表

```mysql
语法:drop table [if exists] `表1`,`表2`;
```

```mysql
mysql> drop table if exists `user`,`user_info`;
Query OK, 0 rows affected
mysql> show tables;
Empty set
```

#### (4)查看表结构

```mysql
desc `表名`;  | describe `user`;

+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(11) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | char(16)         | NO   |     | tom     |                |
+-------+------------------+------+-----+---------+----------------+
2 rows in set
```



#### (5)更改表

##### a.修改表名

```mysql
语法: alter table `old_name` rename `new_name`;
```

##### b.增加一个字段

```mysql
alter table `表名` add `字段名` 数据类型;

alter table user2 add age int(3) first;  #添加在表的第一个

alter table user2 add height int(3) after age; #添加字段在指定字段的后面
```

##### c.修改字段属性

```mysql
alter table `表名` modify `属性名(字段名)` 数据类型;
```

##### d.修改字段名

```mysql
alter table `表名` change `原字段名` `新的字段名` varchar(10) ;
```

##### e.修改字段的位置

```mysql
alter table user2 change `字段名` `改为新的字段名` char(16) after '字段名';
```

##### f.修改表的引擎

```mysql
alter table `表名` engine=innodb|myisam;
```

##### g.移动表到指定数据库并改名为指定名称

```mysql
alter table `原表名` rename to java.user;
```



#### (6)复制表

```mysql
create table `新表` select * from `原来的表`;

特点:
1.旧表的数据会一起复制过来到新表中
2.不能复制主键
```

```mysql
create table `新表` like `原来的表`;

特点:
1.它可以复制主键
2.但是不会复制数据
```



#### (7)数据操作

##### a.插入数据

```mysql
1.insert into user(`id`,`age`,`sex`) values('',18,'tom');
#值的个数要和字段数一致
2.insert into user(`age`,`sex`) values(20,'jack');
#id为自动增长字段,可以不写
3.insert into user values(null,25,'lily');
#不写字段l,40,'wj'),(null,50,'ybq');
#一次插入多条
5.insert into user set age=60,sex='hx';名,要一一对应字段个数
4.insert into user values(null,30,'lyb'),(nul
#一次只能插入一条数据   insert into 表名 set 字段='',字段='';
```

```python

#面试题
如何优化insert插入语句(一次性插入1万跳,一次性插入100万条)

答:将insert语句进行字符串拼接,拼接vaules.
    
#why?
insert每写一次都需要被机器做语法解析,语法设别,字段对应,它需要耗费时间.
```



查询:`select * from 表明;`



md5()在mysql中可以直接加密,在python中hashlib.md5().

md5 是单向加密


md5在项目中怎么加密.



```mysql
md5(123456) --->e10adc3949ba59abbe56e057f20f883e

md5(e10adc3949ba59abbe56e057f20f883e+base64(admin))
```



##### b.修改数据

```mysql
update user set sex='pgone' where id=8;
#update 表名 set 字段名='值',字段名=123 where 字段(一般使用主键)=值;
update user set sex='贾乃亮',age=40 where id=5;
#修改多个字段
```

##### c.删除数据

```mysql
delete from user where id=8;
#delete from 表名 where 字段(一般为主键)=值
#一条一条的删
delete from user where True;
#删除全部
#它也是一条一条的删
truncate user;
#记录你原来建表语句,然后删除整个表,在创建,数据全部被清空

```

