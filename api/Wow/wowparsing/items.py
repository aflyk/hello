# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WowparsingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    rate = scrapy.Field()
    spec = scrapy.Field()
    wow_class = scrapy.Field()
    build = scrapy.Field()
    pvp = scrapy.Field()
    type = scrapy.Field()