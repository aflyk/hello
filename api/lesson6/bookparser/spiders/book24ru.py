import scrapy
from scrapy.http import HtmlResponse
from items import BookparserItem

class Book24ruSpider(scrapy.Spider):
    name = 'book24ru'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/search/?q=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5']

    def parse(self, response:HtmlResponse):
        next_page = response.css('a.catalog-pagination__item._text.js-pagination-catalog-item::attr(href)').extract_first()

        book_links = response.css('a.book__title-link.js-item-element.ddl_product_link::attr(href)').extract()
        for link in book_links:
            yield response.follow(link, callback=self.page_parse)

        yield response.follow(next_page, callback=self.parse)

    def page_parse(self, response:HtmlResponse):
        link = response.url
        name = response.css('h1::text').extract_first()
        price = response.css('div.item-actions__price b::text').extract_first()
        old_price = response.css('div.item-actions__price-old::text').extract_first()
        author = response.css('a.item-tab__chars-link::text').extract_first()
        rate = response.css('span.rating__rate-value::text').extract_first()

        yield BookparserItem(name=name, price=price, author=author, rate=rate, link=link, old_price=old_price)