# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 职称
    title = scrapy.Field()
    # 个人简历
    info = scrapy.Field()

