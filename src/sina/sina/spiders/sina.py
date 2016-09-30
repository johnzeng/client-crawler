# -*- coding: UTF-8 -*-
import scrapy
import urllib

class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["weibo.com"]
    query = urllib.quote("买猫")
    print "tttt %s"%query
    start_urls = [
        'http://s.weibo.com/weibo/%s&nodup=1' % query
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
