#centos6.8

#安装CentOS 6.8

第一步

```
>>>>Install or upgrade an existing system #安装或升级现有的系统

install system with basic video driver #安装过程中采用基本的显卡驱动

Rescue installed system #进入系统修复模式

Boot from local drive #退出安装从硬盘启动

Memory test #内存检测
```
第二步

```python

这里选择第一项，安装或升级现有的系统，回车。

出现是否对CD媒体进行测试的提问，这里选择“Skip”跳过测试。
```
第三步

```python
选择NEXT
```
第四步

```python
选择中文
```
第五步

```python
选择键盘
选择美国英语式
```
第六步

```python
选择基本存储设备
```
第七步

```python
是，忽略所有的设备
```
第八步

```python
修改主机名称
```

第九步

```python
选择时区 亚洲上海
```

第十步

```python
输入root用户密码，至少是六位

#如果提示密码过于简单，那么就无论如何都要使用
```

第十一步

```python
选择使用所有空间

#将修改写入磁盘
```
#配置网卡
vim /etc/sysconfig/network-scripts/ifcfg-eth0
修改这个文件，将  ONBOOT=no   将no修改为yes

重启网卡
service network restart

​	

#配置yum源
常见的yum源：
网易源，清华源，阿里源，搜狐源，中科大源

配置yum源

cd /etc/yum.repos.d/


mv CentOS-Base.repo CentOS-Base.repo.back

curl -O http://mirrors.aliyun.com/repo/Centos-6.repo

curl -O http://mirrors.163.com/.help/CentOS6-Base-163.repo


mv CentOS6-Base-163.repo CentOS-Base.repo
​		
配置好之后
yum clean all    清空所有
yum makecache    生成缓存