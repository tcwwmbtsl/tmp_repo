#!/usr/bin/env python
# coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    # 打开 demo.html
    browser.get('http://localhost/demo.html')
    # 通过 id 属性查找姓名 input 节点
    input = browser.find_element(By.ID, 'name')
    # 自动输入 王军
    input.send_keys('王军')
    # 通过 id 属性查找年龄 input 节点
    age = browser.find_element(By.ID, 'age')
    # 自动输入 30
    age.send_keys('30')
    # 通过 name 属性查找国家 input 节点
    country = browser.find_element(By.NAME, '国家')
    # 自动输入 中国
    country.send_keys('中国')
    
    # 通过 class 属性查找收入 input 节点
    seleary = browser.find_element(By.CLASS_NAME, 'myclass')
    # 自动输入 4000
    seleary.send_keys('4000')
    #　注想要覆盖前面的输入，需要在输入前清空节点
    seleary.clear()
    seleary.send_keys('5000')
except Exception as e:
    print(e)
    browser.close()