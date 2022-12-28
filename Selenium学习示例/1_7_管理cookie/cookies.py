#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.jd.com')
# 获取 cookie 列表
print(browser.get_cookies())
# 添加新的Cookies 
data = {
    'name':'name',
    'value':'lei',
    'domain':"www.jd.com"
}
browser.add_cookie(data)
print(browser.get_cookies())
# 删除所有的 Cookie 
browser.delete_all_cookies()
print(browser.get_cookies())