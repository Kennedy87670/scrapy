# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import sqlite3

class SQLLitePipeline(object):

    def open_spider(self, spider):
        self.collection = sqlite3.connect("slick.db")
        self.c = self.collection.cursor()
        self.c.execute(
            """
            CREATE TABLE computer(
                name TEXT,
                link ,
                store-name TEXT ,
                price TEXT 
            )
            """
        )
        self.collection.commit()

    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.c.execute(
            """
            INSERT INTO computer (name, link, store-name, price) VALUES(?,?,?,?)
            """, (
                item.get('name'),
                item.get('link'),
                item.get('store-name'),
                item.get('price'),
            ))
        self.collection.commit()
        return item
    # @classmethod
    # def from_crawler(cls, crawler):
    #     logging.warning(crawler.settings.get("MONGO_URL"))
    #     pass
    # def open_spider(self, spider):
    #     logging.warning("Spider Opened from Pipeline")

    # def close_spider(self, spider):
    #     logging.warning("Spider closed from Pipeline")


    # def process_item(self, item, spider):
    #     return item
