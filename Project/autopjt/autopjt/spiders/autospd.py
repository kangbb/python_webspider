# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import  Request
class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002203.html']
    def parse(self, response):
        item = AutopjtItem()
        #通过xpath表达式提取商品名称、价格、链接、评论数量
        item['name'] = response.xpath("//a[@class='pic']/@title").extract()
        item['price'] = response.xpath("//span[@class='price_n']/text()").extract()
        item['link'] = response.xpath("//a[@class='pic']/@href").extract()
        item['comnum'] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        #print(item['name'])
        #print(item['price'])
        #print(item['link'])
        #print(item['comnum'])
        # 提取完item返回
        yield item
        #关键部分
        for i in range(2,10):
            #通过总结的网址格式构造爬取的网址
            url = 'http://category.dangdang.com/pg'+str(i)+'-cid4002203.html'
            #通过yield返回Request,并指定要爬取的网址和毁掉函数
            #实现自动爬取
            yield Request(url, callback=self.parse)
