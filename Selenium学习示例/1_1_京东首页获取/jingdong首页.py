#!/usr/bin/env python
# coding=utf-8


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)

browser = webdriver.Chrome('./wedriver/chromedriver')
try:
    # 打开京东首页
    browser.get('https://www.jd.com')
    # 根据id 属性的值查找搜索框
    input = browser.find_element(By.ID, 'key')
    # 使用 send_keys 方法向搜索框架输入 Python从菜鸟到高手 的文本
    input.send_keys('Python从菜鸟到高手')
    # 使用 send_keys 方法模拟按下 Enter 键
    input.send_keys(Keys.ENTER)
    # 创建webdriverWait 对象，设置最长等待时间为 4 秒
    wait = WebDriverWait(browser, 4)
    # 等待搜索页面显示(通过找id为 goodsList 的节点判断搜索页面内容是否显示)
    wait.until(ec.presence_of_all_elements_located((By.ID, 'J_goodsList')))
    # 显示搜索页面的标题
    print(browser.title)
    # 显示搜索页面的 URL
    print(browser.current_url)
    # 显示搜索页面的代码
    print(browser.page_source)
    # 关闭浏览器
    #browser.close()
    time.sleep(360)
except Exception as e:
    print(e)
    browser.close()
    