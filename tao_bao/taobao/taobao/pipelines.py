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
            self.wb = openpyxl.Workbook()  # ����������
            self.ws = self.wb.active  # �õ�Ĭ�ϼ���Ĺ�����
            self.ws.title = 'TaoBaoData'  # ����������
            self.ws.append(('����', '�۸�', '����', '��������', '���̵�ַ'))  # ��ͷ
            # self.conn=pymysql.connect(host=host,port=port,user=username,password=password,
            #                           database=database,charset='utf8mb4',
            #                           autocommit=True)
            # self.cursor=self.conn.cursor()

        def close_spider(self, spider):  # ����ֹͣ���е�ʱ��ִ�и÷���,���Ӻ������Լ�ִ�в���Ҫ����
            self.wb.save('�Ա���Ʒ����.xlsx')
            # self.conn.close()

        def process_item(self, item, spider):
            title = item.get('title', '')  # ����ֵ��е�titleֵΪ�յĻ����Ͱ�''����ֵ������title����,д��һ
            price = item.get('price') or 0  # ����ֵ��е�titleֵΪ�յĻ����Ͱ�''����ֵ������title������д����
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
