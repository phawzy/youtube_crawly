# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from youtube.items import YoutubeItem
from scrapy_splash import SplashRequest

class ChannelWebzeroSpider(Spider):
    name = 'channel_webzero'
    allowed_domains = ['https://www.youtube.com/user/OsamaElzero/videos']
    start_urls = ['https://www.youtube.com/user/OsamaElzero/videos/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )


    def parse(self, response):
        html = response.body
        #titles = hxs.select("//span[@class='pl']")
        #for titles in titles:
        #    title = titles.select("a/text()").extract()
        #    link = titles.select("a/@href").extract()
        #    print title, link
        print "1111111111111111111111111111111111"
        #print hxs
        with open("channelhtml.log", "wb") as f:
            f.write(html)
