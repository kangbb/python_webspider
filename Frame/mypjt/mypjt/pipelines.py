# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import re
class MypjtPipeline(object):
    def __init__(self):
        self.file = codecs.open("D://Kangbb/python_webspider/Frame/mypjt/data1.txt", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        l = str(item)+'\n'
        self.file.write(l)
        return item
    def close_spider(self, spider):
        self.file.close()

class CreateJson(object):
    def __init__(self):
        self.file = codecs.open("D:/Kangbb/python_webspider/Frame/mypjt/data1.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #通过dict(item)将item转换为一个字典
        #然后通过json模块下的dumps()处理字典数据
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        #得到的数据后加上‘\n'换行符形成要写入的一行数据
        #写入数据到json文件中
        self.file.write(line)
        return item
    def close_spider(self, spider):
        self.file.close()
