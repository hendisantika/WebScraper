import scrapy

class Tes1(scrapy.Spider):
    name = "tes"
    start_urls = [
        'http://olx.co.id/properti/rumah/',
    ]

    def parse(self, response):
                for items in response.xpath('//table[@id="offers_table"]/tbody/tr/td/table/tbody'):
                # for items in response.xpath('//table[@id="offers_table"]/tbody/tr/td/table/tbody/tr/td/div/p/strong'):
                    # print 'price: ', items.xpath('./tr/td[4]/div/p/strong/text()').extract()
                    # print 'url: ', items.xpath('./tr/td[3]/h3/a/@href').extract()
                    # print 'title: ', items.xpath('./tr/td[3]/h3/a/span/text()').extract()
                    
                    
                    yield {
                        'url': items.xpath('./tr/td[3]/h3/a/@href').extract_first().strip(),
                        'title': items.xpath('./tr/td[3]/h3/a/span/text()').extract_first().strip(),
                        'price': items.xpath('./tr/td[4]/div/p/strong/text()').extract_first().strip(),
                        #'description' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                        #'source' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                        'posted' : items.xpath('./tr/td/p/text()').extract_first().strip(),
                        #'type' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                        'city' : items.xpath('./tr/td/p/small/span/text()').extract_first().strip(),
                        #'area' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                        #'apartment' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                        #'luas' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                        #'certificate' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                        
                    }

              


