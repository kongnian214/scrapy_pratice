#	coding=gbk
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TaobaoItem(scrapy.Item):
    title = scrapy.Field()  # ����
    price = scrapy.Field()  # �۸�
    deal_count = scrapy.Field()  # ����
    shop = scrapy.Field()  # ��������
    location = scrapy.Field()  # ���̵�ַ

