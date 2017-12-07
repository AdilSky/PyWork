#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse
import os
import time
import hashlib
import urllib2
import json
from collections import OrderedDict

import YingLeiLian.readConfig as RC

rc = RC.ReadConfig()

appId = rc.getItemQuery('appId')

data = rc.getItemQuery('data')

appKey = rc.getItemQuery('appKey')

# print appId
#
# print data
#
# print appKey





# parser = argparse.ArgumentParser(description='manual to this script')
# parser.add_argument('--appId', type=str, help='ops_user_client app_id column')
# parser.add_argument('--data', type=str, help='request the http restfull api params')
# parser.add_argument('--appKey', type=str, help='ops_user_client app_key column')
# args = parser.parse_args()
# print args.appId
# print args.data
# print args.appKey
# if args.appId is None or args.data is None or args.appKey is None:
#     parser.print_help()
#     os._exit(0)

t = time.time()
start = int(round(t * 1000))
#MD5
m = hashlib.md5()
#
# appId = args.appId
# data = args.data


# dataJson=json.loads(data)
#print dataJson

dataJsonSortedStr = None
dataJsonStr = None
try:
    dataJson=json.loads(data)
    #print dataJson
    dataJson["timeStamp"] = start
    dataJsonStr = json.dumps(dataJson, sort_keys=True)
    print "********"
    print dataJsonStr
    dataJsonSortedJson = json.loads(dataJsonStr)
    print dataJsonSortedJson
    dataJsonSortedStr = json.dumps(dataJsonSortedJson, sort_keys=True)
    print dataJsonSortedStr
    print "********"
except Exception as e:
    print(e.message)
    os._exit(0)
dataJsonSortedStrJSON = json.loads(dataJsonSortedStr, object_pairs_hook=OrderedDict)
print dataJsonSortedStrJSON
print dataJsonSortedStrJSON.keys()
print dataJsonSortedStrJSON['itemOuterId']
params = ''
for key in dataJsonSortedStrJSON.keys():
    params += ('%s=%s&' % (key, dataJsonSortedStrJSON[key]))
params = 'appId=' + appId +'&'+ params + "appKey="+appKey
print(params)
m.update(params.encode("utf8"))
sign = m.hexdigest()
print(sign)
restFullJson = {}
restFullJson["appId"] = appId
restFullJson["data"] = dataJsonSortedJson
restFullJson["sign"] = sign
print(json.dumps(restFullJson))
headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url='http://api.dev1.yiyao.cc/item/query', headers=headers, data=json.dumps(restFullJson))
response = urllib2.urlopen(request)
print("request cost : {%s} ms" % (int(round(time.time() * 1000)) - start))
print(response.read())