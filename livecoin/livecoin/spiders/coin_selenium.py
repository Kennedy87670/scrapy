import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoinwatch.com']
    start_urls = ['http://www.livecoinwatch.com/']

    # def parse(self, response):
    #     pass
    def __init__(self):
        chrome_options =Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.get("http://www.livecoinwatch.com")
