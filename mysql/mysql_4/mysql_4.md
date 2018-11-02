# Lesson_4

# MySql

## 1.union联合查询

```mysql
将多个select语句的结果纵向组合

select * from stuinfo union select * from stuinfoo;


union:
1.all #显示全部记录
2.distinct  #(去除重复的值  他是默认)

select * from stuinfo union all select * from stuinfoo;
```

查找北京的女生和上海的男生  `[晚上自己写一篇或多编]`

```mysql
select * from stuinfo where (city='上海' and sex='male') or (city='北京' and sex='female');

select * from stuinfo having city='上海' and sex='male' union all select * from stuinfo having city='北京' and sex='female';
```

```mysql
Union的要求:
1.两边的select语句的字段数要一致
2,字段名可以不一样,最终按照第一个select语句的字段名返回
3.两边可以具有相同或不同的数据类型
```

男生的年龄降序,女生的年龄升序    ` [ 晚上自己写一篇或多编]`

```mysql
(select * from stuinfo having sex=1 order by age desc limit 1000) union all (select * from stuinfo having sex=2 order by age asc limit 1000);
```

## 2.多表查询

### (1)分类

```mysql
1.内连接
2.外连接
	a.左外连接
	b.右外连接
3.交叉连接
4.自然连接
```



### (2)内连接(inner join)

```mysql
#查询学生信息
select * from stuinfo inner join stumarks on stuinfo.sid = stumarks.stuno;
#inner 可以不用写
#给表取别名的 as 也可以省略不写
select * from stuinfo a join stumarks b on a.sid = b.stuno;

#inner join数据不完整就不显示

大坑别踩:

表连接肯定经常要用,如果你查询单条数据,而这条数据的从表信息不完整,使用内链接,查询出的结果为空,
但是,python代码的写法是一致的,为了避免python报错,基本不使用内链接.
```



### (3)外连接

#### a.左外连接(left  join)

```mysql
select * from stuinfo a left join stumarks b on a.sid=b.sid;
#以左边的表为准,右边表中没有的记录用null表示
```

#### b.右外连接(right join)

```mysql
select * from stuinfo a right join stumarks b on a.sid=b.sid;
##以右边的表为准,左边表中没有的记录用null表示
```

```mysql
思考:
select * from 表一 inner join 表二 on 表一.公共字段=表二.公共字段;
select * from 表二 inner join 表一 on 表二.公共字段=表一.公共字段;

select * from 表一 left join 表二 on 表一.公共字段=表二.公共字段;
select * from 表一 right join 表二 on 表一.公共字段=表二.公共字段;

select * from 表一 left join 表二 on 表一.公共字段=表二.公共字段;
select * from 表二 right join 表一 on 表二.公共字段=表一.公共字段;

```

### (4)交叉连接(cross join)

```mysql
#交叉连接返回的结果和内链接一样的
select * from stuinfo a cross join stumarks b on a.sid=b.stuno;
select * from  stuinfo,stumarks;
```

### (5)自然连接(natural)

```mysql
1.natural join #自然内连接
2.natural left join #自然左外连接
3.natural right join #自然右外连接

select * from stuinfo a natural join stumarks b;
select * from stuinfo a natural left join stumarks b;
select * from stuinfo a natural right join stumarks b;

结论:
1.自动判断连接条件,依据的是同名字段名
2.如果没有同名的字段名返回的是笛卡尔积
3.自动返回结果并进行整理;
	a.连接字段最好保留一个
	b.连接字段最好放在最前面
```

### (6)using

```mysql
#指定连接字段,using也会查询出的结果进行整理,整理的方式和自然连接相同.

select * from stuinfo left join stumarks using(sid);
```



## 练习

```mysql
1.显示地区和每个地区参加数学考试的人数,并且按人数降序排列
select a.city,count(b.math)  c from stuinfo a left join stumarks b using(sid) group by city order by c desc;

2..显示男生人数和女生人数
select a.sex,count(a.sex) from stuinfo a group by sex;

select sex,count(sex) from stuinfo where sex=1 union select sex,count(sex) from stuinfo where sex=2;

select sum(sex=1) 男,sum(sex=2) 女 from stuinfo;


3.显示每个地区的男生人数,女生人数,总人数
select city 城市,count(sex) 总人数,sum(sex='male') 男, sum(sex='female') 女 from stuinfo group by city;

```

## 3.子查询

```mysql
什么叫子查询?
查询语句中还有查询语句,外面的查询称为父查询,里面的叫子查询.
子查询为父查询提供查询条件.

例题:查询数学成绩是80分的学生
#普通的查询
select * from stumarks left join stuinfo using(sid) where math=80;
#子查询
select * from stuinfo where sid=(select sid from stumarks where math = 80);
#如果使用等于,那就必须确保子查询查到的结果只有一个
#子查询的结果只能是单一的字段


例题:查找数学最高分的学生
#普通的查询
select a.sid,a.sname,a.sex,a.age,a.city,max(b.math) from stuinfo a left join stumarks b using(sid);#问题 


#子查询
select * from  stuinfo where sid = (select sid from stumarks where math = (select max(math) from stumarks));
```

### (1)in|not in

```mysql
如果子查询中返回了多条记录,使用 = 会发生错误,那么就必须要用in

例题:查询数学成绩不及格的学生
 select * from stuinfo where sid in (select sid from stumarks where math in (select math from stumarks having math<60));

#1.数学成绩不及格 <60 60种可能
select math from stumarks having math<60; #查询到的有可能是一个也有可能是多个(58,59)
#2.这些成绩是那些学生的(sid)
select sid from stumarks where math in (58,59);   #(3,4)
#3.根据学号查找学生的信息
 select * from stuinfo where sid in (3,4);


例题:查询没有参加考试的学生
select * from stuinfo where sid in (select sid from stumarks where math is null);
```



### (2)some | any|all

```mysql
some和any是一样的,表示一些,类似与 in
all 表示全部的元素
#some
select * from stuinfo where sid =some (select sid from stumarks where math<60);

select *from stuinfo where sid =any (select sid from stumarks where math<60);

#条件都满足
select * from stuinfo where sid =all (select sid from stumarks where math<60);

查询数学90分以上的学生
select * from  stuinfo where sid not in (select sid from stumarks where math<90);

select * from  stuinfo where sid != some (select sid from stumarks where math<90);
#some = in  !=some不等与 not in
#!=all 等同 not in


查询数学90以下的学生
select * from  stuinfo where sid =some (select sid from stumarks where math in(select math from stumarks having math<90));
```



### (3)exists | not exists 

```mysql
如果有人math超过100分,就显示所有学生的信息
select * from stuinfo where exists(select * from stumarks where math>=100);
#成绩未达到100分就显示
select * from stuinfo where not exists(select * from stumarks where math>=100);
```



### (4)子查询分类

```mysql
1.标量子查询:子查询返回的值只有一个 sid = 
2.列子查询:子查询返回一个列表 sid in (3,4)
3.行子查询:查询多个条件由多个字段组成的行形成:

select * from stumarks where (sid,ch,math) in (select * from stumarks where math=100);
#例如python中
sid,ch,math = ((3,4),(88,99),(100,88))

找出语文成绩最高的男生和女生:


select * from stuinfo where sid in (select sid from stumarks where ch in ( select max(ch) from stuinfo left join stumarks using(sid) group by sex));
```



## 4.视图

```mysql
1.视图是一张虚拟的表,他表示一张表的部分数据或多张表的综合数据,
视图的结构是建立在表的基础上
2.视图中没有数据,只有表结构,视图中的数据在基表中获取
3.一张表可以创建多个视图,一个视图可以引用多张表
```

### (1)创建视图

```mysql
create [or replace] view `视图名`
as
sql语句
```

```mysql
create view stu_view_1
as
select sid,sname,age,sex,city,ch,math from stuinfo left join stumarks using(sid);


#视图创建完毕后,会在对应的文件夹中保存一个.frm的文件,子文件是视图的结构
```

### (2)查询

```mysql
select * from `stu_view_1`;
```

### (3)修改视图

```mysql
alter view stu_view_1
as
select * from stuinfo;
```

### (4)查看视图的信息

```mysql
show create view stu_view_1\G



mysql> show create view stu_view_1\G
*************************** 1. row ***************************
                View: stu_view_1
         Create View: CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL
SECURITY DEFINER VIEW `stu_view_1` AS select `stuinfo`.`sid` AS `sid`,`stuinfo`.
`sname` AS `sname`,`stuinfo`.`sex` AS `sex`,`stuinfo`.`age` AS `age`,`stuinfo`.`
city` AS `city` from `stuinfo`
character_set_client: gbk
collation_connection: gbk_chinese_ci
1 row in set (0.00 sec)
```



### (5)查看视图的结构

```mysql
desc stu_view_1;

mysql> desc stu_view_1;
+-------+-----------------------+------+-----+---------+-------+
| Field | Type                  | Null | Key | Default | Extra |
+-------+-----------------------+------+-----+---------+-------+
| sid   | int(11)               | NO   |     | 0       |       |
| sname | varchar(255)          | YES  |     | NULL    |       |
| sex   | enum('male','female') | YES  |     | NULL    |       |
| age   | tinyint(4)            | YES  |     | NULL    |       |
| city  | varchar(64)           | YES  |     | NULL    |       |
+-------+-----------------------+------+-----+---------+-------+
5 rows in set (0.00 sec)
```



### (6)查找视图;

```mysql
show tables;#它也可以查看视图

select table_name from information_schema.views;

show table status where comment='view'\G;
```



### (7)删除视图

```mysql
drop view stu_view_1;
```

```mysql
找出语文成绩最高的男生和女生:
select * from stu_view_1 where(sex,ch) in (select sex,max(ch)from stu_view_1 group by sex);
#把查询当作是数据源,命名为t
select * from (select * from stu_view_1 order by ch desc) t group by sex;
```

```mysql
create view vw_1
as
select * from stu_view_1 order by ch desc;
```



### (8)视图算法理论

```mysql
1.merge:合并算法(将视图语句与外层语句合并执行)
2.temptable:临时表算法(将视图执行的结果作为一个临时表,再执行外层语句)
3.undefined:未定义算法,由mysql自己决定,一般使用的都是merge

#给视图指定算法
create or replace algorithm=merge view vm_2
as
select * from stuinfo order by sid desc;
```



### 5.事务

```mysql
什么是事务?
1.事务是一个不可拆分的工作单元;
2.事务是作为一个整体向系统提交的,要么一起执行,要么一起不执行;
3.事务是不支持嵌套的
```

### (1)事务的特性

```mysql
1.原子性:不可拆分
2.一致性:要么一起执行,要么一起不执行
3.隔离性:事务彼此没关系
4.永久性:一旦执行成功,不可修改
```

```mysql
#事务先要开启
start transaction;
#语句
insert into stuinfo values(null,'百强',1,18,'黑龙江');
insert into stuinfo values(null,'百强1',2,18,'黑龙江');
insert into stuinfo values(null,'百强2',3,18,'黑龙江');
#不成功回滚
rollback;
#成功->提交
commit;

#注意
事务只能在innodb引擎下使用
```

### (2)自动提交事务 

```mysql
#查看自动提交事务是否开启
show variables like 'autocommit';

#如果是关的
set autocommit=0|1
```



## 6.索引

```mysql
优点:加快了mysql的查找速度
缺点:
1.更多的储存空间来储存索引字段名
2.myisam使得insert,update,delete的速度变慢了(查询操作占用90%,cud操作加起来占用10%的操作还未必能达到)
#如果一张表中的索引过多，比如我有50个字段，我给每一个字段都添加一个索引

```

### (1)创建索引的原则

```mysql
#适合
1.用于频繁查找的列(字段)
2.用于条件判断的列(字段)
3.用于排序的列(字段)
#不适合
1.列中的数据并不多
2.表中的数据量很小
```

### (2)索引的类型

```mysql
1.普通索引
create index isex on stuinfo(sex);

alter table stuinfo add index isname(sname);

```

```mysql
2.唯一索引
unique
#创建方法如上
```

```mysql
3.主键索引
#是最快的
primary key
#创建方法如上
```

```mysql
4.全文索引
#xunsearch是一种工具

Fulltext key
只能在myisam表引擎下使用(innodb,myisam创建的话都能创建,但是innodb中无效),使用like的时候提升效率.#  where nama like '%你%';
create FULLTEXT KEY zu on stuinfo(age,city);
#myisam 不支持事务
```

```mysql
5.创建多列索引(组合索引)
create index zu on stuinfo(age,city);
alter table stuinfo add index isname(sname,city);
```

### (3)删除索引

```mysql
drop index zu on stuinfo;
```

```mysql
#mysql优化

#面试问： insert 插入的时候一般都是一次插入一条
#那么在插入10000条数据的时候，一般想到的是循环
#插入数据步骤：  mysql先连接，在选库，再插入，进行语法分析，进行表对应，插入数据，断开连接  10000次
#for 循环拼接insert sql 语句，mysql先连接。



innodb=>执行 insert(多条) update delete 非常快
myisam=>执行 insert(单次) select  非常快     #查询非常快，但是极少用到


#分表 100w user1 id(1) user2(id 50w)
#分库 分的数据库 每个公司会有很多项目 通过约定值 
#分机器 主从复制

1.mysql需要搭建在远程的服务器中
2.1mysql台服务器中的所有表类型全部是innodb,其它4台服务器中的表全市myisam的

主从复制(一主多从)(双主多从)
master(主的mysql服务器 innodb) IO
#从服务器监听主服务器
slave(从服务器是myisam)  10.11.58.1 () IO
slave(从服务器是myisam)  10.11.58.2
slave(从服务器是myisam)
slave(从服务器是myisam)

从服务器(myisam)sub监听主服务器

监听什么?
ip地址
干吗了?
主服务器插入,修改,删除一条,从服务器插入,修改,删除一条.

从服务器主要是用来查询的.


innodb 和myisam有什么区别吗?
表文件,数据存储方式不同.
myisam 3个文件 .frm 储存结构， .MYI  .MYD
innodb 初始是两个文件，.frm（结构和索引） .idb(理论上无限多)

innodb可以使用外键,事务,唯一键，行锁，表锁
myisam可以使用全文索引，表锁

mysql8.0  innodb不论是io,都很强，相互监听 


mysql怎么优化? IO
添加索引,常用被查询的,数据量大的
分表: 垂直分表和水平分表
垂直分表是分字段
水平分表是分数据的数量

字段越多，运行速度越慢。

数据库分库,主从

核心优化方法：
硬件方面考虑,固态硬盘比机械强
```











































