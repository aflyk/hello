# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
import scrapy

class InstparsPipeline:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.inst

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        if collection.count_documents(item) == 0:
            collection.insert_one(item)
        return item


class InstPhotosPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['photo']:
           try:
              yield scrapy.Request(item['photo'], meta=item)
           except Exception as e:
              print(e)

    def file_path(self, request, response=None, info=None):

        return f'full/{request.meta["source"]}/{request.meta["user_name"]}.jpg'

    def item_completed(self, results, item, info):
 #       if results:
 #           item['photo'] = [itm[1] for itm in results if itm[0]]
        return item