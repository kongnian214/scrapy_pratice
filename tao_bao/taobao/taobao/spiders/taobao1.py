#	coding=gbk
import scrapy
from scrapy import Request,Selector
from ..items import TaobaoItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']


    def start_requests(self):
        keywords = ['�ֻ�', '�ʼǱ�����', '������װ']
        for keyword in keywords:
            for page in range(2):
                url = f'https://s.taobao.com/search?q={keyword}&s={48 * page}'
                yield Request(url=url)

    # def parse_detail(self, response, **kwargs):
    #     pass

    def parse(self, response, **kwargs):  # �Ա���������ͨ��js��̬��Ⱦ�����ģ����Ǿ�̬���ݣ�ͨ��ѡ�����ò���������Ҫͨ��selenium���������õ�,�����ݹܵ���ʵ��
        sel = Selector(response)
        selectors = sel.css('div.items > div.item.J_MouserOnverReq > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew')
        for selector in selectors:  # type: Selector
            item = TaobaoItem()
            item['title'] = ''.join(selector.css('div.row.row-2.title > a::text').extract()).strip()
            item['price'] = selector.css('div.row.row-1.g-clearfix > div.price.g_price.g_price-highlight > strong::text').extract_first().strip()
            item['deal_count'] = selector.css('div.row.row-1.g-clearfix > div.deal-cnt::text').extract_first().strip()
            item['shop'] = selector.css('div.row.row-3.g-clearfix > div.shop > a > span:nth-child(2)::text').extract_first().strip()
            item['location'] = selector.css('div.row.row-3.g-clearfix > div.location::text').extract_first().strip()
            yield item

