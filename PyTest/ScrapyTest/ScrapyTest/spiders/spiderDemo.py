# -*- coding: utf-8 -*-
import scrapy


class SpiderdemoSpider(scrapy.Spider):
    name = 'spiderDemo'
    allowed_domains = ['domainTest']
    start_urls = ['http://domainTest/']

    def parse(self, response):
        pass
