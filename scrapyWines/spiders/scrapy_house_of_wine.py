import scrapy
from scrapyWines.items import HouseOfWinesItem
from scrapy.loader import ItemLoader
import re
import pandas as pd 

def get_urls():
    path = '/home/alex/Documents/pythonProyectoFinal/scrapyWines/scrapyWines/temp/houseofwineFinale.txt'
    with open(path) as file:
       
        urls = list(map(lambda x: x.replace('\n','').replace(" ",""),file.readlines()))
    return urls  

class SpyderHouseWines(scrapy.Spider):
    name ="spider_house_wines"


    def is_year(self,year):
        regex = r'.*([1-3][0-9]{3})'
        match = re.search(regex,year)
        return match

    def is_percent(self,string):
        return string.endswith('%')
    
    def is_volume(self,string):
        return string.endswith('ml')

    def start_requests(self):
        urls= get_urls()[20:]

        print(urls)

        for url in urls:
            yield scrapy.Request(url)
        
    def parse(self,response):
        product_name = response.css('div.product-name > h1::attr(title)').extract_first()
        availability = response.css('span.backorder::text').extract_first()
        price = response.css('span.regular-price > span.price::text').extract_first()
        price_discount = response.css('li.tier-0 > span.price::text').extract_first()
        producer_and_grape_var = response.css('tr > td  > a ::text').extract()
        data = {
            "product_name": product_name if product_name is not None else "" ,
        

            "availability" : availability if availability is not None else "",
        
            "price" : price[1:] if price is not None else "",
        
            "price_discount" : price_discount[1:] if price_discount is not None else "",  

            "producer" : producer_and_grape_var[0] if len(producer_and_grape_var)>0 else "",
            "grape_variety" :  producer_and_grape_var[1] if len(producer_and_grape_var)>0 else "",

            
        }
        table_data= response.css('tr>td.data::text').extract()
        for row in table_data:
            
            if self.is_year(row) is not None:
                match = self.is_year(row)
                data["year"] = match.group(0)[-4:] 
                          
            elif self.is_volume(row):
                data["volume_mlt"]= row 
                
            elif self.is_percent(row): 
                data["alcohol_percent"] = row
        
        posible_none_keys= ["year","volume_mlt","alcohol_percent"]
        for keys in posible_none_keys:
            if data.get(keys) is None:
                data[keys]= ""
        
        #print(f" product name: { response.css('div.product-name > h1::attr(title)').extract()}")
        #print(f"alcohol_percet: {response.css('tr>td.dat::text').extract()[12]}")
        #df = pd.DataFrame(data)
        

        print(f"que se {data}")
        with open("temp/housewines.txt",mode='a+') as file: 
            file.write(','.join(data.values()))
            file.write('\n')      
        #yield producto_loader.load_item()
        #print("que se yo")
        #print(producto_imprimir)




   


