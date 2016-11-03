# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class Tes1Pipeline(object):
#     def process_item(self, item, spider):
#         return item
# import sys
# import MySQLdb
# import hashlib
# from scrapy.exceptions import DropItem
# from scrapy.http import Request

# class MySQLStorePipeline(object):
#   def __init__(self):
#     self.conn = MySQLdb.connect(user='root', 'root', 'olx_property', 'localhost:3306', charset="utf8", use_unicode=True)
#     self.cursor = self.conn.cursor()

# def process_item(self, item, spider):    
#     try:
#         self.cursor.execute("""INSERT INTO property (url, price)  
#                         VALUES (%s, %s)""", 
#                        (item['url'].encode('utf-8'), 
#                         item['price'].encode('utf-8')))

#         self.conn.commit()


#     except MySQLdb.Error, e:
#         print "Error %d: %s" % (e.args[0], e.args[1])


#     return item

import pymongo

class MongoPipeline(object):
	collection_name = 'scrapy_items'


	def __init__(self, mongo_uri, mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db
	
	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			mongo_uri=crawler.settings.get('localhost:27017'),
			mongo_db=crawler.settings.get('olx', 'items')
		)

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]
	
	def close_spider(self, spider):
		self.client.close()
	
	def process_item(self, item, spider):
		self.db[self.collection_name].insert(dict(item))
		return item