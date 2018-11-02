import time,os
class View:
    def openView(self):
        view = '''
        *************************************************************
        **                                                         **
        **                                                         **
        **                                                         **
        **                  欢迎来到天地山水网上银行                 **
        **                                                         **
        **                                                         **
        **                                                         **
        **                                                         **
        *************************************************************
        '''
        print(view)
        time.sleep(1)

    def jumping(self):
        view = '''
       *************************************************************
       **                                                         **
       **                                                         **
       **                                                         **
       **                  即将进入到操作菜单...                   **
       **                                                         **
       **                                                         **
       **                                                         **
       **                                                         **
       *************************************************************
       '''
        print(view)
        time.sleep(1)

        timeEnd = int(time.time()) + 3

        for i in range(3):
            timeNow = int(time.time())
            res = timeEnd - timeNow

            time_view = '''
       *************************************************************
       **                                                         **
       **                                                         **
       **                                                         **
       **                  即将进入到操作菜单...                   **
       **                          %d                             **
       **                                                         **
       **                                                         **
       **                                                         **
       *************************************************************
       '''%res

            print(time_view)
            time.sleep(1)

    def menuView(self):

        view = '''
        *************************************************************
        **                                                         **
        **          (1)注册                     (2)登陆            **
        **          (3)查询                     (4)转账            **
        **          (5)锁卡                     (6)解锁            **
        **          (7)补卡                     (8)销户            **
        **          (9)改密                                        **
        **                        (q)退出                          **
        **                                                         **
        *************************************************************
        '''
        print(view)

    def rem(self):
        # login.txt
        self.path = os.getcwd()
        self.file_name = 'login.txt'
        self.file_path = os.path.join(self.path, self.file_name)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

