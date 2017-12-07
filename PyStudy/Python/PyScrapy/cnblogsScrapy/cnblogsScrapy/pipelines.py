# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
class CnblogsscrapyPipeline(object):
    def process_item(self, item, spider):
        # file_name = './blogs/' + item['page_title'] + '.html'
        # with codecs.open(filename=file_name, mode='wb', encoding='utf-8') as f:
        #     f.write(item['page_html'])
        return item





