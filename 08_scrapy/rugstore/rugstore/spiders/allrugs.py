import scrapy
from ..items import RugstoreItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class LoginSpider(scrapy.Spider):
    name = 'allrugs'
    allowed_domains = ['therugshopuk.co.uk']
    start_urls = ['https://www.therugshopuk.co.uk/rugs-by-type/rugs.html']

    def parse(self, response):
        # Go to login page
        login_page = response.css('.header_account_link::attr(href)').get()
        if login_page is not None:
            yield response.follow(login_page, callback = self.login)
    
    def login(self, response):
        print("\nLOGIN\n")
        # login
        token = response.css('div.login-container input[name="form_key"]::attr(value)').get()
        return FormRequest.from_response(
            response,
            formdata={
                'form_key': token,
                'username': 'horstannho@gmail.com',
                'password': 'Heymaesthe123',
                'send': ''
            },
            callback = self.go_clearence,
            dont_filter=True
        )
    
    def go_clearence(self, response):
        print("\nCLEARENCE\n")
        clearence_page = response.css('.ui-corner-all::attr(href)').get()
        if clearence_page is not None:
            yield response.follow(clearence_page, callback = self.scrape)

    def scrape(self, response):
        #open_in_browser(response)
        
        # start scraping in the clearence page
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