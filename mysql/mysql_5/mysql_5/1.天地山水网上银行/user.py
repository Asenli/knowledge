import os,pickle
import mysql
class User:

    def __init__(self):
       self.db = mysql.MySql()

    def login(self):
        import main
        print('***********************进入登陆界面****************************')
        username = input('请输入您的帐号:')
        #sql语句
        sql="select * from users where username=%s;"
        #执行sql语句
        self.db.query(sql=sql,data=username,)
        res = self.db.cursor.fetchone()
        print(res,res['uid'])
        if res:
            pass
        else:
            print('您的帐号未注册')
            # main.one()

        password = input('请输入您的密码:')
        #123456  userinfo[admin] = 123456

        if password == res['password']:
            #密码正确就登陆了,改变登陆的状态
            sql = "update users set status=1 where uid=%s;"
            self.db.query(sql=sql, data=str(res['uid']), )
            #登陆成功以后返回到主菜单
            main.one()
        elif password == 'q':
            main.one()
        else:
            password = input('密码错误,请重新输入,不想干了按q:')


    def  register(self):
        import main
        print('***********************进入注册界面****************************')
        #我过一会要获取所用的用户信息,用来判断该帐号是否被注册过
        usm = input('请输入您的注册用户名:')

        # sql = "select * from users where username=%s;"
        # self.db.query(sql=sql, data=usm, )
        # res = self.db.cursor.fetchone()
        #
        # while True:
        #     if res:
        #         # 如果usm 在 userinfo这个字典中,表示已经被注册了
        #         usm = input('您输入的用户名已被使用,请重新输入:')
        #     else:
        #         #如果输入的帐号没被注册,那么就跳出死循环
        #         break

        pwd  = input('请输入您的密码:')
        pwdto = input('请确认您的密码:')

        while True:
            #如果两次密码输入一致,退出死循环
            #123456  == 123456
            if pwd == pwdto:
                break
            elif pwdto == 'q':
                main.one()
            else:
                pwdto = input('两次密码输入不一致,请重新输入,输入q退出:')
                #我以前有一个帐号,密码忘记了,我不想找会,我就注册一个新的,但是注册了一般,我想起来了.

        #创建用户
        isql = "insert into users values(null,%s,%s,0);"
        result= self.db.query(sql=isql, data=(usm,pwd))
        print(result)

        print('恭喜您注册成功!Y(*^_^*)Y')
        main.one()



































