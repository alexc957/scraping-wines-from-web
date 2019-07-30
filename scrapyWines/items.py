# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
import re 

def get_item_price(text_price):
    regex = r"(\d+\.\d{1,})"
    return float(re.search(regex,text_price).group(0))

def get_percent(percent):
    return percent.split('%')[0]

def get_year(year):
    return year[-4:]
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


class  MajesticWine(scrapy.Item):
    product_name = scrapy.Field(output_processor = TakeFirst()) 
    price= scrapy.Field( 
        input_processor= MapCompose(
            get_item_price
        ),
        output_processor = TakeFirst() )
    discount_price= scrapy.Field(
         input_processor= MapCompose(
            get_item_price
        ),
        output_processor = TakeFirst() 
    )
    producer= scrapy.Field(output_processor = TakeFirst())
    grape_variety= scrapy.Field(output_processor = TakeFirst())
    wine_color= scrapy.Field( output_processor = TakeFirst())
    year= scrapy.Field(
         input_processor= MapCompose(
            get_year
        ),
        output_processor = TakeFirst() 
    )
    alcohol_percent= scrapy.Field(
         input_processor= MapCompose(
            get_percent
        ),
        output_processor = TakeFirst() 
    )
    country = scrapy.Field( output_processor = TakeFirst())
                



