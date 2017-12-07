# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from cnblogsScrapy.items import CnblogsscrapyItem


class MycnblogsSpider(CrawlSpider):
    name = 'MyCnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/BlueSkyyj/']

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),

        # 爬取下一页，没有callback，意味着follow为True
        Rule(LinkExtractor(allow=('default.html\?page=\d+',))),
        # 爬取所有的文章，并使用parse_item方法进行解析，得到文章网址，文章标题，文章内容
        Rule(LinkExtractor(allow=('BlueSkyyj/p/',)), callback='parse_item'),

        #Rule(LinkExtractor(allow=('BlueSkyyj/p/\d+/\d+/\d+/\d+.html',)), callback='parse_item'),
    )



    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

        item = CnblogsscrapyItem()

        item['page_url'] = response.url
        #item['page_title'] = response.xpath('.//div[contains(@class,"postTitl2")]/a/text()').extract()
        item['page_title'] = response.xpath(".//*[@id='cb_post_title_url']/text()").extract_first()

        # 还未实现保存html功能，以及爬取文章内容的功能

        # html = response.body.decode("utf-8")
        # html = html.replace("<head>", "<head><base href='http://www.cnblogs.com/'>")
        # item['page_html'] = html

        yield item


