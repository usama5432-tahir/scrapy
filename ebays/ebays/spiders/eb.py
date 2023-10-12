import scrapy
import scraper_api
import csv

client = scraper_api.ScraperAPIClient('804ef4ac97441c08e351a3255c8e96c6')

class EbSpider(scrapy.Spider):
    name = 'eb'
    allowed_domains = ['ebay.com']

    # Define a list of keywords to scrape
    keywords = ['laptops']
    
    # Define the starting and ending page numbers
    start_page = 1
    end_page = 2  # Change this to the desired ending page number

    def start_requests(self):
        for keyword in self.keywords:
            for page in range(self.start_page, self.end_page + 1):
                start_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={keyword}&_sacat=0&page={page}'
                yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
        if product_links:
            for url in product_links:
                yield scrapy.Request(url, callback=self.parse_page)
        next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
        if next_page and self.page_within_range(next_page):
            yield scrapy.Request(next_page, callback=self.parse)

    def page_within_range(self, page_url):
        page_number = int(page_url.split('page=')[1])
        return self.start_page <= page_number <= self.end_page

    def parse_page(self, response):
        storename = response.xpath('//span[@class="ux-textspans ux-textspans--PSEUDOLINK ux-textspans--BOLD"]/text()').get()
        storelink = response.xpath('//div[@class="ux-seller-section__item--seller"]/a[1]/@href').get()
        name = response.xpath('(//div[@class="vim d-business-seller"]//div[@class="ux-layout-section-module"]//span[@class="ux-textspans"])[2]/text()').get()

        phone_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Phone:')]/following-sibling::span/text()")
        if phone_elements:
            phone = phone_elements[0].get()
        else:
            phone = None

        email_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Email:')]/following-sibling::span/text()")
        if email_elements:
            email = email_elements[0].get()
        else:
            email = None

        # if phone or email:
        yield {
                "Store Name": storename,
                "Store Link": storelink,
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Link": response.url
            }
