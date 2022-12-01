import scrapy
from scrapy.selector import Selector 
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
class ExampleSpider(scrapy.Spider):
    name = 'example'
    
    def start_requests(self):
        yield SeleniumRequest(
            url ='https://duckduckgo.com',
            wait_time= 3,
            screenshot=True,
            callback = self.parse
        )

    def parse(self, response):
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath("//input[@id='search_form_input_homepage']")
        search_input.send_keys('hello World')

        # driver.save_screenshot('after_filling_input.png')
        search_input.send_keys(Keys.ENTER)

        # to get the page details
        html = driver.page_source
        response_obj = Selector(text=html)

        # driver.save_screenshot('ENTER.png')
        links = response_obj.xpath("//div[@class='ikg2IXiCD14iVX7AdZo1']/h2/a")
        for link in links:
            yield{
                'URL': link.xpath('.//@href').get()
            }
