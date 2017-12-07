#-*-coding:utf-8-*-
# Time:2017/10/14 23:28
# Author:YangYangJun

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
with open('items.json') as f:
    rownum = 0
    # print f
    new_list = json.load(f)
    # new_list 是一个列表 列表中元素是字典类型
    # print  new_list
    for i in new_list:
        # 的列表中的各个元素 字典
        rownum += 1
        #[{"reply": ["0"], "title": ["\u4e13\u4e1a\u627f\u63a5\u7f51\u7edc\u722c\u866b\uff0c\u4e8c\u697c"], "author": ["fdsd777"]}]
        #print i
        #print i['page_title']
        #字典中的元素值是列表所以要加上序列号获取值
        print "                                           "
        print i['page_title']
        print "                                           "
        print("""line{}:  page_title:{},  page_url:{}, .""".format(rownum,
                                                                     i['page_title'],
                                                                     i['page_url']))


