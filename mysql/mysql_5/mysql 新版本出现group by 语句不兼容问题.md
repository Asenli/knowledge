# mysql 新版本出现group by 语句不兼容问题



## 1、 具体出错提示：

```basic
[Err] 1055 - Expression #1 of ORDER BY clause is not in GROUP BY clause and contains nonaggregated column 'information_schema.PROFILING.SEQ' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```



### 1.1、查看sql_mode

```basic
select @@global.sql_mode;
```



### 1.2、 查询出来的值为：

```basic
ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
```



## 2、去掉ONLY_FULL_GROUP_BY，重新设置值。

```basic
set    @@global.sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';

```

### 2.1、上面是改变了全局sql_mode，对于新建的数据库有效。对于已存在的数据库，则需要在对应的数据下执行：

```basic
set sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';

```

### 3、：修改my.cnf（windows下是my.ini）配置文件，删掉only_full_group_by这一项

若我们项目的mysql安装在ubuntu上面，找到这个文件打开一看，里面并没有sql_mode这一配置项，想删都没得删。

当然，还有别的办法，打开mysql命令行，执行命令

#### 如果 [mysqld] 这行被注释掉的话记得要打开注释。

```basic
sql_mode=STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
```

# 然后重重启mysql服务