import scrapy
from scrapy.http import HtmlResponse
from wowparsing.items import WowparsingItem

class WowruSpider(scrapy.Spider):
    name = 'wowru'
    allowed_domains = ['worldofwarcraft.com']
    start_urls = ['https://worldofwarcraft.com/ru-ru/game/pvp/leaderboards/2v2?page=1']

    def parse(self, response:HtmlResponse):
        next_page = response.css('a.Link.Button.Button--ghost.Button--small.Pagination-button.Button--next.is-selected::attr(href)').extract_first()

        char_links = response.xpath("//a[contains(@class,'Link Character')]//@href").extract()
        for link in char_links:
            yield response.follow(link, callback=self.page_parse)

        yield response.follow(next_page, callback=self.parse)

    def page_parse(self, response:HtmlResponse):
         build = response.css('div.react-mount::attr(data-initial-state)').extract()
         yield WowparsingItem(build=build)



