#	coding=gbk
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import Request
from scrapy.http import HtmlResponse
from .utils import create_chrome_driver,add_cookies

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class TaobaoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn��t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class TaobaoDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def __init__(self):  # ��ʼ�����ݹܵ�ʱģ���û���¼
        self.browser = create_chrome_driver()
        self.browser.get('https://www.taobao.com')
        add_cookies(self.browser, 'taobao2.json')

    def __del__(self):  # ����ʱִ�и÷���
        self.browser.close()

    def process_request(self, request: Request, spider):  # ����ԭ����������ȥ���أ��Լ���дһ��selenium������
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        self.browser.get(request.url)
        # page_source �Ǵ��˶�̬���ݵ���ҳԴ���룬��ֱ���������������Դ���벻һ��,ֱ���������������ֻ�о�̬����
        # ͨ�����������֮��ֱ�ӷ�����Ӧ����������ͨ�����洫�ݸ�������
        return HtmlResponse(url=request.url, body=self.browser.page_source,
                            request=request, encoding='utf-8')

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


