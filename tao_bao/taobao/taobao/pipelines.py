#	coding=gbk
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
import pymysql
from scrapy.crawler import Crawler
class TaobaoPipeline:
        def from_crawler(cls,crawler:Crawler):
            host=crawler.settings['DB_HOST']
            port = crawler.settings['DB_PORT']
            username = crawler.settings['DB_USER']
            password = crawler.settings['DB_PASS']
            database = crawler.settings['DB_NAME']
            return cls(host,port,username,password,database)
        def __init__(self,host,port,username,password,database):
            self.wb = openpyxl.Workbook()  # 创建工作簿
            self.ws = self.wb.active  # 拿到默认激活的工作表
            self.ws.title = 'TaoBaoData'  # 工作表名称
            self.ws.append(('标题', '价格', '销量', '店铺名称', '店铺地址'))  # 表头
            # self.conn=pymysql.connect(host=host,port=port,user=username,password=password,
            #                           database=database,charset='utf8mb4',
            #                           autocommit=True)
            # self.cursor=self.conn.cursor()

        def close_spider(self, spider):  # 爬虫停止运行的时候执行该方法,钩子函数，自己执行不需要调用
            self.wb.save('淘宝商品数据.xlsx')
            # self.conn.close()

        def process_item(self, item, spider):
            title = item.get('title', '')  # 如果字典中的title值为空的话，就把''（空值）赋给title变量,写法一
            price = item.get('price') or 0  # 如果字典中的title值为空的话，就把''（空值）赋给title变量，写法二
            deal_count = item.get('deal_count', '')
            shop = item.get('shop', '')
            location = item.get('location', '')
            self.ws.append((title, price, deal_count, shop, location))  #
            # self.cursor.execute(
            #     'insert into `tb_taobao_goods` '
            #     '(`g_title`,`g_price`,`g_deal_count`,`g_shop`,`g_locatior`)'
            #     'values(%s,%s,%s,%s,%s)',
            #     (title,price,deal_count,shop,location)
            # )
            return item
