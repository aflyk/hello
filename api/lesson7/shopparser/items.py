# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def price_float(value):
    if value:
        return float(value.replace(' ',''))
    return value

class ShopparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    specification = scrapy.Field()
    specification_name = scrapy.Field()
    specification_value = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(price_float))
    link = scrapy.Field()
    picture = scrapy.Field()
