# --*-- coding:utf-8 --*--
import requests
import re
import json
import time
from bs4 import BeautifulSoup

'''
@File: re_maoyan.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-11-23 14:14
'''

'''
Description: 爬取猫眼电影top100影单
'''


def get_page(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) '
                       'Chrome/86.0.4240.198  Safari / 537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name.*?<a .*?>(.*?)</a>' +
                         '.*?star">(.*?).*?releasetime">(.*?).*?integer">(.*?).*?fraction">(.*?)</i></p>.*?<dd>',
                         re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3],
            'release time': item[4],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('movie.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(0, 10):
        main(i * 10)
        time.sleep(1)


