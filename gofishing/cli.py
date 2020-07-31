import click
import csv
import datetime
import logging
import os
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
    stations_csv = "/tmp/stations.csv"

    if check:
        location = check[0]
        date = check[1]
        now = datetime.datetime.now()
        current_year = now.year
        station_url_prefix = (
            "https://tides.gc.ca/eng/data/table/" + str(current_year) + "/wlev_sec/"
        )
        station_url = ""
        if os.path.isfile(stations_csv):
            stations_dict = csv.DictReader(open(stations_csv))
            for row in stations_dict:
                if row["site"].lower() == location.lower():
                    station_url = station_url_prefix + row["station_id"]
        tide_crawler = CrawlerProcess()
        tide_crawler.crawl(TideSpider, start_urls=[station_url], date=date)
        tide_crawler.start()
    else:
        if os.path.isfile(stations_csv):
            print(
                f"Skipping parsing as {stations_csv} exists. Please delete it if you would like a fresh parsing."
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
