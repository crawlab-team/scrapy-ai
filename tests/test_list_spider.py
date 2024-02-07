from scrapy.crawler import CrawlerProcess

from scrapy_ai import ListSpider


class TestSpider(ListSpider):
    name = 'test_spider'
    start_urls = ['https://movie.douban.com/top250']


def test_spiders():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    })
    process.crawl(TestSpider)
    process.start()
