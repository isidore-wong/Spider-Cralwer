# --*-- coding:utf-8 --*--
from selenium import webdriver

'''
@File: selenium_moudle.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-14 10:18
'''

'''
Selenium 可以驱动浏览器完成各种操作，比如填充表单、模拟点击等
'''

'''
获取单个节点的方法
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
'''
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()

# Selenium提供了通用方法find_element()，它需要传入两个参数：查找方式By和值。实际上，它就是find_element_by_id()这种方法的通用函数版本，
# 比如 find_element_by_id(id) 就等价于 find_element(By.ID, id)
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()

# 如果要查找所有满足条件的节点，需要用find_elements()这样的方法
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()

# 节点交互   Selenium可以驱动浏览器来执行一些操作，比较常见的用法有：输入文字时用send_keys方法，清空文字时用clear方法，
# 点击按钮时用click方法
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()

# 动作链：比如鼠标拖曳、键盘按键等
from selenium import webdriver
from selenium.webdriver import ActionChains

# 拖拽
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

# 执行JavaScript
# 对于某些操作，Selenium API 并没有提供。比如，下拉进度条，它可以直接模拟运行 JavaScript，此时使用 execute_script() 方法即可实现
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')




