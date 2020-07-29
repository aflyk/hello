from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from wowparsing import settings
from wowparsing.spiders.wowru import WowruSpider


if __name__ == '__main__':

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(WowruSpider)
    process.start()