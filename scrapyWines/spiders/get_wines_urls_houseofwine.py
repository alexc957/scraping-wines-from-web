import scrapy

def get_urls():
    base_url = 'https://www.houseofwine.gr/how/intl/wine.html?p=pageNumber'
    return [base_url.replace('pageNumber',str(page_number)) for page_number in range(0,38) ]
    #for page in range(0,176,25):




class SpydeGetLinksWinesGr(scrapy.Spider):
   
    name ="spyder_get_url_gr"

    def start_requests(self):
        urls = get_urls() 
        for url in urls:
            yield scrapy.Request(url=url)
    
    def parse(self,response):
        wines_urls = response.css('h2.product-name > a::attr(href)').extract()
        path = '/home/alex/Documents/pythonProyectoFinal/scrapyWines/scrapyWines/temp/'
        with open(path+"houseofwineUrls.txt",mode='a+') as file:
            for url in wines_urls:
                file.write(url+" \n")
