#!/usr/bin/env python
# coding=utf-8


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 查找百度搜索按钮
search_button = driver.find_element(By.ID, 'su')
# 定义搜索按钮可以移动的 x 坐标位置
x_positions = [50, 90, 130, 170]
# 定义搜索按钮可以移动的y坐标的位置，与x 坐标列表中元素的个数要相等
y_positons = [100, 120, 160, 90]
# 迭代位置列表，每隔2秒移动一次搜索按钮
for i in range(len(x_positions)):
    # 用于移动搜索按钮的 JavaScript 代码， arguments[0], 就是搜索按钮对应的DOM
    js = '''
        arguments[0].style.position = 'absolute';
        arguments[0].style.left="{}px";
        arguments[0].style.top="{}px"; 
    '''.format(x_positions[i], y_positons[i])
    # 执行 JavaScript 代码，并开始移动搜索按钮
    driver.execute_script(js, search_button)
    time.sleep(2)