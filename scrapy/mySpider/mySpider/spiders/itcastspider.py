# _*_ coding:utf-8 _*_

import scrapy

class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫实际的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

    def parse(self,response):
        # 注意要用‘wb+’的方式打开文件，否则会报错write() argument must be str, not bytes
        with open("itcast.html","wb+") as f:
            f.write(response.body)
