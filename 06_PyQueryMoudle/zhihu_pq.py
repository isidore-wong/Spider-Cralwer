# --*-- coding:utf-8 --*--
import requests
from pyquery import PyQuery as pq

'''
@File: zhihu_pq.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-2 8:15
'''

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.198 Safari/537.36'
}

html = requests.get(url, headers=headers).text
doc = pq(html)
# print(doc)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

# 写入txt文件中
with open('ex.txt', 'a', encoding='utf-8') as file:
    file.write('xxxxx')