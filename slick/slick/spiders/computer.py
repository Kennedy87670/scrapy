import scrapy
from scrapy.selector import Selector 
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys

class ComputerSpider(scrapy.Spider):
    name = 'computer'

    # def remove_characters(self, value):
    #     return value.strip('\xa0')
    
    def start_requests(self):
        yield SeleniumRequest(
            url= 'https://slickdeals.net/computer-deals/',
            wait_time= 3,
            callback= self.parse
        )

    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals blueprint']/li")
        for product in products:
            yield{
                'name': product.xpath("//a[@class='itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'link': product.xpath("//a[@class='itemTitle bp-p-dealLink bp-c-link']/href").get(),
                'Store-name': product.xpath("normalize-space(.//span[@class='blueprint']/button/text())").get(),
                'Price': product.xpath("normalize-space(.//div[@class='priceLine']/div/text())").get()
            }
        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            absolute_url = f"https://slickdeals.net{next_page}"
            yield  SeleniumRequest(
                url = absolute_url,
                wait_time= 3,
                callback = self.parse
            )

# //div[@class='pagination buttongroup']/a