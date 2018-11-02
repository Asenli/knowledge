import os,pickle,time
class Select:

    def balance(self):
        import main

        #当前登陆用户标记
        path = os.getcwd()
        file_name = 'login.txt'
        file_path = os.path.join(path,file_name)

        # 当前登陆用户的存款信息
        money_name = 'money.txt'
        money_path = os.path.join(path,money_name)

        if not os.path.exists(file_path):
            print('请您先登陆')
            main.one()

        #获取当前登陆用户信息
        with open(file_path,'rb') as f:
            loginfo = pickle.load(f)


        with open(money_path,'rb') as f:
            #{lyb:lyb}
            #list(loginfo.keys()) = ['lyb']
            username = list(loginfo.keys())[0]
            money = pickle.load(f)
            bal = money[username]


        usm = list(loginfo.keys())[0]

        view = '''
       *************************************************************
       ** 尊敬的%s用户:                                         **
       **                                                         **
       **                                                         **
       **       您的余额人名币:%d￥                         **
       **                                                         **
       **                                                         **
       **                                                         **
       **                                                         **
       *************************************************************
       '''%(usm,bal)
        print(view)
        action = input('输入q返回主菜单:')

        while True:
            if action != 'q':
                action = input('你个傻帽,按q返回主菜单:')
            else:
                main.one()


        # time.sleep(5)
        # main.one()