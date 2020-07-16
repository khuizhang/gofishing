# -*- coding: utf-8 -*-
import scrapy


class NoticeSpider(scrapy.Spider):
    name = "notice"
    allowed_domains = ["dfo-mpo.gc.ca"]

    def parse(self, response):
        pass
