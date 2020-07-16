# -*- coding: utf-8 -*-
from gofishing.items import Area
import scrapy


class AreaSpider(scrapy.Spider):
    name = "area"
    allowed_domains = ["dfo-mpo.gc.ca"]
    start_urls = [
        "https://www.pac.dfo-mpo.gc.ca/fm-gp/maps-cartes/areas-secteurs/index-eng.html"
    ]

    custom_settings = {
        "LOG_ENABLED": True,
        "FEED_FORMAT": "csv",
        "FEED_URI": "file:///tmp/areas.csv",
    }

    def parse(self, response):
        host = response.url.split("/fm-gp")[0]
        for row in response.xpath("//table[@id='area-table']//tr"):
            if row.xpath(".//td"):
                area_id = row.xpath(".//td/a/text()").get().strip().split()[1]
                try:
                    area_description = row.xpath(".//td/text()").getall()[1]
                except IndexError:
                    area_description = row.xpath(".//td/text()").get()
                area_url = host + row.xpath(".//td/a/@href").get().strip()
                yield Area(
                    area_id=area_id,
                    area_description=area_description,
                    area_url=area_url,
                )
