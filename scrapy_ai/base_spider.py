import os

import scrapy


class BaseSpider(scrapy.Spider):
    _api_endpoint: str = os.getenv('CRAWLAB_AI_API_ENDPOINT') or 'https://crawlab-ai.azurewebsites.net'
