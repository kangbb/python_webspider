# -*- coding: utf-8 -*-
import scrapy
from ban.items import BanItem

class WeisuenSpider(scrapy.Spider):
    # naem代表文件名
    name = 'weisuen'
    # allowed_domain代表语序爬行的域名 假如启动OffsiteMiddleware，非允许域名会自动过滤掉
    allowed_domains = ['sina.com.cn']
    # 爬行的起始网址;可以定义多个，逗号隔开
    start_urls = ['http://www.jd.com',
                  'http://sina.com.cn',
                  'http://yum.iqianyue.com']

    # 未指定回掉函数，则该方法是处理Scrapy爬虫爬行到的网页响应的默认方法
    def parse(self, response):
        item = BanItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        print(item['urlname'])