#!/usr/bin/env python
# coding=utf-8


import pymysql


conn = pymysql.connect(host='127.0.0.1',
                    user='root', password='1454015651@DS',port=3306, database='python-04',charset='utf8')
cursor = conn.cursor()
try:
    # 增加数据 'insert into booktest_heroinfo values(18, 袁承志， 1, 金蛇剑法, 4, 0);'
    # sql_cmd1 = 'insert into booktest_heroinfo values(%s, %s, %s, %s, %s, %s)'
    # add_data = [18, '袁承志', 1, '金蛇剑法', 4, 0]
    # cursor.execute(sql_cmd1, add_data)
    # 修改数据 袁承志的名称为小袁承志
    # sql_cmd2 = 'update booktest_heroinfo set hname=%s where id=18'
    # update_data = ['小袁承志']
    # cursor.execute(sql_cmd2, update_data)
    # 删除数据  
    sql_cmd3 = 'delete from booktest_heroinfo where id=%s'
    del_data = [18]
    cursor.execute(sql_cmd3, del_data)
    conn.commit()
except Exception as e:
    conn.rollback()
finally:
    cursor.close()
    conn.close()