# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

class RugstorePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect("sqlite3_db.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        # Check if table exist first
        self.curr.execute("""
            DROP TABLE IF EXISTS rugs
        """)
        self.curr.execute("""
            CREATE TABLE rugs(
                title TEXT,
                link TEXT,
                price REAL
            )
        """)

    def process_item(self, item, spider):
        # Insert items into table
        self.store_db(item)

        print('\nPipeline:', item['title'])
        return item

    def store_db(self, item):
        self.curr.execute("""
            INSERT INTO rugs
            VALUES (?,?,?)""", (
                item['title'][0],
                item['link'][0],
                item['price'][0]
            )
        )
        self.conn.commit()
