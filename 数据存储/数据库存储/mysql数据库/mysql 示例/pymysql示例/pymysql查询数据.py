#!/usr/bin/env python
# coding=utf-8


# 导包
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',
                    user='root', password='1454015651@DS',port=3306, database='python-04',charset='utf8')
# 游标对象
cursor = conn.cursor()
try:
    # 编写SQL语句
    sql_cmd = 'select * from booktest_heroinfo'
    cursor.execute(sql_cmd)
    # 获取查询结果
    row_count = cursor.fetchall()
    for i in row_count:
        print(i)
except Exception as e:
    print(e)
finally:
    # 游标对象关闭
    cursor.close()
    # 数据库关闭
    conn.close()
