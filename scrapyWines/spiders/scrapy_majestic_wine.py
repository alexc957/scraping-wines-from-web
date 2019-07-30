import scrapy
from scrapyWines.items import MajesticWine
from scrapy.loader import ItemLoader
import re
import pandas as pd 

def get_urls():
    path = '/home/alex/Documents/pythonProyectoFinal/scrapyWines/scrapyWines/temp/majesticUrls.txt'
    with open(path) as file:
       
        urls = list(map(lambda x: x.replace('\n',"").replace(" ",""),file.readlines()))
    return urls  

class SpyderHouseWines(scrapy.Spider):
    name ="spider_majestic_wines"
    
    def is_year(self,year):
        regex = r'.*([1-3][0-9]{3})'
        match = re.search(regex,year)
        return match


    def start_requests(self):
        urls = get_urls()
            
     
     
        for url in urls:
            yield scrapy.Request(url)
     
    def parse(self,response):
        selector = response.css('table')[0]
        values = selector.css('tr:not([class^="show-for-small-only"]) > td.content-table__text::text').extract()
        print(f"values len is  {len(values)}")
        if len(values)>3:
                product_name = response.css('h1.product-info__name::text').extract_first()  
                price =  response.css('span.product-action__price-info::text').extract() 
                discount_price=  response.css('span.product-action__price-text::text').extract()  
                producer = ""
                grape_variety= values[0]
                wine_color = selector.css('tr >  td.content-table__text > a ::text').extract_first()
                year =  self.is_year(product_name).group(0) if self.is_year(product_name) is not None else "" 
                alcohol_percent = list(filter(lambda x: x.endswith('%'),values))[0]
                country=  response.css('div.product-info__symbol--country >  div.product-info__symbol-label::text').extract()[0]
               
                #print(f"data is {data}") 


                print("aqui creamos el ItemLoader")
                wine_loader = ItemLoader(
                    item=MajesticWine(),
                    

                )

                wine_loader.add_value(
                    'product_name',
                    product_name
                )
                wine_loader.add_value(
                    'price',
                     price[0]
                )

                wine_loader.add_value(
                    'discount_price',
                    discount_price[0]
                )
                wine_loader.add_value(
                    'producer',
                    producer
                )

                wine_loader.add_value(
                    'grape_variety',
                    grape_variety
                )

                wine_loader.add_value(
                    'wine_color',
                    wine_color

                )

                wine_loader.add_value(
                    'year',
                    year
                )

                wine_loader.add_value(
                    'alcohol_percent',
                    alcohol_percent
                )

                wine_loader.add_value(
                    'country',
                    country
                )
                print("espero que cargue el item")
                print(wine_loader.load_item())
                yield wine_loader.load_item()



