import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True, process_request='set_user_agent')
    )
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield{
            'title': response.xpath("//div[@class='sc-80d4314-1 fbQftq']/h1/text()").get(),
            'year': response.xpath("//span[@class='sc-8c396aa2-2 itZqyK']/text()").get(),
            'duration': response.xpath("//li[@class='ipc-inline-list__item']/text()").get(),
            'rating': response.xpath("(//span[@class='sc-7ab21ed2-1 jGRxWM'])/text()").get(),
            'movie_url': response.url
            # 'user-agent': response.request.headers["User-Agent"]
        }
        print(response.url)

# scrapy crawl best_movies