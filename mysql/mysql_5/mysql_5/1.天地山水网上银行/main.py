from view import View
from action import Action
view = View()
def main():
    #remove先不看
    view.rem()
    #第一步
    view.openView()
    #第二步
    view.jumping()
    #第三步
    one()

#为什么把one分出去,因为后续返回主界面的时候需要调用one()
def one():
    view.menuView()
    action = Action()

if __name__ == "__main__":
    main()