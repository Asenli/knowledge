import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='python',charset='utf8')
cursor = conn.cursor()

user = "'or 1=1 -- '"
passwd = "u1pass"
# sql = "select * from stuinfo where sid='%s' and sname='%s'" % (user, passwd)
# sql = "select * from stuinfo"
# 拼接语句被构造成下面这样，永真条件，此时就注入成功了。因此要避免这种情况需使用pymysql提供的参数化查询。
# select user,pass from tb7 where user='u1' or '1'-- ' and pass='u1pass'

row_count = cursor.execute("select * from stuinfo where sid='%s' and sname='%s'",(user,passwd))
row_all = cursor.fetchall()
print(row_all)


cursor.close()
conn.close()