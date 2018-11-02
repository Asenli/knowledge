from user import User
from select import Select
import os


#Action是分配任务的控制器
class Action:

    def __init__(self):
        self.user = User()
        self.select = Select()

        action_list = ['1','2','3','4','5','6','7','8','9','q']
        action = input('请输入你要选择的操作:')

        while True:
            #if action == '1' and action == '2'
            if action in action_list:
                break
            else:
                action = input('请重新输入你要选择的操作:')


        if action == action_list[0]:
            #注册
            self.user.register()
        elif action == action_list[1]:
            #登陆
            self.user.login()
        elif action == action_list[2]:
            #查询余额
            self.select.balance()
        elif action == action_list[3]:
            pass
        elif action == action_list[4]:
            pass
        elif action == action_list[5]:
            pass
        elif action == action_list[6]:
            pass
        elif action == action_list[7]:
            pass
        elif action == action_list[8]:
            pass
        elif action == action_list[9]:
            if not os.path.exists(self.file_path):
                exit()
            else:
                os.remove(self.file_path)
                exit()
























