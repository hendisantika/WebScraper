#UDAH OKE UNTUK INSERT INTO MYSQL DB NYA MAH
#TINGGAL NEXT PAGE

import scrapy
import MySQLdb

class Tes1(scrapy.Spider):
    name = "tes4"
    start_urls = [
        'http://olx.co.id/mobil/',
    ]

        

    def __init__(self):
        self.db = MySQLdb.connect("127.0.0.1", "root", "root", "olx")
        self.stmt = "insert into cars(url, title, price, posted, city) values(%s, %s, %s, %s, %s)"

    def parse(self, response):
        c = self.db.cursor()
            # for items in response.xpath('//table[@id="offers_table"]/tbody/tr/td/table/tbody/tr/td[3]/h3/a/@href'):
            # for items in response.xpath('//table[@id="offers_table"]/tbody/tr/td/table/tbody/tr/td/div/p/strong'):
                # print 'price: ', items.xpath('./tr/td[4]/div/p/strong/text()').extract()
                # print 'url: ', items.xpath('./tr/td[3]/h3/a/@href').extract()
                # print 'title: ', items.xpath('./tr/td[3]/h3/a/span/text()').extract()
        urls = response.xpath('//table[@id="offers_table"]/tbody/tr/td/table/tbody/tr/td[3]/h3/a/@href').extract()
        for url in urls:
            absolute_url = response.urljoin(url)
            request = scrapy.Request(
                absolute_url, callback=self.parse_cars)
            yield request

            # title = response.xpath(
            #     '//*[@id="offer_active"]/div/div/div/div/h1/text()').extract_first()
            # price = response.xpath(
            #             '//*[@id="offeractions"]/div/div/div/strong/text()').extract_first()
            # city = response.xpath(
            #             '//*[@id="offer_active"]/div/div/div/div/p/span/span/strong/a/text()').extract_first()
            # posted = response.xpath(
            #             '//*[@id="offer_active"]/div/div/div/div/p/small/span/text()').extract_first()
            # cp = response.xpath(
            #             '//*[@id="offeractions"]/div/div/div/div/p/span/text()').extract_first()
            # desc = response.xpath(
            #             '//*[@id="textContent"]/p/text()').extract_first()
        #     c.execute("insert into cars(url, title, price, posted, city, contact_person, desc) values(%s, %s, %s, %s, %s)", (url, title, price, posted, city, cp, desc))
        # self.db.commit()
            # print('url :  ', urls)
            # print('title : ', title)

        # process next page
        # next_page_url = response.xpath('//*[@id="body-container"]/div/div/div/span/a/@href').extract_first()
        next_page_url = response.xpath('//*[@id="body-container"]/div/div/div/span/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        request = scrapy.Request(absolute_next_page_url)
        yield request
        
                
                #yield {
                #'url': items.xpath('./tr/td[3]/h3/a/@href').extract(),
                #'title': items.xpath('./tr/td[3]/h3/a/span/text()').extract(),
                #'price': items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #'description' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #'sourceSite' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #'posted' : items.xpath('./tr/td/p/text()').extract(),
                #'type' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #'city' : items.xpath('./tr/td/p/small/span/text()').extract(),
                #'area' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #'apartmentName' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #'luas' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #'certificate' : items.xpath('./tr/td[4]/div/p/strong/text()').extract(),
                #}

                # url = items.xpath('./tr/td[3]/h3/a/@href').extract()[0].strip()
                # title = items.xpath('./tr/td[3]/h3/a/span/text()').extract()[0].strip()
                # price = items.xpath('./tr/td[4]/div/p/strong/text()').extract()[0].strip()
                # posted =  items.xpath('./tr/td/p/text()').extract()[0].strip()
                # city = items.xpath('./tr/td/p/small/span/text()').extract()[0].strip()
                # cp = items.xpath('//*[@id="offeractions"]/div/div/div[3]/div/p/span[1]/text()').extract()[0].strip()
                # c.execute("insert into cars(url, title, price, posted, city, contact_person) values(%s, %s, %s, %s, %s)", (url, title, price, posted, city))
            #     c.execute("insert into cars(url, title, price, posted, city) values(%s, %s, %s, %s, %s)", (url, title, price, posted, city))
            # self.db.commit()

    def parse_cars(self, response):
        c = self.db.cursor()
        title = response.xpath(
            '//*[@id="offer_active"]/div/div/div/div/h1/text()').extract_first().strip()
        price = response.xpath(
            '//*[@id="offeractions"]/div/div/div/strong/text()').extract_first().strip()
        city = response.xpath(
            '//*[@id="offer_active"]/div/div/div/div/p/span/span/strong/a/text()').extract_first()
        posted = response.xpath(
            '//*[@id="offer_active"]/div/div/div/div/p/small/span/text()').extract_first().strip()
        cp = response.xpath(
            '//*[@id="offeractions"]/div/div/div/div/p/span/text()').extract_first().strip()
        desc = response.xpath(
            '//*[@id="textContent"]/p/text()').extract_first().strip()

        c.execute("insert into cars(url, title, price, posted, city, contact_person, description) values(%s, %s, %s, %s, %s, %s, %s)", (response.url, title, price, posted, city, cp, desc))
        self.db.commit()    

        cars = {
            'title': title,
            'price': price,
            'city': city,
            'posted': posted,
            'cp'    : cp,
            'desc'  : desc,
            'url': response.url}
            # 'url': url}
        yield cars                 

            # next_page_url = response.xpath('//*[@id="body-container"]/div/div/div/span/a/@href').extract_first()
            # if next_page_url is not None:
            #         yield scrapy.Request(response.urljoin(next_page_url))

    # def parse_restaurant(self, response):
    #     url = response.xpath(
    #         '//div[@class="mapContainer"]/@data-name').extract_first()
    #     rating = response.xpath(
    #         '//img[@property="ratingValue"]/@content').extract_first()
    #     latitude = response.xpath(
    #         '//div[@class="mapContainer"]/@data-lat').extract_first()
    #     longitude = response.xpath(
    #         '//div[@class="mapContainer"]/@data-lng').extract_first()
    #     cars = {
    #             'url': url,
    #             'title': title,
    #             'price': price,
    #             'posted': posted,
    #             'city' : city,
    #             'url2': response.url}
    #     yield cars  


 

              

