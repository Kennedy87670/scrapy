import scrapy


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoinwatch.com']
    start_urls = ['http://www.livecoinwatch.com/']

    def parse(self, response):
        pass
