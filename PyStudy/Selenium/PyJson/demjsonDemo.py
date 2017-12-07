#-*-coding:utf-8-*-
# Time:2017/9/22 21:25
# Author:YangYangJun

import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
#demjson.encode(self, obj, nest_level=0)
json = demjson.encode(data)
print json  #[{"a":1,"b":2,"c":3,"d":4,"e":5}]




json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
#语法
#demjson.decode(self, txt)
text = demjson.decode(json)
print  text  #{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}