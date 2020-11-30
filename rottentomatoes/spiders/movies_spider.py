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
        items = MovieItem()

        raw = response.css('#top_movies_main .articleLink::text').extract()
        movie_names = []

        for movie in movies:
            movie_names.append(movie.strip())
            


