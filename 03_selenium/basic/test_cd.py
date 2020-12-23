# --*-- coding:utf-8 --*--
from selenium import webdriver
from PIL import Image
import pytesseract

'''
@File: test_cd.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-14 9:16
'''

'''
driver_path = 'D:/anaconda/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://www.baidu.com')
print(driver.page_source)
'''

def read_text(text_path):
    """
    传入文本(jpg、png)的绝对路径,读取文本
    :param text_path:
    :return: 文本内容
    """
    # 验证码图片转字符串
    im = Image.open(text_path)
    # 转化为8bit的黑白图片
    imgry = im.convert('L')
    # 二值化，采用阈值分割算法，threshold为分割点
    threshold = 140
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    # 识别文本
    text = pytesseract.image_to_string(out, lang="eng", config='--psm 6')
    return text

if __name__ == '__main__':
    print(read_text("./testcode.png"))