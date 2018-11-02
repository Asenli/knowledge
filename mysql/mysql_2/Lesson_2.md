# Lesson_2

## MySql-2

### 1.1字符集

字符集：可见字符在保存和传输的时候对应的二进制代码集合。

字符集在两个地方用到

```mysql
1.保存数据
2.数据传输
```

### 1.2在存续时使用字符集

```mysql
1、MySQL可以在服务器上、数据库、表、字段上指定字符编码
2、在服务器上指定字符编码是安装服务器的时候指定的
3、数据库、表、字段上是创建时候指定的
```

```mysql
create table test(
-> name varchar(10) charset utf8
->)charset=gbk;
```

### 1.3  gbk,gb2312,utf8的区别

这三种都是常用的字符编码方式，gbk和gb2312(自带)是简体中文的编码，utf8是国际通用编码。

Python、MySQL、jQuery等等都是开源的产品，开源产品建议使用utf8编码

gbk和gb2312都是简体中文，但是内部编码方式是不一样的。

在python中

```mysql
在gbk或gb2312下，一个中文占用2个字节
在utf8下，一个中文占用3个字节
```

```python
注意:在数据库中如果字符编码是utf8的，一个汉字字符长度就是1，gbk一个汉字的字节长度是2。
```

```mysql
create table `emp`(
sex varchar(21844)
)engine=myisam charset=utf8;

65535/3-1


create table `emp2`(
sex varchar(32766)
)engine=myisam charset=gbk;

65535/2-1
```

```mysql
数据库如果是UTF8,那么你在此库中建立的'表'如果没有设定字符集,默认使用数据库的字符集
```

 ![图片1](images\图片1.png)



### 1.4 在传输的时候字符编码

 ![图片2](images\图片2.png)

 ![图片3](images\图片3.png)

mysql服务器接受的编码

```mysql
mysql> show variables like 'character_%';
+--------------------------+-----------------------------------------------+
| Variable_name            | Value                                         |
+--------------------------+-----------------------------------------------+
| character_set_client     | utf8  #服务器接受客户端的字符码                 |
| character_set_connection | utf8                                          |
| character_set_database   | gbk                                           |
| character_set_filesystem | binary                                        |
| character_set_results    | utf8  #返回结果的字符编码                       |
| character_set_server     | utf8                                          |
| character_set_system     | utf8                                          |
| character_sets_dir       | C:\phpStudy\PHPTutorial\MySQL\share\charsets\ |
+--------------------------+-----------------------------------------------+
8 rows in set (0.00 sec)
```

现在客户端发送的编码和服务器接受的编码不一致

```mysql
解决:
#windows默认的是GBK
set character_set_client=gbk;

字符编码不一样返回的就不一样
返回的是utf8   windows不认识会乱码

解决:
set character_set_results=gbk;

小技巧:
set names gbk; ->set names 可以一次设置修改3个字符编码;

mysql> show variables like 'character_%';
+--------------------------+-----------------------------------------------+
| Variable_name            | Value                                         |
+--------------------------+-----------------------------------------------+
| character_set_client     | gbk                                           |
| character_set_connection | gbk                                           |
| character_set_database   | gbk                                           |
| character_set_filesystem | binary                                        |
| character_set_results    | gbk                                           |
| character_set_server     | utf8                                          |
| character_set_system     | utf8                                          |
| character_sets_dir       | C:\phpStudy\PHPTutorial\MySQL\share\charsets\ |
+--------------------------+-----------------------------------------------+
8 rows in set (0.00 sec)
```





### 2校对集

在某种字符集下，字符和字符的关系成为校对集。比如(ASCII)a和B的大小关系，如果区分大小写a>B，如果不区分大小写a<B

不同的校对集的比较规则不一样。

在定义表的时候可以指定校对集

```mysql
#utf8_general_ci  使用_ci这种校对集不区分大小写
create table t1(
name char(1)
)charset=utf8 collate=utf8_general_ci;

create table t2(
name char(1)
)charset=utf8 collate=utf8_bin;

insert into t1 values ('a'),('B');
insert into t2 values ('a'),('B');
```

```mysql
mysql> select * from t1 order by name;
+------+
| name |
+------+
| a    |
| B    |
+------+
2 rows in set (0.00 sec)

#排序查询以后没有区分大小写说明a和b不区分大小写;
```

```mysql
mysql> select * from t2 order by name;
+------+
| name |
+------+
| B    |
| a    |
+------+
2 rows in set (0.00 sec)

#按照正序排列,对照ASCLL编码,B<a,B在a前面那么这种二进制校对集区分大小写;
```

```mysql
牢记:
_bin：按二进制编码比较
_ci：不区分大小写比较
```

```mysql
#显示所有的字符集

mysql> show character set;
+----------+-----------------------------+---------------------+--------+
| Charset  | Description                 | Default collation   | Maxlen |
+----------+-----------------------------+---------------------+--------+
| big5     | Big5 Traditional Chinese    | big5_chinese_ci     |      2 |
| dec8     | DEC West European           | dec8_swedish_ci     |      1 |
| cp850    | DOS West European           | cp850_general_ci    |      1 |
| hp8      | HP West European            | hp8_english_ci      |      1 |
| koi8r    | KOI8-R Relcom Russian       | koi8r_general_ci    |      1 |
| latin1   | cp1252 West European        | latin1_swedish_ci   |      1 |
| latin2   | ISO 8859-2 Central European | latin2_general_ci   |      1 |
| swe7     | 7bit Swedish                | swe7_swedish_ci     |      1 |
| ascii    | US ASCII                    | ascii_general_ci    |      1 |
| ujis     | EUC-JP Japanese             | ujis_japanese_ci    |      3 |
| sjis     | Shift-JIS Japanese          | sjis_japanese_ci    |      2 |
| hebrew   | ISO 8859-8 Hebrew           | hebrew_general_ci   |      1 |
| tis620   | TIS620 Thai                 | tis620_thai_ci      |      1 |
| euckr    | EUC-KR Korean               | euckr_korean_ci     |      2 |
| koi8u    | KOI8-U Ukrainian            | koi8u_general_ci    |      1 |
| gb2312   | GB2312 Simplified Chinese   | gb2312_chinese_ci   |      2 |
| greek    | ISO 8859-7 Greek            | greek_general_ci    |      1 |
| cp1250   | Windows Central European    | cp1250_general_ci   |      1 |
| gbk      | GBK Simplified Chinese      | gbk_chinese_ci      |      2 |
| latin5   | ISO 8859-9 Turkish          | latin5_turkish_ci   |      1 |
| armscii8 | ARMSCII-8 Armenian          | armscii8_general_ci |      1 |
| utf8     | UTF-8 Unicode               | utf8_general_ci     |      3 |
| ucs2     | UCS-2 Unicode               | ucs2_general_ci     |      2 |
| cp866    | DOS Russian                 | cp866_general_ci    |      1 |
| keybcs2  | DOS Kamenicky Czech-Slovak  | keybcs2_general_ci  |      1 |
| macce    | Mac Central European        | macce_general_ci    |      1 |
| macroman | Mac West European           | macroman_general_ci |      1 |
| cp852    | DOS Central European        | cp852_general_ci    |      1 |
| latin7   | ISO 8859-13 Baltic          | latin7_general_ci   |      1 |
| utf8mb4  | UTF-8 Unicode               | utf8mb4_general_ci  |      4 |
| cp1251   | Windows Cyrillic            | cp1251_general_ci   |      1 |
| utf16    | UTF-16 Unicode              | utf16_general_ci    |      4 |
| cp1256   | Windows Arabic              | cp1256_general_ci   |      1 |
| cp1257   | Windows Baltic              | cp1257_general_ci   |      1 |
| utf32    | UTF-32 Unicode              | utf32_general_ci    |      4 |
| binary   | Binary pseudo charset       | binary              |      1 |
| geostd8  | GEOSTD8 Georgian            | geostd8_general_ci  |      1 |
| cp932    | SJIS for Windows Japanese   | cp932_japanese_ci   |      2 |
| eucjpms  | UJIS for Windows Japanese   | eucjpms_japanese_ci |      3 |
+----------+-----------------------------+---------------------+--------+
39 rows in set (0.00 sec)
```

```mysql
#显示所有校对集
mysql> show collation;
```



### 3. MySQL的数据类型——值类型

#### (1)整型

| 整型        | 占用字节 | 范围                                       |
| :-------- | ---- | :--------------------------------------- |
| tinyint   | 1    | -2 ^7 ~ 2^7-1   (-128~127)               |
| smallint  | 2    | -2 ^15 ~ 2^15-1   (-32768~32765)         |
| mediumint | 3    | -2 ^23 ~ 2^23-1   (-8388608~8388607)     |
| int       | 4    | -2 ^31~ 2^31-1   (-2147483648~2147483647) |
| bigint    | 8    | -2 ^63 ~ 2^63-1   (太大了)                  |

#### (2)unsigned  (无符号)

一个数是无符号数，那么这个数肯定是非负数

`数据库mysql第一条记录一定是1(起码是),绝对不能是0`



`tinyint unsigned   2^8-1`

无符号数的范围相当于是有符号数的两倍。

```mysql
mysql> create table test1(
    -> age tinyint unsigned
    -> );
Query OK, 0 rows affected (0.00 sec)

mysql> insert into test1 values (128);
Query OK, 1 row affected (0.00 sec)
```

#### (3)显示宽度

整形支持显示宽度，显示宽度就是最小的显示位数，比如int(11)表示最少用11

位数字表示这个数，如果不够用0来做前导。默认情况下显示位数不起作用，必须集合zerofill才起作用

```mysql
create table stu(
id int(5),
age int(5) zerofill
);

#插入测试数据
insert into stu values (1,23),(2,123456);
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from stu;
+------+--------+
| id   | age    |
+------+--------+
|    1 |  00023 |
|    2 | 123456 |    #超过显示宽度5就显示值本身
+------+--------+
```

显示宽度不决定整型的显示大小，只是在值的位置不够的时候用前导0来填充，如果超过显示位数，就不加前导0.显示本身.



#### (4)浮点型

| 浮点型    | 占用字节 | 范围                   |
| ------ | ---- | -------------------- |
| float  | 4    | -3.4E+38 ~ 3.4E+38   |
| double | 8    | -1.8E+308 ~ 1.8E+308 |

```mysql
create table test2(
  num1 float,
  num2 double
  );
insert into test2 values(23.123,2.123);

#float理论上只保留小数点一位,根据实际版本
#double理论上只保留小数点两位, 根据实际版本

insert into test2 values(2.2E2,2.123);
#也支持科学计数法

insert into test2 values(999.999999999999999999999999999,2.123456);
#丢失精度
```

python中我们没有双精度这一类型,float代表浮点数.

#### (5)定点数

```mysql
decimal(M,D),M的最大值是65,D的最大值是30,默认是(10,0)

create table test3(
	num1 float(10,2),
  	num2 decimal(10,2)
	);

insert into test3 values(123.57,1234567.00);
mysql> select * from test3;
+-------------+-------------+
| num1        | num2        |
+-------------+-------------+
| 12345679.00 |      123.57 |
| 12345679.00 | 12346623.57 |
+-------------+-------------+
2 rows in set (0.00 sec)


#定点数可以保留多个小数点位,它在有些情况下也会失去精度.浮点数的执行效率要高于定点数.
#浮点数和定点数都支持 无符号.
```



### 4.MySql的数据类型--字符类型

| 数据类型       | 描述                 |
| ---------- | ------------------ |
| char       | 定长(255)            |
| varchar    | 可变长度(65535)        |
| tinytext   | 2^8-1    (255)     |
| text       | 2^16-1     (65535) |
| mediumtext | 2^24-1             |
| longtext   | 2^32-1             |



```mysql
char(10)和varchar(10)

	相同点:都是不能超过10个字符
	不同点:char你输入5个字符,它还是占用了10个字符
		varchar你输入5个字符,他会返还多于的空间
		char的最大长度是255
		varchar的理论长度是65535
		实际上达不到,我使用的是gbk(mysql中占用2个字符),那么65535/2.
```



```mysql
create table test(
  name varchar(32766)
  )charset=gbk;


#utf8在创建的时候报错了,最多支持21845个字符,因为utf8一个汉字要使用3个字符

create table test(
  name varchar(65535)
  )charset=gbk

#utf8在创建的时候报错了,最多支持32767个字符,因为gbk一个汉字要使用2个字符
```



### 5.MySql数据类型--枚举(enum)

列出一些选项的,单选.

```mysql
create table test(
name varchar(32),
sex enum('男','女','保密')
);

insert into test values('贾乃亮','男');
#插入正常
insert into test values('PGONE','人妖');
#插入报错
```

```mysql
枚举型在数据库内部是通过整型来管理的,第一个值1,第二个值是2,依次向后推

insert into test values('王宝强',1);
insert into test values('刘运斌',3);


枚举型的优点:
1.限制值
2.节省空间
3.运行效率高
思考:已知枚举型占用2个字节,请问最多可以设置多少个枚举值?

2个字节16位,2^16-1,最多可保存65535/2个值
```



### 6.MySql数据类型--集合(set)

列出数据类型,保存多选

```mysql
create table test2(
name varchar(32),
hobby set('吃','睡觉','看书','鉴黄')
);

insert into test2 values('刘运斌','吃,睡觉,鉴黄');
insert into test2 values('刘运斌-2','吃,睡觉,李小璐');
```

```mysql
集合和枚举一样,为每个元素分配一个固定的值,分配方式不一样.
它的管理也是使用整型
集合是这么分配的:
'吃','睡觉','看书','鉴黄'

2^0   2^1    2^2   2^3  如果后面还有依次向后推
保存的时候,把多个值(转换为整型了)加起来,这样值会边的很大(浪费资源)
一个集合他的元素通过一个位表示,有几个集合元素就需要几个位.

思考:已知集合占用8个字节,那么集合能保存多少个选项?
只能保存64个选项.
```

### 7.MySql数据类型--日期时间型

| 数据类型      | 描述         |
| --------- | ---------- |
| date      | 日期,占用8个字节  |
| time      | 时间         |
| datetime  | 日期时间       |
| year      | 年份,占用一个字节  |
| timestamp | 时间戳,占用4个字节 |

#### (1)datetime

```mysql
#格式 年-月-日 时:分:秒
create table test4(
create_at datetime
);

insert into test4 values('2018-01-12 15:00:53');
insert into test4 values(now());#表示的是当前的时间
insert into test4 values('10000-12-31 23:59:59'); #错误
```



#### (2)date

仅表示时间的日期部分

#### (3)time

表示时间部分,也表示时间间隔,范围是-838:59:59 ~ 838:59:59

```mysql
create table test5(
create_at time
);

insert into test5 values('12:12:12');
insert into test5 values('212:12:12');
insert into test5 values('-800:12:12');
insert into test5 values('-839:59:59');  #错误的,超出范围

#time支持以天的方式表示时间间隔
insert into test5 values('10 12:59:59');
```



#### (4)timestamp

从1970年1月1日 00:00:00秒的格林威治时间开始计算,在python中是特殊类型,但在mysql中显示为datatime格式

```mysql
create table test6(
create_at timestamp
);

insert into test6 values(now());
insert into test6 values('2018-01-12 15:43:30');
insert into test6 values('2038-01-19 11:14:07');#这里就是一个节点

\
insert into test6 values('2038-01-19 11:14:08');#超过了4个字节
timestamp在格式上和datetime是一样的,它们的区别在于:
datetime 从1到9999,而timestamp从1970年~2038年.
timestamp占用4个字节,到2038年超过4个字节的长度了.
```



#### (5)year

占用一个字节,只能是255个数,以1900年为基数,范围1900+1 ~ 1900+255.

```mysql
create table test7(
create_at year
);

insert into test7 values(1900);#错误的
insert into test7 values(1901);
insert into test7 values(2155);
insert into test7 values(2156);#错误的,不在范围内
```



### 8.布尔型(boolean)

mysql不支持布尔型,所以用1和0代替.

```mysql
create table test8(
num boolean
);

insert into test8 values(True);
insert into test8 values(1);
insert into test8 values(False);
insert into test8 values(0);
insert into test8 values('A');#错误

布尔型的使用是比较少的,可以用tinyint代替,或者用enum代替
```

### 9.列属性--是否为空(null|not null)

```mysql
create table test9(
id int auto_increment primary key not null comment'主键',
username varchar(64) not null,
pwd char(64) null
);

insert into test9 values(null,'admin','');
insert into test9 values(null,'','');
insert into test9 values(null,null,'');
insert into test9 values(null,'',null);

#空字符串不等于null
```

### 10.列属性--(default)

```mysql
create table test10(
id int auto_increment primary key not null comment'主键',
username varchar(64) not null,
pwd char(64) null default '123456'
);

insert into test10(username) values('admin2');#推荐的SQL语句


create table test11(
age int  default '123456'
);
insert into test11 values(null);
#输入null加插入null,不写是默认
```



### 11.自动增长列

```mysql
auto_increment
字段值默认从1开始,每次递增1,特点:不会有重复的值,主键常用.

友情提示:在mysql中自动增长的列必须作为主键.
自动增长的烈在插入的时候可以输入(null)

被删除的id不能被再次使用:
如果中间的摸个ID值比较大,那么后面插入的id根据最大值依次+1
```



### 12.列属性--主键

```mysql
primary key
主键:主键是唯一的
特点:不能为空,也不能重复
一个表只有一个主键

CREATE TABLE `test12` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`,`num`,`age`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#以上的主键有'3'个,其实一个主键,这个3个字段组成(一个联合主键),在开发中几乎不会被用上
#(教学使用)

create table demo1(
id int auto_increment primary key
);

create table demo2(
id int auto_increment ,
primary key(id)
);

create table demo3(
id int(11) 
);

alter table demo3 add primary key(id);

选择主键的原则:
1.最少性:必须选择单个键作为主键
2.稳定性:作为主键的这个字段最好不要被修改
```

### 13.列属性--唯一键(unique)

特点:不能重复,不能为空

一个表可以有多个唯一键

```mysql
create table test13(
uid int auto_increment primary key,
mobile char(11) unique,
email char(32) unique,
pwd char(32)
);

insert into test13 values(null,'13877776666','this_dog@qq.com','123456');

insert into test13 values(null,'13877776665','this_do@qq.com','123456');

#修改表属性方法添加唯一键
alter table test13 add unique `my`(mobile);

#删除唯一键还是使用删除的方法
alter table test13 drop index mobile;#有别名删除别名,没别名删除字段名
```



### 14.列属性--备注(comment)

```mysql
备注用来给程序员相互交流使用的
有点:起码你能看的动这个字段是用来干吗的.

stauts tinyint comment'描述一个人的状态 1表示死了,2表示活的,0表示半死不活' 
```



### 15.SQL注释

```mysql
python的注释
# 单行注释
'''

''' 多行注释

mysql的注释
# 单行注释
--单行注释

/*注释的内容*/ 多行注释
```

| 用户名    | " or 1=1 #" |
| ------ | ----------- |
| 密    码 |             |

select * from test13 where uname=" " or 1=1  --" " and pwd=" ";

练习

```mysql
#手机号码一般使用什么数据类型储存?
字符型 char(11)
#性别使用什么数据类型?
字符型 (枚举型) 布尔型
#年龄用什么?
整型 tinyint unsigned
#照片用什么?
binary  字符(只保存路径,不保存资源)
varchar()
#工资用什么类型?
decimal 定点型 
#学员的姓名允许为空吗?
不允许
#家庭地址可以为空吗?
最好不可以
#电子邮箱可以为空吗?
对于目前来说有一点分量,随意,最好不用
#考试成绩可以为空?
不允许 default 0 
#在主键列输入的数值,能为空吗?
肯定不能 null当作占位符
#一个表可以有多个主键吗?
不可以
#在一个学校的数据库中,如果这个学校允许学员重名, 班级不允许有重名的,那么把班级和学生的姓名作为组合主键可以吗?
primary key(id,name)
可以,但是不合理
#标识列允许使用字符串类型吗?
可以,但不允许
#表中没有合适的列(字段)作为主键怎么办?
自己添加一个自增长的字段作为主键
```

























