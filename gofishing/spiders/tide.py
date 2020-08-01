import csv
import scrapy
import datetime
from gofishing import stations_csv


class TideSpider(scrapy.Spider):
    name = "tide"
    allowed_domains = ["tides.gc.ca"]
    custom_settings = {
        "LOG_ENABLED": True,
    }

    def __init__(self, location="", **kwargs):
        now = datetime.datetime.now()
        current_year = now.year
        station_url_prefix = (
            "https://tides.gc.ca/eng/data/table/" + str(current_year) + "/wlev_sec/"
        )
        station_url = ""
        stations_dict = csv.DictReader(open(stations_csv))
        for row in stations_dict:
            if row["site"].lower() == location.lower():
                station_url = station_url_prefix + row["station_id"]
        self.start_urls = [station_url]
        super().__init__(**kwargs)
        # example url from cli: start_urls = ["https://tides.gc.ca/eng/data/table/2020/wlev_sec/7577"]

    def parse(self, response):
        target_month, target_day = self.date.split("/")
        print(f"Tide height(m) prediction on {self.date}:")
        for sel in response.xpath("//table[@class='width-100']"):
            month_year = sel.xpath("caption/text()").get()
            month_name = month_year.split()[0]
            month_number = datetime.datetime.strptime(month_name, "%B").month
            if str(month_number) == target_month:
                for row in sel.xpath(".//tr"):
                    contents = row.xpath(".//td/text()").getall()
                    try:
                        day = contents[0]
                        if day == target_day:
                            print(contents)
                    except IndexError:
                        pass
