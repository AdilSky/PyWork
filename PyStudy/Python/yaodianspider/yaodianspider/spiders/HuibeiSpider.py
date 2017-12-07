# -*- coding: utf-8 -*-
import scrapy
import os
import os.path
from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.exceptions import CloseSpider
from yaodianspider.items import YaodianItem
import logging
logger = logging.getLogger('HuibeiSpider')


# 命令行运行 scrapy crawl HuibeiSpider -o hubei_info.csv -t csv

# http://www.whfda.gov.cn/xzxkLicense/xzxkLicenseAction!viewLicence.dhtml?map.COLSQL=XKZSQL&map.XKZLX=099&map.XKZID=4fc412b8b27c46698b6d68096fb97b06&abc=0.04852832876781599

# http://www.whfda.gov.cn/portal/portalAction!getPage.dhtml?forward=menu_qytree_sjcx&index=ypjyls_licWHADp&pagesize=13&clear=true&isSd=false&node_id=GKhubfda&cat_id=ypjyls_lic

class HuibeiSpider(CrawlSpider):
    name = 'HuibeiSpider'
    allowed_domains = ['www.whfda.gov.cn']
    # 湖北省武汉市
    start_urls = ['http://www.whfda.gov.cn/portal/portalAction!getPage.dhtml?forward=menu_qytree_sjcx&index=ypjyls_licWHADp&pagesize=4000&clear=true&isSd=false&node_id=GKhubfda&cat_id=ypjyls_lic']

    detailUrlBase = 'http://www.whfda.gov.cn/xzxkLicense/xzxkLicenseAction!viewLicence.dhtml?map.COLSQL=XKZSQL&map.XKZLX=099&map.XKZID=%s&abc=0.04852832876781599'

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.zc511.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }

    # 默认解析 start_urls中的连接
    def parse(self, response):
        # /html/body/div/div[2]/div[3]/table/tbody/tr[1]
        # /html/body/div/div[2]/div[3]/table/tbody/tr[1]/td[2]
        # response.xpath('/html/body/div/div[2]/div[3]/table/tr').extract_first()
        # response.xpath('/html/body/div/div[2]/div[3]/table/tbody/tr[2]/td[6]/a/@onclick').extract_first()

        rowsXPath = '/html/body/div/div[2]/div[3]/table/tbody/tr'
        rows = response.xpath(rowsXPath)
        for row in rows:
            companyName = self._strip(row.xpath('td[2]/text()').extract_first())
            area = self._strip(row.xpath('td[3]/text()').extract_first())
            license = self._strip(row.xpath('td[4]/text()').extract_first())
            licenseDate = self._strip(row.xpath('td[5]/text()').extract_first())
            XKZID = self._strip(row.xpath('td[6]/a/@onclick').extract_first())[17:49]
            logger.debug('XKZID: %s' % XKZID)

            meta = {
                'companyName': companyName,
                'area': area,
                'license': license,
                'licenseDate': licenseDate 
            }
            # /html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[6]/a/@onclick
            detailUrl = self.detailUrlBase % XKZID
            yield scrapy.Request(url=detailUrl, headers = self.headers, meta=meta, callback=self.parse_item)

    def parse_item(self, response):
        # response.xpath('/html/body/div/span[3]/text()').extract_first()
        # /html/body/div/span[10]
        # 注册地址
        registrationAddress = self._strip(response.xpath('/html/body/div/span[3]/text()').extract_first())
         # 经营范围
        businessScope = self._strip(response.xpath('/html/body/div/span[4]/text()').extract_first())
        # 法定代表人
        legalRepresentative = self._strip(response.xpath('/html/body/div/span[5]/text()').extract_first())
        # 企业负责人
        companyController = self._strip(response.xpath('/html/body/div/span[6]/text()').extract_first())
        # 企业质量负责人
        qualityRepresentative = self._strip(response.xpath('/html/body/div/span[7]/text()').extract_first())
        # 仓库地址
        repositoryAddress = self._strip(response.xpath('/html/body/div/span[8]/text()').extract_first())
        # 发证机关
        issuingAuthority = self._strip(response.xpath('/html/body/div/span[9]/text()').extract_first())
        
        validTillYear = self._strip(response.xpath('/html/body/div/span[10]/text()').extract_first())
        validTillMonth = self._strip(response.xpath('/html/body/div/span[11]/text()').extract_first())
        validTillDay = self._strip(response.xpath('/html/body/div/span[12]/text()').extract_first())

        # 有效期至
        validTillDate = '%s-%s-%s' % (validTillYear,validTillMonth,validTillDay)

        meta = response.meta

        item = YaodianItem()
        
        item['companyName'] = meta['companyName']
        item['area'] = meta['area']
        item['license'] = meta['license']
        item['licenseDate'] = meta['licenseDate']

        item['registrationAddress'] = registrationAddress
        item['businessScope'] = businessScope
        item['legalRepresentative'] = legalRepresentative
        item['companyController'] = companyController
        item['qualityRepresentative'] = qualityRepresentative
        item['repositoryAddress'] = repositoryAddress
        item['issuingAuthority'] = issuingAuthority
        item['validTillDate'] = validTillDate

        return item

    def _strip(self, str):
        value = ''
        if str != None:
            value = str.strip()
        return value