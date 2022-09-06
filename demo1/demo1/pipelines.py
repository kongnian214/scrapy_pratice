
#-*- coding : utf-8-*-
# coding:unicode_escape
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import openpyxl
import pymysql
class DbPipeline:
    def __init__(self):
        self.conn=pymysql.connect(host='localhost',port=3306,
                                  user='root',password='111111',
                                  database='spider',charset='utf8mb4')
        self.cursor=self.conn.cursor()
        self.data=[]
    def close_spider(self,spider):#只调用一次
        if len(self.data)>0:
            self._write_to_db()
        self.conn.close()
    def process_item(self, item, spider):#每拿到一条数据都调用一次
        self.data.append(
            (item['title'], item['rank'], item['subject'], item['duration'], item['intro'])
        )
        if len(self.data)==100:
            self._write_to_db()
            self.data.clear()
        return item
    def _write_to_db(self):
        self.cursor.executemany(
            'insert into tb_top_movie(title, ranting, subject) values (%s,%s,%s,%s,%s)',
            self.data
        )
        self.conn.commit()
class Demo1Pipeline:
    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.ws=self.wb.active
        self.ws.title='Top250'
        self.ws.append(('标题','评分','主题','时长','简介'))
    def close_spider(self,spider):#只调用一次
        self.wb.save('电影数据.xlsx')
    def open_spider(self,spider):#只调用一次
        pass
    def process_item(self, item, spider):#每拿到一条数据都调用一次
        self.ws.append(
            (item['title'],item['rank'],item['subject'],item['duration'],item['intro']))
        return item
