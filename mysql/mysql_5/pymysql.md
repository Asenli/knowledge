## python使用pymysql

**一、安装**

```python
pip3 install pymysql
```

**二、使用操作**

```python
import pymysql
  
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='python', charset='utf8')

# 创建游标
cursor = conn.cursor()

'''
cursor中还没有数据，只有等到fetchone()或fetchall()的时候才返回一个元组tuple，才支持len()和index()操作，这也是它是迭代器的原因。但同时为什么说它是生成器呢？因为cursor只能用一次，即每用完一次之后记录其位置，等到下次再取的时候是从游标处再取而不是从头再来，而且fetch完所有的数据之后，这个cursor将不再有使用价值了，即不再能fetch到数据了。
'''

mysql的游标详细看:https://blog.csdn.net/xushouwei/article/details/52201360


# 执行SQL，并返回受影响行数
effect_row = cursor.execute("select * from stuinfo")

# 执行SQL，并返回受影响行数
#effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
#effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])

# 提交，不然无法保存新建或者修改的数据
#conn.commit()

# 关闭游标
cursor.close()


# 关闭连接
conn.close()
```



**获取查询数据**

```python
import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1')
cursor = conn.cursor()
cursor.execute("select * from tb7")

#将游标的数据返回类型设置为字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
 
# 获取结果的第一行数据
row_1 = cursor.fetchone()
print(row_1)
# 获取剩余结果前n行数据
# row_2 = cursor.fetchmany(3)
 
# 获取剩余结果所有数据
# row_3 = cursor.fetchall()
 
conn.commit()
cursor.close()
conn.close()
```

**获取新创建数据自增ID**

可以获取到最新自增的ID，也就是最后插入的一条数据ID

```python
import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1')
cursor = conn.cursor()
effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u3","u3pass","11113"),("u4","u4pass","22224")])
conn.commit()
cursor.close()
conn.close()
#获取自增id
new_id = cursor.lastrowid      
print new_id
```

**4、移动游标**

操作都是靠游标，那对游标的控制也是必须的

```python
注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
 
cursor.scroll(1,mode='relative') # 相对当前位置移动
cursor.scroll(2,mode='absolute') # 相对绝对位置移动
```

**5、fetch数据类型**

关于默认获取的数据是元祖类型，如果想要或者字典类型的数据，即：

```python
import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1')
#游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select * from tb7")
 
row_1 = cursor.fetchone()
print row_1　　#{u'licnese': 213, u'user': '123', u'nid': 10, u'pass': '213'}
 
conn.commit()
cursor.close()
conn.close()
```

**6、调用存储过程**

a、调用无参存储过程

```python
 import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1')
#游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#无参数存储过程
cursor.callproc('p2')  #等价于cursor.execute("call p2()")
 
row_1 = cursor.fetchone()
print row_1
 
 
conn.commit()
cursor.close()
conn.close()
```



b、调用有参存储过程

```python
import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
 
cursor.callproc('p1', args=(1, 22, 3, 4))
#获取执行完存储的参数,参数@开头
cursor.execute("select @p1,@_p1_1,@_p1_2,@_p1_3")  #{u'@_p1_1': 22, u'@p1': None, u'@_p1_2': 103, u'@_p1_3': 24}
row_1 = cursor.fetchone()
print row_1
 
 
conn.commit()
cursor.close()
conn.close()
```

**三、关于pymysql防注入**

2、字符串拼接查询，造成注入

```python

import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1')
cursor = conn.cursor()
 
user="abc' or '1'-- "
passwd="u1pass"
sql="select user,pass from tb7 where user='%s' and pass='%s'" % (user,passwd)
 
#拼接语句被构造成下面这样，永真条件，此时就注入成功了。因此要避免这种情况需使用pymysql提供的参数化查询。
#select user,pass from tb7 where user='u1' or '1'-- ' and pass='u1pass'
 
row_count=cursor.execute(sql)
row_1 = cursor.fetchone()
print row_count,row_1
 
 
conn.commit()
cursor.close()
conn.close()
```



2、避免注入，使用pymysql提供的参数化语句



```python
#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "TKQ"
import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1')
cursor = conn.cursor()
 
user="u1' or '1'-- "
passwd="u1pass"
#执行参数化查询
row_count=cursor.execute("select user,pass from tb7 where user=%s and pass=%s",(user,passwd))
#内部执行参数化生成的SQL语句，对特殊字符进行了加\转义，避免注入语句生成。
# sql=cursor.mogrify("select user,pass from tb7 where user=%s and pass=%s",(user,passwd))
# print sql
#select user,pass from tb7 where user='u1\' or \'1\'-- ' and pass='u1pass'被转义的语句。
 
row_1 = cursor.fetchone()
print row_count,row_1
 
conn.commit()
cursor.close()
conn.close()
```

