#!/usr/bin/env python
# coding=utf-8

# 注：因为需要手机验证码，未能成功实现

import time 
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('headless')


browser = webdriver.Chrome()
browser.maximize_window()

# 获取QQ空间说说的正文和发布时间
def get_info(qq):
    browser.get('http://user.qzone.qq.com/{}/311'.format(qq))
    # 下面的代码用于模拟登录，请填写自己的QQ号和密码
    browser.switch_to.frame('login_frame')
    input = browser.find_element(By.XPATH, '//*[@id="switcher_plogin"]')
    input.click()
    browser.find_element(By.XPATH, '//*[@id="u"]').send_keys(qq)
    browser.find_element(By.XPATH, '//*[@id="p"]').send_keys('1454015651@DS')
    browser.find_element(By.XPATH, '//*[@id="login_button"]').click()
    time.sleep(5)
    browser.switch_to.frame('app_canvas_frame')
    contents = browser.find_elements_by_css_selector('.content')
    times = browser.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
    for content, tim in zip(contents, times):
        data = {
            'time': tim.text,
            'content': content.text
        }
        print(data)
    
    
    time.sleep(50)

if __name__ == "__main__":
    get_info('1454015651')
    
