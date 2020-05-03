# _*_ coding:utf-8 _*_
import xlwt

"""
@author: Isidore
@email:616132717@qq.com
@file: save2excel.py
@time: 2018/12/23  16:20
@version: 1.0
"""

"""
程序目的：将爬取到的数据存储到Excel中
"""

class SaveBallData(object):
    def __init__(self, items):
        self.items = items
        self.run(self.items)

    def run(self, items):
        file_name = 'fucai_data.xls'
        book = xlwt.Workbook(encoding='utf8', style_compression=0)
        sheet = book.add_sheet('ball', cell_overwrite_ok=True)
        sheet.write(0, 0, '开奖日期')
        sheet.write(0, 1, '期号')
        sheet.write(0, 2, '红1')
        sheet.write(0, 3, '红2')
        sheet.write(0, 4, '红3')
        sheet.write(0, 5, '红4')
        sheet.write(0, 6, '红5')
        sheet.write(0, 7, '红6')
        sheet.write(0, 8, '蓝')
        sheet.write(0, 9, '销售额')
        sheet.write(0, 10, '一等奖')
        sheet.write(0, 11, '二等奖')

        i = 1
        while i <= len(items):
            item = items[i-1]
            sheet.write(i, 0, item.date)
            sheet.write(i, 1, item.order)
            sheet.write(i, 2, item.red1)
            sheet.write(i, 3, item.red2)
            sheet.write(i, 4, item.red3)
            sheet.write(i, 5, item.red4)
            sheet.write(i, 6, item.red5)
            sheet.write(i, 7, item.red6)
            sheet.write(i, 8, item.blue)
            sheet.write(i, 9, item.money)
            sheet.write(i, 10, item.firstPrize)
            sheet.write(i, 11, item.secondPrize)
            i += 1
        book.save(file_name)



if __name__ == '__main__':
    pass
