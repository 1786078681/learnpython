# -*- coding: utf-8 -*-
import scrapy


class Xh2Spider(scrapy.Spider):
    name = 'xh2'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://xiaohuar.com/']

    def parse(self, response):
        pass
