# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class YaodianItem(scrapy.Item):
    # define the fields for your item here like:
    # 企业名称
    companyName = Field()
    # 所在辖区
    area = Field()
    # 许可证号
    license = Field()
    # 发证日期
    licenseDate = Field()
    # 注册地址
    registrationAddress = Field()
    # 法定代表人
    legalRepresentative = Field()
    # 企业负责人
    companyController = Field()
    # 企业质量负责人
    qualityRepresentative = Field()
    # 仓库地址
    repositoryAddress = Field()
    # 经营范围
    businessScope = Field()
    # 有效期至
    validTillDate = Field()
    # 发证机关
    issuingAuthority = Field()


    pass
