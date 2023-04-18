import scrapy


class AdondevivirSpider(scrapy.Spider):
    name = "adondevivir"
    allowed_domains = ["adondevivir.com"]
    start_urls = ["http://adondevivir.com/"]

    def parse(self, response):
        pass
