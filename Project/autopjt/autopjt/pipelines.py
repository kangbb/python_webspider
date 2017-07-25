# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
class AutopjtPipeline(object):
    def __init__(self):
        self.file = codecs.open("D:/Kangbb/python_webspider/Project/autopjt/dataset/mydata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #每页包含多个商品信息，可以通过循环，每一次处理一个商品
        for j in range(0, len(item['name'])):
            name = item['name'][j]
            price = item['price'][j]
            comnum = item['comnum'][j]
            link = item['link'][j]
            #将当前页下第j个商品的name\price\comnum\link等信息处理
            #重新组合成一个dict
            goods = {'name':name, 'price':price, 'comnum':comnum, 'link':link}
            #将组合后的当前页第j商品的数据写入Json文件
            line = json.dumps(dict(goods), ensure_ascii=False) + '\n'
            self.file.write(line)
        return item
    def close_spider(self, spider):
        self.file.close()