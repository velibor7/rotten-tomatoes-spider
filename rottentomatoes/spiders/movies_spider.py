import scrapy
from ..items import MovieItem

class MovieSpider(scrapy.Spider):
    name = 'movies'  # unique

    start_urls = [
        'https://www.rottentomatoes.com/top/bestofrt/?year=2020'
    ]

    # praticemo sve liknove imena, i sa te stranice cemo da skidamo sve
    # ne marimo za godine
    # for loop za sve ce da ide od ~1960 do 2020 i tako cemo kroz sve da prodjemo

    def parse(self, response):

        # movie_links = response.css('#top_movies_main .articleLink::attr(href)').extract()

        for href in response.css('#top_movies_main .articleLink::attr(href)'):
            url = response.urljoin(href.extract())
            # pogadjamo dobar url
            yield scrapy.Request(url, callback = self.parse_individual_movie)

    def parse_individual_movie(self, response):
        item = MovieItem()
        item['name'] = response.css('.mop-ratings-wrap__title--top::text').get()
        item['tomatometer'] = response.css('#tomato_meter_link .mop-ratings-wrap__percentage::text').get()
        yield item






            


