# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义name用于存储商品名
    name = scrapy.Field()
    # 定义price用于存储商品价格
    price = scrapy.Field()
    # 定义link用于存储商品链接
    link = scrapy.Field()
    # 定义comnum用于存储商品评论数量
    comnum = scrapy.Field()
