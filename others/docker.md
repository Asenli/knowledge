环境：centos7 + python3 

安装docker 之前设置docker仓库

`yum install -y yum-utils device-mapper-persistent-data lvm2`

设置yum源

`sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`

安装docker 

`yum install docker-ce`

\#如果这里出错就要删除 /etc 下面一个进入yum.repos.d   进入删除down...的文件

启动docker

`systemctl start docker`

验证docker是否安装成功

`docker run hello-world`

查看docker版本号

 `docker version`

可整体搬迁的运⾏镜像 需要Dockerfile进⾏配置，Dockerfile定义了容器内的环境 

`mkdir docker_test` 

`cd docker_test` 

`vim Dockerfile`

##### 在里面写入

\# Use an official Python runtime as a parent image

FROM python:2.7-slim

\# Set the working directory to /app

WORKDIR /app

\# Copy the current directory contents into the container at /app

ADD . /app

\# Install any needed packages specified in requirements.txt

RUN pip install -i https://pypi.douban.com/simple --trusted-host

pypi.python.org -r requirements.txt

\# Make port 80 available to the world outside this container

EXPOSE 80

\# Define environment variable

ENV NAME World

\# Run app.py when the container launches

CMD ["python", "app.py"]



##### requirements.txt



Flask 

Redis



##### app.py 



from flask import Flask

from redis import Redis, RedisError 

import os 

import socket 

\# Connect to Redis 

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2) 

app = Flask(__name__) 

@app.route("/") 

def hello(): 

try: visits = redis.incr("counter") 

except RedisError: 

visits = "cannot connect to Redis, counter disabled" 

html = "<h3>Hello {name}!</h3>" \

 "<b>Hostname:</b> {hostname}<br/>" \

"<b> "Visits: </b>{visits}" 

return html.format(name=os.getenv("NAME", "world"),

hostname=socket.gethostname(), visits=visits)

​       if __name__ == "__main__": 

​       		app.run(host='0.0.0.0', port=80)



##### 创建docker 镜像 (-t 取⼀个标签名字）

`docker build -t myhello .`

查看docker镜像 

`docker image ls`

重启docker

`service docker restart`

运⾏容器 -p 外⾯端⼝4000映射容器内端⼝80

`docker run -p 4000:80 myhello`

`docker run -d -p 4000:80 myhello`

`docker ps`





停⽌docker

`docker container stop 63ac7fad8ea4`

在docker hub上注册账号 （国内太慢，⽤daocloud替代）

加速器 DaoCloud - 业界领先的容器云平台

Push 镜像到 DaoCloud 镜像仓库

docker 登录 daocloud.io镜像仓库

docker login daocloud.io

给镜像打标签

docker tag <your-image> daocloud.io/carmack_team/<your-image>:<tag>

例⼦： docker tag myhello daocloud.io/carmack_team/myhello:v1

docker image ls

上传镜像

docker push daocloud.io/carmack_team/<your-image>:<tag>

例⼦： docker push daocloud.io/carmack_team/myhello:v1

从服务器拉取镜像并运⾏容器

`docker run -p 4000:80 username/repository:tag`

例⼦： docker run -p 4000:80 daocloud.io/carmack_team/myhello:v1

ps aux |  grep nginx 查看nginx进程