#-*- coding : utf-8-*-
# coding:unicode_escape
import scrapy
from scrapy import Selector,Request
from ..items import MovieItem
from scrapy.http import HtmlResponse
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    def start_requests(self):#第二种方法
        for page in range(1):
            yield  Request(
                url=f'https://movie.douban.com/top250?start={page*25}&filter=',
                #meta={'proxy':'socks5://127.0.0.1:1086'}##代理ip
                )
    def parse(self, response:HtmlResponse,**kwargs):
        sel=Selector(response)
        list_items=sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            detail_url=list_item.css('div.info>div.hd>a::attr(href)').extract_first()
            movit_item=MovieItem()
            movit_item['title']=list_item.css("span.title::text").extract_first()
            movit_item['rank']=list_item.css("span.rating_num::text").extract_first()
            movit_item['subject']=list_item.css("span.inq::text").extract_first()
            yield Request(
                url=detail_url,callback=self.parse_detail,
                cb_kwargs={'item':movit_item}
            )
    def parse_detail(self,response,**kwargs):
        movit_item=kwargs['item']
        sel=Selector(response)
        movit_item['duration']=sel.css('span["property=v:runtime"]::attr(content)').extract()
        movit_item['intro'] =sel.css('span["property=v:summary::text"]').extract_first() or ''
        yield movit_item

