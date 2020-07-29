# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


import scrapy


class DataBasePipeline:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.leroymerlin_shop

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        item['specification_value'] = [''.join(i).replace('\n','') for i in [line.split(' ') for line in item['specification_value']]]
        item['specification'] = dict(zip(item['specification_name'],item['specification_value']))
        del item['specification_value']
        del item['specification_name']
        item['link'] = item['link'][0]
        item['price'] = item['price'][0]
        if collection.count_documents(item) == 0:
            collection.insert_one(item)
        return item


class LeroymerlinPhotosPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['picture']:
            for img in item['picture']:
                try:
                    yield scrapy.Request(img, meta=item)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['picture'] = [itm[1] for itm in results if itm[0]]
        return item

    def file_path(self, request, response=None, info=None):
        return 'full/' + request.meta['name'] + '/'+ request.url.split('/')[-1]