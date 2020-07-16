import scrapy
import datetime


class TideSpider(scrapy.Spider):
    name = "tide"
    allowed_domains = ["tides.gc.ca"]
    custom_settings = {
        "LOG_ENABLED": False,
    }

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
