#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import requests
from lxml import html

"""
@version: 1.0
@author: isidore wong
@contact: isidore_wong@163.com
@site: https://github.com/isidore-wong
@file: test.py
@time: 2019/9/6 15:55
"""

"""
program purpose:
"""
url = 'https://k.autohome.com.cn/448/12433/index_1.html?GradeEnum=0#dataList'
header = {

}
response = requests.get(url)
html_content = html.etree.HTML(response.text)
pageNum = html_content.xpath('//*[@id="maodian"]/div/div/div[2]/div[19]/div/span[1]')
print(response.content)
print(pageNum)




