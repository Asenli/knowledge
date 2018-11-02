

### hosts 文件位置 C:\Windows\System32\drivers\etc

### win10 先复制到桌面,进行修改,然后在复制回去



### nginx.conf 位置 /usr/local/nginx/conf

```python
  server {
    listen 80;
    server_name _;
    #location / {  把这几行注释掉,默认就是用nginx作为服务器,原来只是作为一个VBS(负载均衡器来使用,也就是反向代理)
    #location / {
    #  try_files $uri @apache;
    #}
    #location @apache {
    #  proxy_pass http://127.0.0.1:88;
    #  include proxy.conf;
    #}
```



#nginx.conf

```nginx
#定义Nginx运行的用户和用户组  
user www www;  
   
#nginx进程数，建议设置为等于CPU总核心数。  
worker_processes auto;  
   
#全局错误日志定义类型，[ debug | info | notice | warn | error | crit ]  
error_log /data/wwwlogs/error_nginx.log crit;
   
#进程文件  
pid /var/run/nginx.pid;
   
#一个nginx进程打开的最多文件描述符数目
worker_rlimit_nofile 65535;  
   
#工作模式与连接数上限  
events  
{  
	#参考事件模型，use [ kqueue | rtsig | epoll | /dev/poll | select | poll ]; epoll模型是Linux 2.6以上版本内核中的高性能网络I/O模型，如果跑在FreeBSD(unix系统)上面，就用kqueue模型。  
	use epoll;  
	#单个进程最大连接数（最大连接数=连接数*进程数）  
	worker_connections 65535;  
	#multi_accept在Nginx接到一个新连接通知后调用accept()来接受尽量多的连接 。off是关闭
	multi_accept on;
}  
   
#设定http服务器  
http  
{  
	include mime.types; #文件扩展名与文件类型映射表  
	default_type application/octet-stream; #默认文件类型  
	charset utf-8; #默认编码  
	server_names_hash_bucket_size 128; #服务器名字的hash表大小  
	client_header_buffer_size 32k; # 客户端头信息缓冲区大小
	large_client_header_buffers 64k; #最大客户端头信息缓冲区大小
	client_max_body_size 8m; #客户端请求的最大文件大小 
	sendfile on; #开启高效文件传输模式，sendfile指令指定nginx是否调用sendfile函数来输出文件，对于普通应用设为 on，如果用来进行下载等应用磁盘IO重负载应用，可设置为off，以平衡磁盘与网络I/O处理速度，降低系统的负载。注意：如果图片显示不正常把这个改成off。  
	autoindex on; #开启目录列表访问  
	tcp_nopush on; #防止网络阻塞  
	tcp_nodelay on; #防止网络阻塞  
	keepalive_timeout 120; #长连接超时时间，单位是秒  

	   
	#gzip模块设置  
	gzip on; #开启gzip压缩输出  
	gzip_min_length 1k; #最小压缩文件大小  
	gzip_buffers 4 16k; #压缩缓冲区  
	gzip_http_version 1.0; #压缩版本（默认1.1，前端如果是squid2.5请使用1.0）  
	gzip_comp_level 2; #压缩等级  
	gzip_types text/plain application/x-javascript text/css application/xml;  
	#压缩类型，默认就已经包含text/html，所以下面就不用再写了  
   
	upstream www.baidu.com {  
		#upstream的负载均衡，weight是权重，可以根据机器配置定义权重。weigth参数表示权值，权值越高被分配到的几率越大。  
    	#hash算法分配
    	#ip_hash
    	#--我是分割线--
		server 192.168.80.121:80 weight=3;  #8核 32G 200M带宽
		server 192.168.80.122:80 weight=2;  #4  16  200M
		server 192.168.80.123:80 weight=1;  #2  4   200M
	}  
   
	#虚拟主机的配置  
	server  
	{  
		#监听端口  
		listen 80;  
		#域名可以有多个，用空格隔开  
		server_name www.baidu.com baidu.com;  

		#先读取的文件类型
		index.html index.htm main.py;  

		#默认的文件路径
		root /data/wwwroot/default;
		
		#404 无法找到文件 显示的样式
		#error_page 404 /404.html;
		
		#502 网关错误 显示的样式
    	#error_page 502 /502.html;

		#图片缓存时间设置  
		location ~ .*.(gif|jpg|jpeg|png|bmp|swf)$  
		{  
			expires 10d;  
		}  
		#JS和CSS缓存时间设置  
		location ~ .*.(js|css)?$  
		{  
			expires 1h;  
		}     
		#定义本虚拟主机的访问日志  
		access_log ar/loginx/hahaaccess.log access;  
		
    	#设置关联apche服务器
    	location / {
     	 try_files $uri @apache;
        }
    	#设置重定向到apache
        location @apache {
      	  #当nginx接收到请求的时候 跳转到本机的127.0.0.1:88端口
          proxy_pass http://127.0.0.1:88;
          include proxy.conf;
        }
    	#让apache去引用php
        location ~ [^/]\.php(/|$) {
          proxy_pass http://127.0.0.1:88;
          include proxy.conf;
        }

		#对 "/" 启用反向代理  
		location / {  
			#接受请求直接指向本机的88端口
			proxy_pass http://127.0.0.1:88;

			#对发送给客户端的URL进行修改  
			proxy_redirect off;  
			#可以设置重新添加请求头
			proxy_set_header X-Real-IP $remote_addr;  
			#后端的Web服务器可以通过X-Forwarded-For获取用户真实IP  
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
			#以下是一些反向代理的配置，可选。  
			proxy_set_header Host $host;  
			client_max_body_size 10m; #允许客户端请求的最大单文件字节数  
			client_body_buffer_size 128k; #缓冲区代理缓冲用户端请求的最大字节数，  
			proxy_connect_timeout 90; #nginx跟后端服务器连接超时时间(代理连接超时)  
			proxy_send_timeout 90; #后端服务器数据回传时间(代理发送超时)  
			proxy_read_timeout 90; #连接成功后，后端服务器响应时间(代理接收超时)  
			proxy_buffer_size 4k; #设置代理服务器（nginx）保存用户头信息的缓冲区大小  
			proxy_buffers 4 32k; #proxy_buffers缓冲区，网页平均在32k以下的设置  
			proxy_busy_buffers_size 64k; #高负荷下缓冲大小（proxy_buffers*2）  
			proxy_temp_file_write_size 64k;  
			#设定缓存文件夹大小，大于这个值，将从upstream服务器传  
		}  
		
		#所有静态文件由nginx直接读取  
		location ~ .*.(htm|html|gif|jpg|jpeg|png|bmp|swf|ioc|rar|zip|txt|flv|mid|doc|ppt|pdf|xls|mp3|wma)$  
		{ expires 15d; }  
		location ~ .*.(js|css)?$  
		{ expires 1h; }  
	} 
	#引入其它的站点位置
	include vhost/*.conf; 
}  
```
include vhost/*.conf;

conf目录中没有 vhost目录，我们可以新建一个，

在conf目中： mkdir vhost

*.conf的名字可以自己取

例如:aliyun.conf   baidu.con


#vim vhost/0.conf

```0.conf

#虚拟主机的配置  
	server  
	{  
		#监听端口  
		listen 127.0.0.1:88;  
		#域名可以有多个，用空格隔开  
		server_name www.taobao.com taobao.com;  

		#先读取的文件类型
		index index.html index.htm main.py;  

		#默认的文件路径
		root /data/wwwroot/project;
		
		#404 无法找到文件 显示的样式
		#error_page 404 /404.html;
		
		#502 网管错误 显示的样式
    		#error_page 502 /502.html;

		#图片缓存时间设置  
		location ~ .*.(gif|jpg|jpeg|png|bmp|swf)$  
		{  
			expires 10d;  
		}  
		#JS和CSS缓存时间设置  
		location ~ .*.(js|css)?$  
		{  
			expires 1h;  
		}     
		#定义本虚拟主机的访问日志  
		access_log ar/loginx/hahaaccess.log access;  
		   
		#对 "/" 启用反向代理  
		location / {  
			#接受请求直接指向本机的88端口
			proxy_pass http://127.0.0.1:8888;

			#对发送给客户端的URL进行修改  
			proxy_redirect off;  
			#可以设置重新添加请求头
			proxy_set_header X-Real-IP $remote_addr;  
			#后端的Web服务器可以通过X-Forwarded-For获取用户真实IP  
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
			#以下是一些反向代理的配置，可选。  
			proxy_set_header Host $host;  
			client_max_body_size 10m; #允许客户端请求的最大单文件字节数  
			client_body_buffer_size 128k; #缓冲区代理缓冲用户端请求的最大字节数，  
			proxy_connect_timeout 90; #nginx跟后端服务器连接超时时间(代理连接超时)  
			proxy_send_timeout 90; #后端服务器数据回传时间(代理发送超时)  
			proxy_read_timeout 90; #连接成功后，后端服务器响应时间(代理接收超时)  
			proxy_buffer_size 4k; #设置代理服务器（nginx）保存用户头信息的缓冲区大小  
			proxy_buffers 4 32k; #proxy_buffers缓冲区，网页平均在32k以下的设置  
			proxy_busy_buffers_size 64k; #高负荷下缓冲大小（proxy_buffers*2）  
			proxy_temp_file_write_size 64k;  
			#设定缓存文件夹大小，大于这个值，将从upstream服务器传  
		}  
		
		#所有静态文件由nginx直接读取  
		location ~ .*.(htm|html|gif|jpg|jpeg|png|bmp|swf|ioc|rar|zip|txt|flv|mid|doc|ppt|pdf|xls|mp3|wma)$  
		{ expires 15d; }  
		location ~ .*.(js|css)?$  
		{ expires 1h; }  
	}  
```