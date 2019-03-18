import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from scrapy.selector import Selector

class ParaIrnosSpider(CrawlSpider):
    name = 'parairnos'

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        print()
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        ParaIrnosSpider.rules = [
           Rule(LinkExtractor(allow =(), restrict_xpaths = ('//ul[@class="pagination pagination-blue pagination-lg"]/li[last()]/a'))),
           Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[@class="results-content"]/div/a')),callback= 'parse_item', follow=False)
        ]
        super(ParaIrnosSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        # You can tweak each crawled page here
        # Don't forget to return an object.
        imagen = response.xpath('//div[@class="fotorama"]/a/@href').get()
        titulo= response.xpath('//h1[@itemprop="name"]/text()').get()
        direccion= response.xpath('//span[@itemprop="streetAddress"]/text()').get()
        #print("IMAGEN: "+imagen)
        #print("TITULO: "+titulo)
        #print("DIRE: "+direccion)
        arreglo = {}
        arreglo['imagen']=imagen
        arreglo['titulo']=titulo
        arreglo['url'] = response.url
        arreglo['direccion'] = direccion
        return arreglo