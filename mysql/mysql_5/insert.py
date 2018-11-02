import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='python')
cursor = conn.cursor()
effect_row = cursor.executemany("insert into stuinfo(sname,sex,age,city,seat) values(%s,%s,%s,%s,%s);",[('jey1',1,12,'abc',20)])
# conn.rollback()
conn.commit()
# 获取自增id
# new_id = cursor.lastrowid
# print(new_id)
cursor.close()
conn.close()