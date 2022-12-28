#!/usr/bin/env python
# coding=utf-8

import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

try:
    browser.get('https://www.jd.com')
    # 在输入框架中输入 电脑
    input = browser.find_element(By.ID, 'key')
    input.send_keys('电脑')
    # 并进行点击
    clic = browser.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button/i')
    # 点击交互节点
    clic.click()
    time.sleep(360)
except Exception as e:
    print(e)