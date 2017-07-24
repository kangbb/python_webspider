# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
#导入随机数模块，目的式随机挑选一个IP池中的IP
import random
#从settings文件(ban.settings为setting.py文件的地址)导入设置好的IPPOOL
from ban.settings import IPPOOL
#导入官方文档中的HttpProxyMiddleware对应模块
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
#导入用户池
from ban.settings import UAPOOL
#导入官方文档中的对应模块
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
class Ipmid(HttpProxyMiddleware):
    def __init__(self, ip=''):
        self.ip = ip
    #process_request()方法，主要处理请求
    def process_request(self, request, spider):
        #先随机选择一个IP
        thisip = random.choice(IPPOOL)
        #输出当前选择的IP，便于观察
        print('当前使用的IP是：'+thisip['ipaddr'])
        #将对应的IP添加为具体的代理，用该IP进行爬取
        request.meta['proxy'] = 'http://'+thisip['ipaddr']

class Uamid(UserAgentMiddleware):
    def __init(self, ua=''):
        self.ua = ua
    def process_request(self, request, spider):
        thisua = random.choice(UAPOOL)
        print("当前使用的uaser-agent是："+thisua)
        request.headers.setdefault('User-Agent',thisua)

class BanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
