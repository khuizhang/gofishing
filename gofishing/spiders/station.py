# -*- coding: utf-8 -*-
from scrapy import Spider

from gofishing.items import Station


class StationSpider(Spider):
    name = "station"
    allowed_domains = ["tides.gc.ca"]
    start_urls = ["https://tides.gc.ca/eng/station/list"]

    custom_settings = {
        "LOG_ENABLED": False,
        "FEED_FORMAT": "csv",
        "FEED_URI": "file:///tmp/stations.csv",
    }

    def parse(self, response):
        host = response.url.split("/eng")[0]
        for row in response.xpath("//table[@id='sitesTable']//tr"):
            if row.xpath(".//td"):
                station_id = row.xpath(".//td[@class='id']/text()").get()
                station_url = host + row.xpath(".//td[@class='sitename']/a/@href").get()
                site = row.xpath(".//td[@class='sitename']/a/text()").get()
                province, latitude, longitude = row.xpath(
                    ".//td[@class='province']/text()"
                ).getall()
                yield Station(
                    station_id=station_id,
                    station_url=station_url,
                    site=site,
                    province=province,
                    latitude=latitude,
                    longitude=longitude,
                )
