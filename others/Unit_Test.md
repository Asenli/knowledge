stack.py

```
class Stack(object):
    def __init__(self):
        self.max_size = 5
        self.stack_list = []

    #判断是否为空
    def is_empty(self):
        return self.stack_list == []

    def push(self, item):
        self.stack_list.append(item)
        return self.stack_list

    # 返回栈顶元素
    def peek(self):
        try:
            return self.stack_list[len(self.stack_list) - 1]
        except BaseException as f:
            return f

    def size(self):
        return len(self.stack_list)

    def pop(self):
        try:
            return self.stack_list.pop()
        except BaseException as e:

            return e


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(4)
    my_stack.push(6)
    print(my_stack.size())
    # print(my_stack.peek())
    print(my_stack.is_empty())
```

test_stack.py



```
import unittest
from stack import Stack


class Test_stack(unittest.TestCase):
    def setUp(self):
        # 实例化
        self.test_stack = Stack()

    def tearDown(self):
        pass

    def test_case01(self):
        # 增加一个
        self.test_stack.push(10)
        self.test_stack.push(9)
        print(self.test_stack.stack_list)

    def test_case03(self):
        print(self.test_stack.is_empty() == True)

    def test_case02(self):
        # self.assertEqual(self.test_stack.peek(),4)
        if self.test_stack.peek() == 1:
            print('成功')

    def test_case04(self):
        print(self.test_stack.pop())
        print(self.test_stack.stack_list)

    def test_case05(self):
        print(self.test_stack.push(4) != None)


if __name__ == '__main__':
    unittest.main()
```

##### 测试登录百度账号

```
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
class NewVisitorTest(unittest.TestCase): 
   
   def setUp(self):
      self.timeout = 40
      self.browser = webdriver.Chrome()
      self.browser.set_page_load_timeout(self.timeout)
      self.wait = WebDriverWait(self.browser, self.timeout)

   def tearDown(self):
      pass
      # self.browser.quit()

   def test_can_start_a_list_and_retrieve_it_later(self):
      self.browser.get('https://www.baidu.com')

      self.assertIn('百度', self.browser.title)
      login_link = self.wait.until(
         #By.LINK_TEXT全局检查登录按钮
         EC.element_to_be_clickable((By.LINK_TEXT, '登录')))
      login_link.click()

      login_link_2 = self.wait.until(
         EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_10__footerULoginBtn')))

      login_link_2.click()

      username_input = self.wait.until(
         EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_10__userName')))
      username_input.clear()
      username_input.send_keys('******@163.com')

      password_input = self.wait.until(
         EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_10__password')))
      password_input.clear()
      password_input.send_keys('1112223')


      login_submit_button = self.wait.until(
         EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_10__submit')))
      login_submit_button.click()

      username_span = self.wait.until(
         EC.presence_of_element_located((By.CSS_SELECTOR, '#s_username_top > span')))
      self.assertEqual(username_span.text, 'PebbleApp')

      # user_login_link = self.browser.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
      # user_login_link.click()

if __name__ == '__main__':
   unittest.main(warnings='ignore')
```