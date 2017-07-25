# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cwpjt.items import CwpjtItem

class MycrawlSpider(CrawlSpider):
    name = 'mycrawl'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        #自动爬取网页中符合条件的链接，以便进行下一次爬取
        Rule(LinkExtractor(allow=('.*?/n.*?shtml',), allow_domains=('sohu.com',)), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = CwpjtItem()
        #提取网页中有需要的数据
        i['title'] = response.xpath('/html/head/title/text()').extract()
        i['link'] = response.xpath("//link[@rel='canonical']/@href").extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
