# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BkchinaItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    city = scrapy.Field()
    MapType = scrapy.Field()
    name = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    officehours = scrapy.Field()
