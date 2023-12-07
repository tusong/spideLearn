# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
import time
from itemadapter import ItemAdapter

import pymongo

from myproject.toutiaoItems import AticlesItem
    

class WeiboPipeline():
    def process_item(self, item, spider):
        if isinstance(item, AticlesItem):
            if item.get('created_at'):
                item['created_at'] = item['created_at'].strip()
               
        return item

class TimePipeline():
    def process_item(self, item, spider):
        if isinstance(item, AticlesItem):
            now = time.strftime('%Y-%m-%d %H:%M', time.localtime())
            item['crawled_at'] = now
            
        return item

class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db='toutiao'
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[AticlesItem.collection].create_index([('id', pymongo.ASCENDING)])
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        if isinstance(item, AticlesItem):
            self.db[item.collection].update({'id': item.get('id')}, {'$set': item}, True)
        return item

