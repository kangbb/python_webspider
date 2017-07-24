# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    #定义新的headers，包含要提取字段的行信息列表
    headers = ['name', 'sex', 'addr', 'email']
    #定义间隔符
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        #提取各行的name\sex\列信息
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        #输出
        print('名字是：'+str(i['name']))
        print('性别是：'+str(i['sex']))
        #输出间隔符，方便识别
        print('----------------------')
        return i
