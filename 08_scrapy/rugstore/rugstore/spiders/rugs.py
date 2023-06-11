import scrapy
from ..items import RugstoreItem

class AllrugsSpider(scrapy.Spider):
    name = 'rugs'
    allowed_domains = ['therugshopuk.co.uk']
    start_urls = ['https://www.therugshopuk.co.uk/rugs-by-type/rugs.html']

    def parse(self, response):
        items = RugstoreItem()

        for item in response.css('div.product-item-info'):
            title = item.css('img.product-image-photo.image::attr(alt)').get()
            link = response.css('a.product-item-link::attr(href)').get(),
            price = response.css('span.price::text').get()

            items['title'] = title
            items['link'] = link
            items['price'] = price

            yield items
        
        ### Dealing with pagenated sites ###
        # next_page = response.css('a[title=Next]::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback = self.parse)