
# DJANGO使用指南

>Auth: 李东兵
>
>Data：2018-04-21
>
>Email：634163114@qq.com
>
>github：https://github.com/Asenli/knowledge

---

### Django简介：
[Django官网地址](https://www.djangoproject.com/)
[Django中文文档](https://docs.djangoproject.com/zh-hans/2.0/)
Django发布于2005年7月，是当前Python世界里最有名且成熟的网络框架。 最初是被开发用于管理劳伦斯出版集团旗下的以新闻内容为主的网站的，即CMS(内容管理系统)软件。

Django是一个用Python编写的开放源代码的Web应用框架，代码是开源的。此系统采用了MVC的框架模式, 也可以称为MTV模式

***

#### 什么是MVC模式

MVC全名是Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。MVC被独特的发展起来用于映射传统的输入、处理和输出功能在一个逻辑的图形化用户界面的结构中。 <b>通俗的来讲就是，强制性的使应用程序的输入，处理和输出分开。</b>

<b>核心思想</b>：解耦

<b>优点</b>：减低各个模块之间的耦合性，方便变更，更容易重构代码，最大程度的实现了代码的重用

MVC(Model, View, Controller)
Model: 即<font color=red>数据存取层</font>。用于封装于应用程序的业务逻辑相关的数据，以及对数据的处理。说白了就是模型对象负责在数据库中存取数据

View: 即<font color=red>表现层</font>。负责数据的显示和呈现。渲染的html页面给用户，或者返回数据给用户。

Controller: 即<font color=red>业务逻辑层</font>。负责从用户端收集用户的输入，进行业务逻辑处理，包括向模型中发送数据，进行CRUD操作。

图解：
<br>
![图](images/mvc.jpg)

浏览器中MVC的表现形式图解:
<br>
![图](images/mvc_request_response.png)

***

#### Django的模式简介

###### MVT模式

严格来说，Django的模式应该是MVT模式，本质上和MVC没什么区别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同。

Model： 负责业务与数据库(ORM)的对象

View： 负责业务逻辑并适当调用Model和Template

Template: 负责把页面渲染展示给用户

注意： Django中还有一个url分发器，也叫作路由。主要用于将url请求发送给不同的View处理，View在进行相关的业务逻辑处理。







