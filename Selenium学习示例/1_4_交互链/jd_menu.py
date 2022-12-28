#!/usr/bin/env python
# coding=utf-8

# 注： 在调用动作链后，必须调用 perform 才能生效
# move_to_element 方法模拟鼠标移动动作

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()

try:
    browser.get('https://www.jd.com')
    # 创建 ActionChains 对象
    action = ActionChains(browser)
    # 通过 css 选择器查找所有 class 属性值为 cate_menu_item 的li 节点，每一个li 节点是一个二级导航菜单
    li_list = browser.find_elements(By.CSS_SELECTOR, ".cate_menu_item")
    # 通过迭代，显示每一个二级菜单，调用动作链中方法发送动作后，必须调用 perform 方法才能生效
    for li in li_list:
        action.move_to_element(li).perform()
        time.sleep(2)
    time.sleep(260)
except Exception as e:
    print(e)