# Lesson_5

# MySql-高级

## 1.存储过程(procedure)

```mysql
语法:
create procedure 存储过程名(参数,…)
begin
	//代码
end//
```

```mysql
注意：存储过程中有很多的SQL语句，SQL语句的后面为了保证语法结构必须要有分号（;），但是默认情况下分号表示客户端代码发送到服务器执行。必须更改结束符
```

```mysql
通过delimiter指令来跟结束符

delimiter // #将结束字符定义为//(原来是;)
```

### (1)创建存储过程

```mysql
#简单的
create procedure pro_1()
select * from stuinfo;
//

#如果存储过程中就一条SQL语句，begin…end两个关键字可以省略。

#调用存储过程
call pro_1()//
```

```mysql
#包涵多条sql语句的
#in代表输入参数,可以省略
create procedure pro_2(in param int)
begin
	select * from stuinfo where sid=param;
	select * from stumarks where sid=param;
end//

#调用
call pro_2(10)//
```

### (2)参数的类别

```mysql
在存储过程中，没有return，如果需要返回值，通过输出参数来实现
在MySQL中，参数分为3类，输入参数（in），输出参数（out）,输入输出参数（inout），默认情况下是是输入参数（in）
```

### (3)删除存储过程

```mysql
语法:drop procedure [if exists] 存储过程名

drop procedure if exists pro_1//
```

### (4)查看存储过程的信息

```mysql
show create procedure pro_2\G
```

### (5)局部变量

```mysql
语法：declare 变量名 数据类型 [初始值]
通过:select ...into…或set命令给变量赋值

例题通过sid查询姓名和年龄
create procedure pro_3(in id int)
begin
	 declare name varchar(10);
     declare sexx char(10);
     select sname,sex into name,sexx from stuinfo where sid=id;
     select name,sexx from dual;
end //
#调用pro_3
call pro_3(10)//

#注意:声明的变量名不能和列名(字段名)同名
```

```mysql
例题:查找同桌
create procedure pro_4(in name varchar(32))
begin
     declare stuseat tinyint;
     select seat into stuseat from stuinfo where sname=name;
     select * from stuinfo where  seat=stuseat+1 or seat=stuseat-1;
end //

#调用

call pro_4('百强')//
```

```mysql
#通过set给变量赋值

create procedure pro_5(in num1 year,in num2 year,in name varchar(32))
begin
	declare num int;
	set num=num2-num1; #得到年龄
	update stuinfo set age=num where sname=name;
	select * from stuinfo where sname = name;
end//

call pro_5(1991,2018,'小力')//
```

### (6)全局变量(用户变量)

```mysql
全局变量前面必须有一个@，全局变量的数据类型取决于变量的值。如果一个全局变量没有赋值，他的数据类型为null。

set @name='百强'//
select * from stuinfo where sname=@name//
```

### (7)系统变量

```mysql
通过两个@开头的都是系统变量

 select @@version from dual//
```

| 系统命令              | 作用      |
| ----------------- | ------- |
| @@version         | 版本号     |
| current_date      | 当前日期    |
| current_time      | 当前时间    |
| current_timestamp | 当前日期和时间 |

### (8)带有输出参数的存储过程

```mysql
#带有out关键字的参数,在存储过程运行结束以后,默认返回
create procedure pro_6(in num int,out result int)
begin
	set result=num*num;
end//

#调用
#@result 接受返回值
call pro_6(6,@result)//
select @result from dual//
```

### (9)带有输入输出参数的存储过程

```mysql
create procedure pro_7(inout num int)
begin
     set num=num*num;
end //

#调用

set @num=10//
call pro_7(@num)//
select @num from dual//
```

## 2.SQL编程(了解)

#### (1) if-elseif-else语句

```mysql
#语法:
if 条件 then
	//代码1
elseif 条件 then
	//代码2
else
	//代码3
end if;
```

```mysql
create procedure pro_8(in grade int)
begin
     if grade=1 then
        select '金牌会员' as '等级';
     elseif grade=2 then
        select '普通会员' as '等级';
     else
         select '游客' as '等级';
     end if;
end //
#调用
call pro_8(3)//
```

#### (2) case-when语句

```mysql
create procedure pro_9(in num int)
begin
     case num
          when 1 then select '杀马特' as '气质';
          when 2 then select '屌丝' as '气质';
          when 3 then select '正常人' as '气质';
          when 4 then select '贵族' as '气质';
          else select '输入不正确' as '气质';
     end case;
end //

call pro_9(0)//
```

```mysql
#显示学员的学号、姓名、性别、语文成绩、等级

select sid,sname,sex,ch,case
       when ch>=90 then '等级A'
       when ch>=80 then '等级B'
       when ch>=70 then '等级C'
       when ch>=60 then '等级D'
       else '等级E'
end as '等级' from stuinfo left join stumarks using(sid)//


select sid,sname,sex,ch from stuinfo left join stumarks using(sid)//

```

### (3)loop循环

```mysql
loop遇到leave退出
create procedure proc(in num int)
begin
     declare total int default 0;
     declare i int default 0;
     sign:loop
         set total=total+i;
         set i=i+1;
         if i>=num then
            leave sign;# leave=break
         end if;
     end loop;
     select total from dual;
end //

call proc(100)//
#如果没有设置标签名,leave loop
#sign是循环名,用于结束循环,可以自己随意取名字
```

### (4)while循环

```mysql
#语法:
while 条件 do
	//代码
end while
```

```mysql
create procedure pro_11(in num int)
begin
     declare total int default 0;
     declare i int default 0;
     while num>=i do
           set total=total+i;
           set i=i+1;
     end while;
     select total from dual;
end //

call pro_11(100)//
```

### (5)repeat循环

```mysql
#语法
repeat
	代码
	until 条件    -- 直重复到条件为true才结束
end repeat
```

```mysql
create procedure pro_12(in num int)
begin
     declare total int default 0;
     declare i int default 0;
     repeat
           set total=total+i;
           set i=i+1;
           until i>num
     end repeat;
     select total from dual;
end //

call pro_12(100)//
```

### (6)leave和iterate

```mysql
leave类似于break，iterate类似于continue
```

```mysql
create procedure pro_13()
begin
     declare i int default 0;
     sign:while i<5 do
           set i=i+1;
           if(i=3) then
                   leave sign;   -- 类似于break
                   #iterate sign;    -- 类似于continue
           end if;
           select i from dual;
     end while;
end //

call pro_13()//
```

## 3.MySql函数

### 内置函数

#### (1).数字类

| 语句                                     | 含义   |
| -------------------------------------- | ---- |
| select rand()  from dual;              | 随机数  |
| select * from stuinfo order by rand(); | 随机排序 |
| select round(5.6);                     | 四舍五入 |
| select ceil(5.3);                      | 向上取整 |
| select floor(5.6);                     | 向下取整 |



#### (2).大小写转换

| 语句                         | 含义   |
| -------------------------- | ---- |
| select  ucase('i am lyb'); | 大写   |
| select lcase('I AM LYB');  | 小写   |

#### (3).截取字符串

| 语句                               | 含义                   |
| -------------------------------- | -------------------- |
| select left('abcdefg',3);        | 截取左边的3位              |
| select right('abcdefg',3);       | 截取右边3位               |
| select substring('abcdefg',2,3); | 从第2位开始取3个字符，起始位置从1开始 |

#### (4).字符串拼接

```mysql
select concat(sid,sname,age,sex,city) from stuinfo;

mysql> select concat(sid,sname,age,sex,city) from stuinfo;
+--------------------------------+
| concat(sid,sname,age,sex,city) |
+--------------------------------+
| 7小明18male上海                      |
| 8小刚20male北京                       |
| 9小强22male重庆                      |
| 10小力23male天津                      |
| 11小丽21female北京                    |
| 12小月20female天津                    |
| 13小yb18male重庆                    |
| 17百强18male黑龙江                      |
| 18百强118male黑龙江                     |
| 19百强218male黑龙江                     |
+--------------------------------+
```

#### (5).coalesce(str1,str2):如果str1不为null则显示str1，否则显示str2

```mysql
select sid,sname,coalesce(ch,'缺考'),coalesce(math,'缺考') from stuinfo left join stumarks using(sid);

mysql> select sid,sname,coalesce(ch,'缺考'),coalesce(math,'缺考') from stuinfo l
eft join stumarks using(sid);
+-----+-------+---------------------+-----------------------+
| sid | sname | coalesce(ch,'缺考') | coalesce(math,'缺考') |
+-----+-------+---------------------+-----------------------+
|  11 | 小丽  | 100                 | 80                    |
|   8 | 小刚  | 60                  | 98                    |
|  10 | 小力  | 50                  | 51                    |
|   9 | 小强  | 67                  | 88                    |
|   7 | 小明  | 88                  | 10                    |
|  12 | 小月  | 96                  | 97                    |
|  17 | 百强  | 缺考                | 缺考                   |
|  18 | 百强1 | 缺考                | 缺考                  |
|  19 | 百强2 | 缺考                | 缺考                  |
+-----+-------+---------------------+-----------------------+
```

#### (6).length(字节长度)、char_length(字符长度)、trim(去两边空格)、repace(替换)

```mysql
select length('千锋');

select char_length('千锋');

select length(trim(' 千锋 '));

select replace('pgone','one','two');
```

#### (7).时间戳

```mysql
select unix_timestamp();
```

#### (8).将时间戳转成当前时间

```mysql
select from_unixtime(unix_timestamp());
```

#### (9).获取当前时间

```mysql
select now(),year(now()),month(now()),day(now()),hour(now()), minute(now()),second(now())\G

#现在时间,年,月,日,时,分,秒
```

#### (10).dayname(),monthname(),dayofyear()

```mysql
select dayname(now()) as `星期`,monthname(now()) as `月份`,dayofyear(now()) as `本年第几天`;
```

#### (11).datediff(结束日期，开始日期)

```mysql
例题计算自己活了多少天
select datediff(now(),'1970-1-1');
```

#### (12).md5():md5加密

```mysql
select md5('@123456.');
```

## 3.自定义函数

```mysql
#语法:
Create function 函数名(形参) returns 返回的数据类型
begin
	//函数体
end
```

```mysql
#第一步
delimiter //

#不带参数的函数
create function myfun() returns varchar(32)
begin
     return '千锋python';
end //

#调用函数
select myfun()//
```

```mysql
#带参数
create function myfun_1(num1 int,num2 int) returns int
begin
     declare num int default 0;
     set num=num1+num2;
     return num;
end //

select myfun_1(100,200)//


#删除函数
drop function myfun_1//
```

## 4.触发器

```mysql
1、触发器是一个特殊的存储过程
2、不需要直接调用，在MySQL自动调用的
3、是一个事务，可以回滚
```

#### (1)触发器的类型(触发事件)

```mysql
1、insert触发器
2、update触发器
3、delete触发器
```

#### (2)创建触发器

```mysql
#语法:
Create trigger 触发器名 触发时间[before|after] 触发事件 on 表名 for each row
Begin
	//代码
end
```

#### (3)new表和old表

```mysql
1、这两个表是个临时表
2、当触发器触发的时候在内存中自己创建，触发器执行完毕后自动销毁
3、他们的表结构和触发器触发的表的结构一样
4、只读，不能修改

stuinfo curd

打开文件,内存中需要加载,会随即分配一个空间用来保存文件的所有数据,->old  6

在新的一轮操作后,内存会生成新的空间,这个空间里面保存了新的数据变化->new 7
```

#### (5)insert触发器

```mysql
#在stuinfo中插入一个值,就会自动在stumarks中插入一条数据
#after insert 表示的是在insert动作执行完毕以后触发
#on stuinfo for each row  针对的stuinfo表,并且可以读取到每一行的变化
#触发器中定义的局部变量不能与表中的字段名一致,否则会发生字段识别问题(识别不出到底是字段,还是变量)
create trigger trig1
after insert on stuinfo for each row
begin
     declare sidno int default 0;
	 declare nch int default 0;
     declare nmath int default 0;
	 declare nseat int default 0;
     set sidno=new.sid;
	 set nseat=new.seat;
     insert into stumarks set sid=sidno,ch=nch,math=nmath,seat=nseat;
end //

insert into stuinfo values(null,'随便','male',20,'合肥',12)//
```

#### (6)update触发器

```mysql
create trigger trig2
after update on stuinfo for each row
begin
	declare sidno int default 0;
    declare seatno int default 0;
	set seatno=new.seat;
	set sidno =new.sid;
	update stumarks set seat=seatno where sid =sidno;
end //

select ((select max(seat) from stuinfo)+1)//
update stuinfo set seat=12 where sid=12//
```

#### (7)delete触发器

```mysql
create trigger trig3
after delete on stuinfo for each row
begin
     declare sidno int default 0;
	 set sidno =old.sid; #删除了新表里面就没有了,只能从老表里面拿
	 delete from stumarks where sid=sidno;
end //

delete from stuinfo where sid =13//

#触发器能做钩子函数
```

#### (8)查看 和 删除 触发器

```mysql
show triggers\G

drop trigger if exists trig1//
```



### ##5.用户管理



```mysql
mysqld --skip--grant--tables
#(5.5最好用)
#--skip--grant--tables 跳过登陆验证(MYSQL服务器开起中)
```

### (1)创建用户

```mysql
语法：create user ‘用户名’@’允许登录的主机地址’  identified by 密码
```

```mysql
#%代表数据库的库名
create user 'ruidong'@'%' identified by '123456';
```

### (2)删除用户

```mysql
语法：drop user 用户
```

```mysql
drop user ruidong;
```

### (3)增加用户权限

```mysql
#将python的所有表的select权限付给ruidong用户
grant select on python.* to 'ruidong'@'%';  

#将所有数据库中所有表的所有权限付给ruidong用户
grant all privileges on *.* to 'ruidong'@'%';

#创建用户并授权
grant all privileges on *.* to 'hal'@'%' identified by '123456' with grant option;

#创建好用户以后,刷新mysql用户权限表
flush privileges ;(linux ,mac)
```

```mysql
revoke select on python.* from 'ruidong'@'%';   #删除select权限
revoke all privileges on *.* from 'ruidong'@'%'; #删除所有权限
```

### (4)mysql57忘记密码

```mysql
1、首先停止mysql服务进程：
service mysqld stop
2.#然后编辑mysql的配置文件my.cnf(如果是windows的话找到my.ini)
vim /etc/my.cnf
3.#找到 [mysqld]这个模块：
#在最后面添加一段代码
skip-grant-tables   ##忽略mysql权限问题，直接登录
#然后保存 :wq!退出
#启动mysql服务：
service mysqld start
```

```mysql
#直接进入mysql数据库：
mysql
#选择mysql数据库
use mysql;
#对user表的root用户进行密码修改
update mysql.user set authentication_string=password('123456') where user='root' and Host = 'localhost';

#特别提醒注意的一点是，新版的mysql数据库下的user表中已经没有Password字段了
#而是将加密后的用户密码存储于authentication_string字段


#执行刷新
 flush privileges;
#exit退出mysql
exit;
#启动服务
service mysqld start
```





























