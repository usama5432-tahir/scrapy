# import scrapy

# class EbaySpider(scrapy.Spider):
#     name = 'ebay'
#     allowed_domains = ['ebay.com']
#     start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=cards&_sacat=0']

#     def parse(self, response):
#         product_links = response.css('.s-item__info.clearfix > a::attr(href)').getall()
#         if product_links:
#             for url in product_links:
#                 yield response.follow(url, callback=self.parse_page)
#         next_page = response.css('a.pagination__next.icon-link::attr(href)').get()
#         if next_page:
#             yield response.follow(next_page, callback=self.parse)

#     def parse_page(self, response):
#         storename = response.css('.ux-textspans.ux-textspans--PSEUDOLINK.ux-textspans--BOLD::text').get()
#         storelink = response.css('.ux-seller-section__item--seller > a:first-child::attr(href)').get()
#         name = response.xpath('(//div[@class="vim d-business-seller"]//div[@class="ux-layout-section-module"]//span[@class="ux-textspans"])[2]/text()').get()

#         # Uncomment and modify the following lines if you want to extract phone and email
#         phone_elements = response.css("div.ux-section__item span:contains('Phone:') + span::text")
#         if phone_elements:
#             phone = phone_elements[0].get()
#         else:
#             phone = None
        
#         email_elements = response.css("div.ux-section__item span:contains('Email:') + span::text")
#         if email_elements:
#             email = email_elements[0].get()
#         else:
#             email = None

#         yield {
#             "Store Name": storename,
#             "Store Link": storelink,
#             "Name": name,
#             "Phone": phone,
#             "Email": email,
#             "Link": response.url
#         }
# import scrapy
# import scraper_api

# client = scraper_api.ScraperAPIClient('804ef4ac97441c08e351a3255c8e96c6')

# class EbaySpider(scrapy.Spider):
#     name = 'ebay'
#     allowed_domains = ['ebay.com']
#     start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=cards&_sacat=0']

#     def parse(self, response):
#         product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
#         if product_links:
#             for url in product_links:
#                 yield scrapy.Request(url, callback=self.parse_page)
#         next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
#         if next_page:
#             yield scrapy.Request(next_page, callback=self.parse)

#     def parse_page(self, response):
#         storename = response.xpath('//span[@class="ux-textspans ux-textspans--PSEUDOLINK ux-textspans--BOLD"]/text()').get()
#         storelink = response.xpath('//div[@class="ux-seller-section__item--seller"]/a[1]/@href').get()
#         name = response.xpath('(//div[@class="vim d-business-seller"]//div[@class="ux-layout-section-module"]//span[@class="ux-textspans"])[2]/text()').get()

#         phone_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Phone:')]/following-sibling::span/text()")
#         if phone_elements:
#             phone = phone_elements[0].get()
#         else:
#             phone = None

#         email_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Email:')]/following-sibling::span/text()")
#         if email_elements:
#             email = email_elements[0].get()
#         else:
#             email = None

#         if phone or email:
#             yield {
#                 "Store Name": storename,
#                 "Store Link": storelink,
#                 "Name": name,
#                 "Phone": phone,
#                 "Email": email,
#                 "Link": response.url
#             } 
        
# import scrapy
# import scraper_api
# import csv

# client = scraper_api.ScraperAPIClient('804ef4ac97441c08e351a3255c8e96c6')

# class EbaySpider(scrapy.Spider):
#     name = 'ebay'
#     allowed_domains = ['ebay.com']


#     # Define a list of keywords to scrape
#     keywords = [ 'laptops', 'watches']

#     def start_requests(self):
#         for keyword in self.keywords:
#             # Construct the start URL with the current keyword
#             start_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={keyword}&_sacat=0'
#             yield scrapy.Request(url=start_url, callback=self.parse)

#     def parse(self, response):
#         product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
#         if product_links:
#             for url in product_links:
#                 yield scrapy.Request(url, callback=self.parse_page)
#         next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
#         if next_page:
#             yield scrapy.Request(next_page, callback=self.parse)

#     def parse_page(self, response):
#         storename = response.xpath('//span[@class="ux-textspans ux-textspans--PSEUDOLINK ux-textspans--BOLD"]/text()').get()
#         storelink = response.xpath('//div[@class="ux-seller-section__item--seller"]/a[1]/@href').get()
#         name = response.xpath('(//div[@class="vim d-business-seller"]//div[@class="ux-layout-section-module"]//span[@class="ux-textspans"])[2]/text()').get()

#         phone_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Phone:')]/following-sibling::span/text()")
#         if phone_elements:
#             phone = phone_elements[0].get()
#         else:
#             phone = None

#         email_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Email:')]/following-sibling::span/text()")
#         if email_elements:
#             email = email_elements[0].get()
#         else:
#             email = None

#         if phone or email:
#             yield {
#                 "Store Name": storename,
#                 "Store Link": storelink,
#                 "Name": name,
#                 "Phone": phone,
#                 "Email": email,
#                 "Link": response.url
#             }

#     def closed(self, reason):
#         # Store the scraped data in a CSV file and filter duplicates based on emails
#         with open('ebay_data.csv', 'w', newline='') as csv_file:
#             fieldnames = ["Store Name", "Store Link", "Name", "Phone", "Email", "Link"]
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#             writer.writeheader()

#             unique_emails = set()
#             for item in self.exported_items:
#                 email = item.get("Email")
#                 if email and email not in unique_emails:
#                     writer.writerow(item)
#                     unique_emails.add(email)
# import scrapy
# import scraper_api
# import csv

# client = scraper_api.ScraperAPIClient('804ef4ac97441c08e351a3255c8e96c6')

# class EbaySpider(scrapy.Spider):
#     name = 'ebay'
#     allowed_domains = ['ebay.com']


#     # Define a list of keywords to scrape
#     keywords = [ 'laptops']

#     def start_requests(self):
#         for keyword in self.keywords:
#             # Construct the start URL with the current keyword
#             start_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={keyword}&_sacat=0'
#             yield scrapy.Request(url=start_url, callback=self.parse)

#     def parse(self, response):
#         product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
#         if product_links:
#             for url in product_links:
#                 yield scrapy.Request(url, callback=self.parse_page)
#         next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
#         if next_page:
#             yield scrapy.Request(next_page, callback=self.parse)

#     def parse_page(self, response):
#         storename = response.xpath('//span[@class="ux-textspans ux-textspans--PSEUDOLINK ux-textspans--BOLD"]/text()').get()
#         storelink = response.xpath('//div[@class="ux-seller-section__item--seller"]/a[1]/@href').get()
#         name = response.xpath('(//div[@class="vim d-business-seller"]//div[@class="ux-layout-section-module"]//span[@class="ux-textspans"])[2]/text()').get()

#         phone_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Phone:')]/following-sibling::span/text()")
#         if phone_elements:
#             phone = phone_elements[0].get()
#         else:
#             phone = None

#         email_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Email:')]/following-sibling::span/text()")
#         if email_elements:
#             email = email_elements[0].get()
#         else:
#             email = None

#         if phone or email:
#             yield {
#                 "Store Name": storename,
#                 "Store Link": storelink,
#                 "Name": name,
#                 "Phone": phone,
#                 "Email": email,
#                 "Link": response.url
#             }
# import scrapy
# import csv

# class EbaySpider(scrapy.Spider):
#     name = 'ebay'
#     allowed_domains = ['ebay.com']

#     # Define a list of keywords to scrape
#     keywords = ['laptops', 'cards']

#     def start_requests(self):
#         for keyword in self.keywords:
#             # Construct the start URL with the current keyword
#             start_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={keyword}&_sacat=0'
#             yield scrapy.Request(url=start_url, callback=self.parse, meta={'page_number': 1, 'keyword': keyword})

#     def generate_csv_filename(self, keyword):
#         # Generate a CSV filename based on the keyword
#         return f'{keyword}_ebay_data.csv'

#     def parse(self, response):
#         page_number = response.meta['page_number']
#         keyword = response.meta['keyword']
#         product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
#         if product_links:
#             for url in product_links:
#                 yield scrapy.Request(url, callback=self.parse_page, meta={'page_number': page_number, 'keyword': keyword})

#         next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
#         if next_page:
#             page_number += 1
#             yield scrapy.Request(next_page, callback=self.parse, meta={'page_number': page_number, 'keyword': keyword})

#     def parse_page(self, response):
#         page_number = response.meta['page_number']
#         keyword = response.meta['keyword']
#         storename = response.xpath('//span[@class="ux-textspans ux-textspans--PSEUDOLINK ux-textspans--BOLD"]/text()').get()
#         storelink = response.xpath('//div[@class="ux-seller-section__item--seller"]/a[1]/@href').get()
#         name = response.xpath('(//div[@class="vim d-business-seller"]//div[@class="ux-layout-section-module"]//span[@class="ux-textspans"])[2]/text()').get()

#         phone_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Phone:')]/following-sibling::span/text()")
#         if phone_elements:
#             phone = phone_elements[0].get()
#         else:
#             phone = None

#         email_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Email:')]/following-sibling::span/text()")
#         if email_elements:
#             email = email_elements[0].get()
#         else:
#             email = None

#         if phone or email:
#             data = {
#                 "Store Name": storename,
#                 "Store Link": storelink,
#                 "Name": name,
#                 "Phone": phone,
#                 "Email": email,
#                 "Link": response.url,
#                 "Page Number": page_number
#             }

#             # Generate the CSV filename for the current keyword
#             csv_filename = self.generate_csv_filename(keyword)

#             # Write the data to the CSV file
#             with open(csv_filename, 'a', newline='') as csvfile:
#                 fieldnames = data.keys()
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#                 # If it's a new CSV file, write the header
#                 if csvfile.tell() == 0:
#                     writer.writeheader()

#                 writer.writerow(data)
# import scrapy
# import csv

# class EbaySpider(scrapy.Spider):
#     name = 'ebay'
#     allowed_domains = ['ebay.com']

#     # Define a list of keywords to scrape
#     keywords = ['laptops', 'cards']

#     def start_requests(self):
#         for keyword in self.keywords:
#             # Construct the start URL with the current keyword and page number
#             start_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={keyword}&_sacat=0'
#             yield scrapy.Request(url=start_url, callback=self.parse, meta={'page_number': 1, 'keyword': keyword})

#     def generate_csv_filename(self, keyword, with_condition=False):
#         # Generate a CSV filename based on the keyword and condition
#         condition_suffix = '_with_condition' if with_condition else '_without_condition'
#         return f'{keyword}_ebay_data{condition_suffix}.csv'

#     def create_or_append_to_csv(self, keyword, with_condition, data):
#         csv_filename = self.generate_csv_filename(keyword, with_condition)
#         with open(csv_filename, 'a', newline='') as csvfile:
#             fieldnames = data.keys()
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#             # If it's a new CSV file, write the header
#             if csvfile.tell() == 0:
#                 writer.writeheader()

#             writer.writerow(data)

#     def parse(self, response):
#         keyword = response.meta['keyword']
#         page_number = response.meta['page_number']
#         product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
#         if product_links:
#             for url in product_links:
#                 yield scrapy.Request(url, callback=self.parse_page, meta={'keyword': keyword, 'page_number': page_number})

#         # Check if there is a "Next" button for pagination
#         # next_page = response.xpath('//a[@class="pagination__next icon-link"]').get()
#         # if next_page:
#         #     next_page_url = response.urljoin(next_page)
#         #     next_page_number = page_number + 1
#         #     yield scrapy.Request(url=next_page_url, callback=self.parse, meta={'page_number': next_page_number, 'keyword': keyword})
#         next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
#         if next_page:
#             page_number += 1
#             yield scrapy.Request(next_page, callback=self.parse, meta={'page_number': page_number})
#         else:
#             self.logger.info(f"No 'Next' button found on page {page_number} for keyword {keyword}")

#     def parse_page(self, response):
#         keyword = response.meta['keyword']
#         page_number = response.meta['page_number']
#         storename = response.xpath('//span[@class="ux-textspans ux-textspans--PSEUDOLINK ux-textspans--BOLD"]/text()').get()
#         storelink = response.xpath('//div[@class="ux-seller-section__item--seller"]/a[1]/@href').get()
#         name = response.xpath('(//div[@class="vim d-business-seller"]//div[@class="ux-layout-section-module"]//span[@class="ux-textspans"])[2]/text()').get()

#         phone_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Phone:')]/following-sibling::span/text()")
#         if phone_elements:
#             phone = phone_elements[0].get()
#         else:
#             phone = None

#         email_elements = response.xpath("//div[@class='ux-section__item']/span[contains(text(),'Email:')]/following-sibling::span/text()")
#         if email_elements:
#             email = email_elements[0].get()
#         else:
#             email = None

#         data = {
#             "Store Name": storename,
#             "Store Link": storelink,
#             "Name": name,
#             "Phone": phone,
#             "Email": email,
#             "Link": response.url,
#             "Page Number": page_number  # Include the page number in the data
#         }

#         # Apply the condition to store data if either "phone" or "email" is present
#         if phone or email:
#             with_condition = True
#         else:
#             with_condition = False

#         # Append data to the CSV file based on the condition
#         self.create_or_append_to_csv(keyword, with_condition, data)
import scrapy
import csv

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    allowed_domains = ['ebay.com']

    # Define a list of keywords to scrape
    keywords = ['laptops', 'cards']

    def start_requests(self):
        for keyword in self.keywords:
            # Construct the start URL with the current keyword and page number
            start_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={keyword}&_sacat=0'
            yield scrapy.Request(url=start_url, callback=self.parse, meta={'page_number': 1, 'keyword': keyword})

    def generate_csv_filename(self, keyword, with_condition=False):
        # Generate a CSV filename based on the keyword and condition
        condition_suffix = '_with_condition' if with_condition else '_without_condition'
        return f'{keyword}_ebay_data{condition_suffix}.csv'

    def create_or_append_to_csv(self, keyword, with_condition, data):
        csv_filename = self.generate_csv_filename(keyword, with_condition)
        with open(csv_filename, 'a', newline='') as csvfile:
            fieldnames = data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # If it's a new CSV file, write the header
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

    def parse(self, response):
        keyword = response.meta['keyword']
        page_number = response.meta['page_number']  # Get the page number from the meta
        product_links = response.xpath('//div[@class="s-item__info clearfix"]/a/@href').getall()
        if product_links:
            for url in product_links:
                yield scrapy.Request(url, callback=self.parse_page, meta={'keyword': keyword, 'page_number': page_number})

        # Check if there is a "Next" button for pagination
        next_page = response.xpath('//a[@class="pagination__next icon-link"]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            next_page_number = page_number + 1
            yield scrapy.Request(url=next_page_url, callback=self.parse, meta={'page_number': next_page_number, 'keyword': keyword})

    def parse_page(self, response):
        keyword = response.meta['keyword']
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

        data = {
            "Store Name": storename,
            "Store Link": storelink,
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Link": response.url,
            "Page Number": page_number  # Include the page number in the data
        }

        # Apply the condition to store data if either "phone" or "email" is present
        if phone or email:
            with_condition = True
        else:
            with_condition = False

        # Append data to the CSV file based on the condition
        self.create_or_append_to_csv(keyword, with_condition, data)


