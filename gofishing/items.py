# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Station(scrapy.Item):
    station_id = scrapy.Field()
    station_url = scrapy.Field()
    site = scrapy.Field()
    province = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()


class Area(scrapy.Item):
    area_id = scrapy.Field()
    area_description = scrapy.Field()
    area_url = scrapy.Field()
