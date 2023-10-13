import scrapy

import csv


class WatchesSpider(scrapy.Spider):
    name = 'watches'
    allowed_domains = ['ebay.com']

    # Define a list of keywords to scrape
    keywords = ['watches']

    def start_requests(self):
        for keyword in self.keywords:
            # Construct the start URL with the current keyword
            start_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={keyword}&_sacat=0'
            yield scrapy.Request(url=start_url, callback=self.parse, meta={'page_number': 1})

    def parse(self, response):
        page_number = response.meta['page_number']
        product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
        if product_links:
            for url in product_links:
                yield scrapy.Request(url, callback=self.parse_page, meta={'page_number': page_number})

        next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
        if next_page:
            page_number += 1
            yield scrapy.Request(next_page, callback=self.parse, meta={'page_number': page_number})

    def parse_page(self, response):
        page_number = response.meta['page_number']
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

        if phone or email:
            yield {
                "Store Name": storename,
                "Store Link": storelink,
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Link": response.url,
                "Page Number": page_number
            }