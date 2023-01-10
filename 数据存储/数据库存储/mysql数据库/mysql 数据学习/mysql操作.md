### 登入客户端操作
1、连接mysql 服务端命令
mysql -uroot -p
2、显示当前时间
select now();
3、退出
exit quit Ctrl+D
### 数据库操作
1、查看所有数据库
show databases;
2、创建数据库
create database 数据库名称 charset=utf8;
3、使用数据库
use 数据库名称;
4、查看当前使用的数据库
select database();
5、删除数据库
drop database 数据库名称;
### mysql 表操作
1、查看当前库中所有表
show tables;
2、创建表
create table 表名(字段名称 数据类型 可选的约束条件..);
3、修改表字段类型
alter table 表名 modify 列名 类型 约束;
4、删除表
drop table 表名;
5、查看表结构
desc 表名;
### mysql crud 操作
1、查询数据
    - 查询所有列
        select * from 表名;
    - 查询指定列
        select 列1,列2, ... from 表名;
2、增加数据
    - 全列插入
        值的顺序必须和字段顺序完全一致
        insert info 表名 values(...);
    - 部分列插入 
        值的顺序和给出的列的顺序对应
        insert into 表名(列1) values (值1)；
    - 多行全列插入
        insert info 表名 values(),(),();
    - 部分列多行插入
        insert info 表名(列1, 列2) values(),(),();
3、 修改数据
update 表名 set 列1=值1， 列2=值 where 条件；
4、删除数据
delete from 表名 where 条件;
物理删除、逻辑删除
### 数据备份和导出
需要退出mysql客户端
备份导出-语法
    mysqldump -u用户名 -p密码 数据库名字 表名字 > data.sql;
恢复导入-语法
    cd 数据文件路径下
    登录数据库
    use 数据库
    source data.sql;

