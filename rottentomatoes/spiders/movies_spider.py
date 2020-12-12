import scrapy
from ..items import MovieItem

class MovieSpider(scrapy.Spider):
    name = 'movies'  # unique

    start_urls = [
        'https://www.rottentomatoes.com/top/bestofrt/?year=2020'
    ]

    # this'll be start urls
    # start_urls = [
        # f'https://www.rottentomatoes.com/top/bestofrt/?year={i}' for i in reversed(range(1990, 2021))
    # ]


    def parse(self, response):
        for href in response.css('#top_movies_main .articleLink::attr(href)'):
            url = response.urljoin(href.extract())
            print(f"Page: {url}")
            yield scrapy.Request(url, callback = self.parse_individual_movie)

    
    def parse_individual_movie(self, response):
        item = MovieItem()
        item['name'] = response.css('.mop-ratings-wrap__title--top::text').get()
        item['genre'] = response.css('.genre::text').get().replace(' ', '').replace('\n', '').replace('and', ',').split(',')
        item['tomatometer'] = response.css('#tomato_meter_link .mop-ratings-wrap__percentage::text').get().strip()
        item['audience_score'] = response.css('.audience-score .mop-ratings-wrap__percentage::text').get().strip()
        yield item
