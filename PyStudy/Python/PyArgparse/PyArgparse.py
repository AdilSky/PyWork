#-*-coding:utf-8-*-
# Time:2017/11/1 20:09
# Author:YangYangJun

# argparse是python用于解析命令行参数和选项的标准模块

# argparse 是一个源文件
import argparse

# 实例化ArgumentParser，ArgumentParser 是argparse 的一个类,而该类有两个基类
# parser = argparse.ArgumentParser()

# add_argument() 是其基类 _ActionsContainer 的方法，这里继承使用
# parser.add_argument()

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--appId', type=str, help='ops_user_client app_id column')
parser.add_argument('--data', type=str, help='request the http restfull api params')
parser.add_argument('--appKey', type=str, help='ops_user_client app_key column')

print parser.print_help()

print "help"

print parser

print "parser"

# 解析命令行参数 返回解析后的信息
args = parser.parse_args()

# 返回 Namespace(appId='ggdfFRnf4UsuQfgAAk9nAA==', appKey='zXKoeppLgNL3Ii0vbibs2g==', \
# data='\'{"supplierSn":"748307065314700","itemOuterId":"10200009","outUserId":"DWI00006671"}\'')

print  args

print args.appId  # ggdfFRnf4UsuQfgAAk9nAA==

print args.data   # '{"supplierSn":"748307065314700","itemOuterId":"10200009","outUserId":"DWI00006671"}'

