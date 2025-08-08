
# import scrapy
# from ..items import ToscrapeItem

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://books.toscrape.com/'
#     ]
    
#     def parse(self, response):
#         all_div_quotes = response.css('article.product_pod')

#         for quote_div in all_div_quotes:
#             items = ToscrapeItem()

#             name = quote_div.css('h3 a::attr(title)').get()
#             price = quote_div.css('.price_color::text').get()
            
#             # avability = quote_div.css('.instock.availability::text').get()
            

#             # Clean availability using list comprehension
#             availability_list = quote_div.css('.instock.availability::text').getall()
#             avability = ''.join([text for text in availability_list if text.strip()])
#             print(avability)

#             items['name'] = name
#             items['price'] = price
#             items['avability'] = avability

#             yield items


import scrapy
from ..items import ToscrapeItem  # Uncommented this line

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://books.toscrape.com/'
    ]
    
    def parse(self, response):
        all_div_quotes = response.css('article.product_pod')

        for quote_div in all_div_quotes:
            items = ToscrapeItem()

            name = quote_div.css('h3 a::attr(title)').get()
            price = quote_div.css('.price_color::text').get()

            # Extract and clean availability text
            availability = quote_div.css('.instock.availability::text').getall()
            availability = ''.join(text.strip() for text in availability if text.strip())

            items['name'] = name
            items['price'] = price
            items['avability'] = availability

            yield items

            next_page = response.css('li.next a::attr(href)').get()

            if next_page is not None:
                yield response.follow(next_page , callback = self.parse)
