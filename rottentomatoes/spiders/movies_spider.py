import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movies'  # unique

    start_urls = [
        'https://www.rottentomatoes.com/top/bestofrt/?year=2020'
    ]

    # def parse(self, response):
    # = response.url.split('/')[-1]
