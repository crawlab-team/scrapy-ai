from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_ai import AISpider


class TestSpider(AISpider):
    start_urls = ['https://books.toscrape.com']


def test_spiders():
    process = CrawlerProcess(get_project_settings())
    process.crawl(TestSpider)
    process.start()
