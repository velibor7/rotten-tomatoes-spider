# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    flag = scrapy.Field() #rating on website should be named flag
    genre = scrapy.Field()
    original_language = scrapy.Field()
    release_date = scrapy.Field()
    # runtime = scrapy.Field()
    tomatometer = scrapy.Field() # percent and total count
    