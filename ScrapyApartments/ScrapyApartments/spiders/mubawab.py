import scrapy


class MubawabSpider(scrapy.Spider):
    name = "mubawab"
    allowed_domains = ["www.mubawab.tn"]
    start_urls = ["https://www.mubawab.tn/fr/sc/appartements-a-vendre"]

    def parse(self, response):
        pass
