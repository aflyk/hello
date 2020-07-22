import scrapy

from scrapy.http import HtmlResponse
from shopparser.items import ShopparserItem
from scrapy.loader import ItemLoader

class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        self.start_urls = [f"https://leroymerlin.ru/search/?q={search}"]

    def parse(self, response:HtmlResponse):
        next_page = response.css('.next-paginator-button::attr(href)').extract_first()

        list_goods = response.css('.product-name-inner')
        for link in list_goods:
            yield response.follow(link, callback=self.parse_goods)

        yield response.follow(next_page, callback=self.parse)

    def parse_goods(self, response:HtmlResponse):
        loader = ItemLoader(item=ShopparserItem(), response=response)
        loader.add_css('name', '.header-2::text')
        loader.add_css('specification_value', '.def-list__definition::text')
        loader.add_css('specification_name', '.def-list__term::text')
        loader.add_css('price', 'meta+ span::text')
        loader.add_xpath('picture', '//img[@alt="product image"]//@src')
        loader.add_value('link', response.url)
        yield loader.load_item()

