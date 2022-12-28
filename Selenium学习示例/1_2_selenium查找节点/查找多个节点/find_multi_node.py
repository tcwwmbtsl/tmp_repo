#!/usr/bin/env python
# coding=utf-8


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get('https://www.jd.com')
    # 查找所有节点名为 li 的节点
    input = browser.find_elements(By.TAG_NAME, 'li')
    # 输出节点本身
    #print(input)
    # 输出所有符合条件的节点数
    print(len(input))
    # 输出第一个符合条件的节点的文本
    print(input[0].text)
    browser.close()
    time.sleep(360)
except Exception as e:
    pass