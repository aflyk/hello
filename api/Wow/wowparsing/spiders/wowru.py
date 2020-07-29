import scrapy
from scrapy.http import HtmlResponse
from wowparsing.items import WowparsingItem
from copy import deepcopy

class WowruSpider(scrapy.Spider):
    name = 'wowru'
    allowed_domains = ['worldofwarcraft.com']
    categories = ['game/pvp/leaderboards/2v2', 'game/pvp/leaderboards/3v3', 'game/pvp/leaderboards/battlegrounds']
    start_urls = ['https://worldofwarcraft.com/ru-ru/']

    def parse(self, response:HtmlResponse):
        for pos, category in enumerate(self.categories):
            link = response.url + category
            yield response.follow(link,
                                  callback=self.parse_category,
                                  cb_kwargs={"pos": deepcopy(pos)})

    def parse_category(self, response:HtmlResponse, pos):
        next_page = response.css('a.Link.Button.Button--ghost.Button--small.Pagination-button.Button--next.is-selected::attr(href)').extract_first()

        char_links = response.xpath("//a[contains(@class,'Link Character')]//@href").extract()
        for link in char_links:
            yield response.follow(link, callback=self.page_parse, cb_kwargs={'pos': deepcopy(pos)})

        yield response.follow(next_page, callback=self.parse_category, cb_kwargs={'pos': deepcopy(pos)})

    def page_parse(self, response:HtmlResponse, pos):
         build = response.css('div.react-mount::attr(data-initial-state)').extract()
         yield WowparsingItem(build=build, type=pos)



