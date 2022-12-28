#!/usr/bin/env python
# coding=utf-8


import time 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    # 切换到 id 属性值为 iframeResult 的 iframe 节点
    browser.switch_to.frame('iframeResult')
    # 使用 css 选择器获取 id 属性值为 draggable 的拖动节点
    source = browser.find_element(By.CSS_SELECTOR, '#draggable')
    # 使用 css 选择器获取 id 属性值为 droppable 的接收点
    target = browser.find_element(By.CSS_SELECTOR, '#droppable')
    # 创建一个ActionChains 对象
    actions = ActionChains(browser)
    # 调用 drap_and_drop 方法拖动节点
    actions.drag_and_drop(source, actions)
    # 调用perform 方法让拖动生效
    actions.perform()
    time.sleep(260)
except Exception as e:
    print(e)
