import scrapy


class SpidermonkeySpider(scrapy.Spider):
    name = "spidermonkey"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://amazon.com"]

    def parse(self, response):
        pass
