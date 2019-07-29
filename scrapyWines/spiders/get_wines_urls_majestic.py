import scrapy

def get_urls():
    base_url = 'https://www.majestic.co.uk/wine?pageNum=pageNumber&pageSize=12'
    return [base_url.replace('pageNumber',str(page_number)) for page_number in range(0,61) ]
    #for page in range(0,176,25):




class SpydeGetLinksWinesGr(scrapy.Spider):
   
    name ="spyder_get_url_majestic"

    def start_requests(self):
        urls = get_urls() 
        for url in urls:
            yield scrapy.Request(url=url)
    
    def parse(self,response):
        wines_urls = response.css('h3.space-b--none > a::attr(href)').extract()
        path = '/home/alex/Documents/pythonProyectoFinal/scrapyWines/scrapyWines/temp/'
        with open(path+"majesticUrls.txt",mode='a+') as file:
            for url in wines_urls:
                file.write('https://www.majestic.co.uk'+url+" \n")
