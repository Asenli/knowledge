1. 检查是否有安装nfs(服务端)

2. ​

   NFS（网络文件系统）


```shell
#先关闭防火墙和seLinux
service firewalld stop
service iptables stop

setenforce 0

rpm -qa|grep nfs

rpm -qa|grep rpcbind
```

若没有这安装nfs-utils和rpcbind

```shell
yum -y install nfs-utils rpcbind
```

2.设置开机启动服务

```shell

chkconfig nfs on 
chkconfig rpcbind on
```

3.启动相关服务

```shell
#启动nfs,需要先启动rpc
#开启顺序 先rpc 后nfs

service rpcbind start 
service nfs start
```

4.创建共享目录

```shell
mkdir /root/nfsdir
```
5.编辑 vim /etc/exports文件添加如下内容

```shell
#/export  nfs 官方指定使用的根目录下的一个共享文件(目录)(可有可无的目录)


#/export目录是干嘛的,这个目录用来共享nfs,但是需要自己创建.
#/export *:(rw,async,no_root_squash,no_subtree_check) 

/root/nfsdir 10.11.58.*(rw,sync,no_root_squash)
```

6.刷新配置立即生效

```shell
exportfs -a
#如果没起作用
service nfs stop
service rpcbind restart 
service nfs start
#关闭防火墙
service iptables stop
```

7.客服端配置

```python
#安装
yum -y install nfs-utils rpcbind

service rpcbind start

service nfs start

mkdir /mnt/nfs1

mount -t nfs 10.11.53.133:/root/nfsdir  /mnt/nfs1
```

