# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    duration = scrapy.Field()
    views = scrapy.Field()
    thumbnail_url = scrapy.Field()
    images_url = scrapy.Field()
