import scrapy
from ..items import MovieItem

class MovieSpider(scrapy.Spider):
    name = 'movies'  # unique

    start_urls = [
        'https://www.rottentomatoes.com/top/bestofrt/?year=2020'
    ]

    # this ll be start urls
    # start_urls = [
        # f'https://www.rottentomatoes.com/top/bestofrt/?year={i}' for i in reversed(range(1990, 2021))
    # ]


    def parse(self, response):
        # movie_links = response.css('#top_movies_main .articleLink::attr(href)').extract()

        for href in response.css('#top_movies_main .articleLink::attr(href)'):
            url = response.urljoin(href.extract())
            # pogadjamo dobar url
            print(f"Before yield on page: {url}")
            yield scrapy.Request(url, callback = self.parse_individual_movie)

    def parse_individual_movie(self, response):
        item = MovieItem()
        item['name'] = response.css('.mop-ratings-wrap__title--top::text').get()
        item['flag'] = response.css('.clearfix:nth-child(1) .meta-value::text').get().replace('\n', '').strip()
        item['genre'] = response.css('.genre::text').get().replace(' ', '').replace('\n', '').replace('and', ',').split(',')
        item['original_language'] = response.css('.clearfix:nth-child(3) .meta-value::text').get().replace('\n', '').strip()
        item['release_date'] = response.css('.clearfix:nth-child(7) time::text').get()

        # runtime = response.css('.clearfix:nth-child(10) time::text').get()


        # item['runtime'] = response.css('.clearfix:nth-child(10) time::text').get().strip()
        item['tomatometer'] = response.css('#tomato_meter_link .mop-ratings-wrap__percentage::text').get().strip()

        yield item

    # shouldnt use this for every string    
    def clear_string(self, string) -> str:
        # za obican string
        string = string.replace('\n', '')
        string = string.replace(' ', '')

        return string

    def clear_list(self, string, delimeter: str) -> list:
        string = self.clear_string(string)
        return string.split(delimeter)







            


