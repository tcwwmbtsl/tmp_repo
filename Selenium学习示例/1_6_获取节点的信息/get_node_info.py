#!/usr/bin/env python
# coding=utf-8


import time 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()

# 添加参数，不让 Chrome 浏览器显示，只在后台运行
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)

browser.get('https://www.jd.com')
# 查找页面中 id 属性值为 navitems-group1 的第1个节点，是一个 ul 节点
ul = browser.find_element(By.ID, 'navitems-group1')
# 输出节点文本
print(ul.text)
# 输出节点内部使用的id, 注意不是 id 属性值
print('id=', ul.id)
# 输出节点的位置（相对于页面的绝对坐标）
print('location=', ul.location)
# 输出节点的名称
print('tag_name=', ul.tag_name)
# 输出节点的尺寸 宽度和高度
print('size=', ul.size)
# 搜索该节点内的所有名为 li 的子节点
li_list = ul.find_elements(By.TAG_NAME, 'li')
for li in li_list:
    # 输出 li 的类型
    print(type(li))
    # 输出 li 节点的文本和class 属性值，如果属性没找到，返回None
    print('<',li.text,'>', 'class=', li.get_attribute('class'))
    # 查找 li 节点内的名为 a 的子节点
    a = li.find_element(By.TAG_NAME, 'a')
    # 输出 a 节点的 href 属性值
    print('href=', a.get_attribute("href"))
    


