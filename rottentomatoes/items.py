# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    genre = scrapy.Field()
    tomatometer = scrapy.Field() # percent and total count
    audience_score = scrapy.Field() 