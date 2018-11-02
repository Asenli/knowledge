import pymysql
'''1
pumysql.connect() #进行连接数据库操作的
host  #MySql服务器的地址
port  #端口号
user  #用户
passwd  #密码
db      #选择的数据库
charset #设置字符集
'''
'''2
connection对象
cursor() #使连接创建并返回游标
commit() #提交当前事务
rollback() #回滚当前事务
close()    #关闭连接
'''
'''3

execute(sql)  #执行mysql命令
fetchone()    #取得结果集的下一行
fetchall()    #取得结果集的所有行
fetchmany(size) #指定取得结果集的几行
rowcount()      #返回数据条数或者影响的行号
close()         #关闭游标对象
'''

#创建mysql服务器连接
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='python',
    charset='utf8'
)
#创建游标对象
#cursor=pymysql.cursors.DictCursor 作用是返回字典类型
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)


#python使用insert,update,delete,默认开启事务,所以execute执行完以后,一定要提交

# sql="select * from stuinfo;"
# #执行sql语句
# cursor.execute(sql)
# #获取返回的结果
# res=cursor.fetchall()
#
# for i in res:
#     print('***********row***************')
#     for key,value in i.items():
#         print(key,':',value)


# sql='''
# create table `users`(
# uid int auto_increment PRIMARY KEY comment'主键',
# username VARCHAR(64) NOT NULL comment'帐号',
# password VARCHAR(64) NOT NULL comment'密码',
# create_at TIMESTAMP NOT NULL comment'创建时间'
# )engine=innodb;
# '''
# cursor.execute(sql)

# sql = "insert into users value(null,'root','123456',now());"
# cursor.execute(sql)
# db.commit()
# print(cursor.rowcount)

# sql = "update users set password=md5(123456) where uid=1;"
# cursor.execute(sql)
# db.commit()
# print(cursor.rowcount)

# sql = "delete from users where uid=2;"
# cursor.execute(sql)
# db.commit()
# print(cursor.rowcount)

# sql1 = "insert into users value(null,'admin1','123456',now());"
# sql2 = "insert into users value(null,'admin2','123456',now());"
# sql3 = "insert into users value(null,'admin3','123456','asd');"
# try:
#     cursor.execute(sql1)
#     cursor.execute(sql2)
#     cursor.execute(sql3)
# except Exception as e:
#     db.rollback()
#     print('事务提交失败:',e)
# else:
#     db.commit()
#     print('事务提交成功:',cursor.rowcount)
# finally:
#     cursor.close()
#     db.close()

# or 1=1;--
#execute这个内置函数自带防sql注入
cursor.execute("select * from users where username=%s and password=%s;",('root','123456'))
res=cursor.fetchall()
print(res)