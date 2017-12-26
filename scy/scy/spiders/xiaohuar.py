# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    visited_set = set()

    def parse(self, response):
        self.visited_set.add(response.url)
        print(response)
        hxs = HtmlXPathSelector(response)
        item_list = hxs.select('//div[@class="item masonry_brick"]')
        # // 子子孙孙,
        for item in item_list:
            # print(item)
            v = item.select('.//span[@class="price"]/text()').extract_first()
            print(v)
            # .// 当前找,  text() 文本, list=extract(), str= extract_first()
        page_list = hxs.select('//a[re:test(@href,"http://www.xiaohuar.com/list-1-\d+.html")]/@href').extract()
        # /@href, get this property "href='...' "
        # for page in page_list:
        #     print(page)
        for url in page_list:
            if url not in self.visited_set:

                obj = Request(url=url, method='GET', callback=self.parse)
                yield  obj