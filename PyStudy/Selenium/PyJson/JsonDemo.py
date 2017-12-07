#-*-coding:utf-8-*-
# Time:2017/9/22 20:15
# Author:YangYangJun

import json

#语法
#json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)

#  indent 缩进  indent = 4 表示缩进 4个单元格
#  sort_keys=True 按 keys 进行排序展示
# separators 分离器 separators=(',', ': '),如果已经使用了缩进，则这个可以不使用，多余了，效果一样。

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]


json1 = json.dumps(data)
print json1 # [{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]


json2 = json.dumps(data,sort_keys=True)
print json2 # [{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]

json3 = json.dumps(data,sort_keys=False)
print json3 # [{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]

testData =[{'name':u'周星驰','age':28}]

jsonD = json.dumps(testData)
print jsonD

print json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))


#语法
#json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

testD = json.loads(jsonData)
print testD  #{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}

