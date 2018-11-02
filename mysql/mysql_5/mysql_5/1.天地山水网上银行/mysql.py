import pymysql
import config
class MySql:

    def __init__(self):
       self.db = pymysql.connect(
           host=config.HOST,
           port=config.PORT,
           user=config.USER,
           passwd=config.PASSWD,
           db=config.DB,
           charset=config.CHARSET
        )
       self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def query(self,sql="select 0 from dual;",data=()):
        try:
            self.cursor.execute(sql,data)
            self.db.commit()
            return '事务提交成功:%s' % self.cursor.rowcount
        except Exception as e:
            self.db.rollback()
            return "事务提交失败:%s"%e

