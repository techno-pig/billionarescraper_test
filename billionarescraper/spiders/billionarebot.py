import scrapy
import datetime as dt

class BillionarebotSpider(scrapy.Spider):
    name = 'billionarebot'
    allowed_domains = ['www.forbes.com/worlds-billionaires/']
    start_urls = ['https://www.forbes.com/worlds-billionaires/?sh=5a9eca9d5864']

    def parse(self, response):
    	dates = response.xpath('//article/div/div/@data-date').extract()
    	titles = response.xpath('//article/div/h3/a/text()').extract()
    	links = response.xpath('//article/div/h3/a/@href').extract()
    	

    	for item in zip(dates,titles,links):

            scraped_info = {
                'date' : dt.datetime.fromtimestamp(int(item[0])/1000),
                'title' : item[1],
                'link' : item[2]
            }

            yield scraped_info

