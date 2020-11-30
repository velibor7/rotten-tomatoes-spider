import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movies'  # unique

    start_urls = [
        'https://www.rottentomatoes.com/top/bestofrt/?year=2020'
    ]

    # def parse(self, response):
    # = response.url.split('/')[-1]

    # movies = response.css('#top_movies_main .articleLink::text').extract()
    # clear_movies = []
    # for movie in movies:
        # clear_movies.append(movie.strip())


