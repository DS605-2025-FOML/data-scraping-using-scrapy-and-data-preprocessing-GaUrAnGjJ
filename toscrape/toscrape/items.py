# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    avability = scrapy.Field()
    
