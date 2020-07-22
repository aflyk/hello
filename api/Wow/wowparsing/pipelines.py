# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import datetime
import json


class WowparsingPipeline:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.mono_base = self.client.wow2v2_rate

    def process_item(self, item, spider):
        collection = self.mono_base[spider.name + str(datetime.datetime.now().date())]

        data = json.loads(item['build'][0])
        item['wow_class'] = data['character']['class']['enum']
        item['spec'] = data['character']['spec']['enum']

        for pos, name in enumerate(data['character']['specs']):
            if name['id'] == item['spec'].lower():
                item['build'] = [i['name'] for i in data['character']['specs'][pos]['talents']['flattened']]
                item['pvp'] = [i['name'] for i in data['character']['specs'][pos]['pvpTalents']['flattened']]

        item['rate'] = data['character']['pvp']['ratings']['2v2']['rating']
        if collection.count_documents(item) == 0:
            collection.insert_one(item)
        return item
