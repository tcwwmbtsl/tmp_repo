#!/usr/bin/env python
# coding=utf-8

import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.jd.com')
# 将京东商城首页滚动到最底端
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# 弹出对话框
browser.execute_async_script('alert("已到页面底端")')

time.sleep(40)
