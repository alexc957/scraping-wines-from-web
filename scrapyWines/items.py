# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapywinesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HouseOfWinesItem(scrapy.Item):
    product_name = scrapy.Field()
    availability = scrapy.Field()
    price = scrapy.Field()
    price_discount  = scrapy.Field()
    producer=scrapy.Field()
    wine_color = scrapy.Field() 
    vintage = scrapy.Field()
    country = scrapy.Field()
    grape_variety = scrapy.Field()
    volume_mlt = scrapy.Field()
    dryness = scrapy.Field() 
    alcohol_percent = scrapy.Field()


