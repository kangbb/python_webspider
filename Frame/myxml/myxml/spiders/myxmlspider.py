# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        #利用XPath表达式将对应的信息提取出来
        i['title'] = selector.xpath('/rss/channel/item/title/text()').extract()
        i['link'] = selector.xpath('/rss/channel/item/link/text()').extract()
        i['author'] = selector.xpath('/rss/channel/item/author/text()').extract()
        #通过for循环遍历提取出来存在item中的信息并输出
        for j in range(len(i['title'])):
            print('第'+str(j+1)+'篇文章')
            print('标题：'+i['title'][j])
            print('对应链接：'+i['link'][j])
            print('对应作者是：'+i['author'][j])
            print('-------------------------')
        return i
