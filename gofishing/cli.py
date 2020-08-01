from gofishing import stations_csv
import click
import logging
import os
import time
from scrapy.crawler import CrawlerProcess

from gofishing.spiders.station import StationSpider
from gofishing.spiders.tide import TideSpider
from gofishing.spiders.area import AreaSpider
from scrapy.utils.log import configure_logging


configure_logging(install_root_handler=True)
logging.disable(50)  # CRITICAL = 50


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--check", "-c", nargs=2, type=str, help="check tide by location and mm/dd"
)
def tide(check):
    if check:
        if os.path.isfile(stations_csv):
            location = check[0]
            date = check[1]
            tide_crawler = CrawlerProcess()
            tide_crawler.crawl(TideSpider, location=location, date=date)
            tide_crawler.start()
        else:
            print(
                f"Cannot find {stations_csv}. Run 'gofishing tide' first and try again!"
            )
    else:
        station_crawler = CrawlerProcess()
        station_crawler.crawl(StationSpider)
        station_crawler.start()


@cli.command()
@click.option(
    "--check",
    "-c",
    nargs=2,
    type=str,
    help="check if harvest given type is allowed in this area",
)
def area(check):
    areas_csv = "/tmp/areas.csv"
    """
    if check:
        # tide table url for a station: https://www.pac.dfo-mpo.gc.ca/fm-gp/rec/tidal-maree/a-s17-eng.html

        tide_crawler = CrawlerProcess()
        tide_crawler.crawl(TideSpider, start_urls=[station_url], date=date)
        tide_crawler.start()

    else:
        if os.path.isfile(areas_csv):
            print(
                f"Skipping parsing as {areas_csv} exists. Please delete it if you would like a fresh parsing."
            )
        else:
            station_crawler = CrawlerProcess()
            station_crawler.crawl(AreaSpider)
            station_crawler.start()
    """
