# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urlname = scrapy.Field() # 网页标题
    urlkey = scrapy.Field() # 网页关键词
    urlcr = scrapy.Field() # 网页版权信息
    urladdr = scrapy.Field() # 网页地址
