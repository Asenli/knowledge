环境：centos7 + python3  pip3

安装rabbitmq

`yum install rabbitmq-server`

启动

`systemctl start rabbitmq-server`

`rabbitmq-server -detached`           //启动rabbitmq，-detached代表后台守护进程方式启动

场景 ：给用户发通知邮件

`/sbin/service rabbitmq-server stop`

 `/sbin/service rabbitmq-server start`

`rabbitmqctl status` 测试是否启动成功

`rabbitmqctl add_user lidongbing 123456`   设置用户密码

`rabbitmqctl add_vhost myvhost`     设置host 名为myvhost

`rabbitmqctl set_user_tags lidongbing mytag`

`rabbitmqctl set_permissions -p myvhost lidongbing "." "." ".*"`

`rabbitmqctl list_queues -p myvhost`

#### 安装celery

`pip3 install celery -i https://pypi.douban.com/simple`

创建执行文件tasks.py  写入代码



import time

from celery import Celery

app = Celery('tasks', backend='amqp://lidongbing:123456@localhost:5672/myvhost', broker='amqp://lidongbing:123456@localhost:5672/myvhost')

@app.task

def add(x, y):

​	time.sleep(5)

  	return x + y



##### 再创建client_test.py 执行流程文件  

from tasks import add

result = add.delay(10,4)

print(result.ready())

print(result.get(timeout=5))

print(result.ready())

print(result.status)

##### 运行celery worker

`celery -A tasks worker --loglevel=info`  这条命令就是在前台运行

![img](E:/youdaoyun/Asen634163114@163.com/1d7e943d980645dc84519d114ac214bd/clipboard.png)

`nohup celery -A tasks worker --loglevel=info &`

（nohup  和&是后台运行的意思）

这时候文件目录下应该有两个文件

![img](E:/youdaoyun/Asen634163114@163.com/050e58dcddd546c79377d20e7f527551/clipboard.png)

执行操作

`python3 client_test.py` 

![img](E:/youdaoyun/Asen634163114@163.com/1810b966d3704a56b524612287ec0c1b/clipboard.png)

如果不对，把client_test.py里面的timeout时间改长一点