#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse
import os
import time
import hashlib
import urllib2
import json
from collections import OrderedDict
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--appId', type=str, help='ops_user_client app_id column')
parser.add_argument('--data', type=str, help='request the http restfull api params')
parser.add_argument('--appKey', type=str, help='ops_user_client app_key column')
args = parser.parse_args()
if args.appId is None or args.data is None or args.appKey is None:
    parser.print_help()
    os._exit(0)

t = time.time()
start = int(round(t * 1000))
#MD5
m = hashlib.md5()

appId = args.appId
data = args.data
appKey = args.appKey
dataJsonSortedStr = None
dataJsonStr = None
try:
    dataJson=json.loads(data)
    dataJson["timeStamp"] = start
    dataJsonStr = json.dumps(dataJson, sort_keys=True)
    dataJsonSortedJson = json.loads(dataJsonStr)
    dataJsonSortedStr = json.dumps(dataJsonSortedJson, sort_keys=True)
except Exception as e:
    print(e.message)
    os._exit(0)
dataJsonSortedStrJSON = json.loads(dataJsonSortedStr, object_pairs_hook=OrderedDict)
params = ''
for key in dataJsonSortedStrJSON.keys():
    if key == 'needItemList':
        if dataJsonSortedStrJSON[key] is True:
            params += ('%s=%s&' % (key, 'true'))
        elif dataJsonSortedStrJSON[key] is False:
            params += ('%s=%s&' % (key, 'false'))
        else:
            params += ('%s=%s&' % (key, dataJsonSortedStrJSON[key]))
    elif key == 'needDeliveryList':
        if dataJsonSortedStrJSON[key] is True:
            params += ('%s=%s&' % (key, 'true'))
        elif dataJsonSortedStrJSON[key] is False:
            params += ('%s=%s&' % (key, 'false'))
        else:
            params += ('%s=%s&' % (key, dataJsonSortedStrJSON[key]))
    else:
        params += ('%s=%s&' % (key, dataJsonSortedStrJSON[key]))
params = 'appId=' + appId +'&'+ params + "appKey="+appKey
print(params)
m.update(params.encode("utf8"))
sign = m.hexdigest()
print(sign)
if dataJsonSortedJson['needItemList'] == 'null':
    dataJsonSortedJson['needItemList'] = None
if dataJsonSortedJson['needDeliveryList'] == 'null':
    dataJsonSortedJson['needDeliveryList'] = None
restFullJson = {}
restFullJson["appId"] = appId
restFullJson["data"] = dataJsonSortedJson
restFullJson["sign"] = sign
print(json.dumps(restFullJson))
headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url='http://api.dev1.yiyao.cc/order/detail/query', headers=headers, data=json.dumps(restFullJson))
response = urllib2.urlopen(request)
print("request cost : {%s} ms" % (int(round(time.time() * 1000)) - start))
print(response.read())