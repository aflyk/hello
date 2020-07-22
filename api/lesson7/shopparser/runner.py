from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from shopparser.spiders.leroymerlin import LeroymerlinSpider
from shopparser import settings


if __name__ == '__main__':
    search = input("Введите, что ищете")

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinSpider, search=search)

    process.start()