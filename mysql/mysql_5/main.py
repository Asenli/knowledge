import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='python', charset='utf8')

# 创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from stuinfo where sname = '小芳'")

# 获取剩余结果的第一行数据
#row_1 = cursor.fetchone()

#获取所有的数据
# row_all = cursor.fetchall();

print(row_all);
cursor.close()
# 关闭连接
conn.close()