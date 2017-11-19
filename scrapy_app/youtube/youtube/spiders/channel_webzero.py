# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from youtube.items import YoutubeItem
from scrapy_splash import SplashRequest
import re

class ChannelWebzeroSpider(Spider):
    name = 'channel_webzero'
    allowed_domains = ['www.youtube.com']

    def __init__(self, domain='', *args, **kwargs):
        super(ChannelWebzeroSpider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )


    def parse(self, response):
        
        htx = Selector(response)
        videos = htx.xpath("//ol[contains(@id,'playlist-autoscroll-list')]" \
        "//li[contains(@class,'yt-uix-scroller-scroll-unit')]")
        for video in videos:
            video_item = YoutubeItem()
            video_item['thumbnail_url'] = video.xpath("a//img/@src").extract_first()
            url = video.xpath("a/@href").extract_first()
            video_item['url'] = "https://www.youtube.com" + url
            video_item['title'] = video.xpath("a/div[contains(@class,'playlist-video-description')]/h4/text()").extract_first()
            request = SplashRequest(video_item['url'], self.parse_video,
                endpoint='render.html',
                args={'wait': 1})
            request.meta['item'] = video_item
            yield request

    def parse_video(self, response):
        video_resonse = Selector(response)
        video_item = response.meta['item']        
        views_txt = video_resonse.xpath("//div[contains(@class,'watch-view-count')]/text()").extract_first()
        video_item['views'] = re.findall('\d+', views_txt.replace(",", ""))[0]
        yield video_item

        