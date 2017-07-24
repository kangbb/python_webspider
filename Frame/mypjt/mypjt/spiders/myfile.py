# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem

class MyfileSpider(scrapy.Spider):
    name = 'myfile'
    allowed_domains = ['www.jd.com']
    start_urls = ['https://channel.jd.com/eleNews.html',
                  'https://doc.scrapy.org/en/latest/topics/item-pipeline.html?highlight=dumps',
                  'http://www.cnblogs.com/Bright-Star/p/4163107.html'
                  ]

    def parse(self, response):
        item = MypjtItem()
        item["title"] = response.xpath("/html/head/title/text()").extract()
        item['key'] = response.xpath("//meta[@name='keywords']/@content").extract()
        print(item)
        return item