import scrapy
from scrapy.http import HtmlResponse
from items import BookparserItem

class LabirintruSpider(scrapy.Spider):
    name = 'labirintru'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/?stype=0']

    def parse(self, response:HtmlResponse):
        next_page = response.css('a.pagination-next__text::attr(href)').extract_first()

        book_links = response.css('a.product-title-link::attr(href)').extract()
        for link in book_links:
            yield response.follow(link, callback=self.parse_page) # в чем отличие от явного вызова? self.parse_page(link)

        yield response.follow(next_page, callback=self.parse)



    def parse_page(self, response:HtmlResponse):
        link_b = response.url
        name_b = response.css('h1::text').extract_first()

        old_price_b = response.css('span.buying-priceold-val-number::text').extract_first()
        discount_price_b = response.css('span.buying-pricenew-val-number::text').extract_first()
        price_b = response.css('span.buying-price-val-number::text').extract_first()

        rate_b = response.css('#rate::text').extract_first()

        yield BookparserItem(name=name_b,
                             link=link_b,
                             old_price=old_price_b,
                             discount_price=discount_price_b,
                             price=price_b, rate=rate_b)