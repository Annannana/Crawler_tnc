# -*- coding: utf-8 -*-
import json
import scrapy
from urllib.parse import urlencode

from bkchina.items import BkchinaItem
from bkchina.cities import cities


class BkaddressSpider(scrapy.Spider):
    name = 'BKAddress'
    allowed_domains = ['bkchina.cn']
    base_url = 'https://www.bkchina.cn/restaurant/getStoreCity?'

    def start_requests(self):
        for city in cities:
            params = {'storeCity': city, 'p': 1}
            yield scrapy.Request(url=self.base_url + urlencode(params), callback=self.parse_start,
                                 meta={"city_params": params})

    def parse_start(self, response):
        city_params = response.meta.get("city_params")
        city = city_params['storeCity']
        item = BkchinaItem()
        item['city'] = city
        item['MapType'] = '2'
        item['link'] = 'https://www.bkchina.cn/restaurant/index.html'

        if city_params['p'] == 1:
            total_pages = int(response.xpath('//div[@class="page_th"]/li[1]/a/text()').re_first('/(\d+) 页'))
            for page in range(2, total_pages + 1):
                params = {'storeCity': city, 'p': page}
                yield scrapy.Request(url=self.base_url + urlencode(params), callback=self.parse_start,
                                     meta={"city_params": params})

        l = response.text.split('var data_info = ')[1]
        l = l.split('];')[0] + ']'
        stores = json.loads(l)
        for store in stores:
            item['lat'] = store.get("storeLatitude", '')
            item['lng'] = store.get("storeLongitude", '')
            item['name'] = store.get("storeName", '')
            item['phone'] = [store.get("storePhone", '')]
            item['address'] = store.get("storeAddress", '')
            item['officehours'] = store.get("storeBusinessHours", '')
            yield item
