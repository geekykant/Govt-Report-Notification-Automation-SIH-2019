# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlparse, urljoin

new_links = [];
visited_links = [];
pdf_links = []


class MhrdSpider(scrapy.Spider):
    name = 'mhrd'
    allowed_domains = ['mhrd.gov.in']
    start_urls = ['http://mhrd.gov.in/']

    def parse(self, response):
        item_links = response.css('a::attr(href)').extract()
        print(response.url + " : " + str(len(item_links)))

        not_url = ['/', '#', 'javascript:void(0)']
        file_types = ['pdf', 'docx', 'docx']

        # href with '/#about' to convert to full href link
        def convertURL(my_url):
            if (my_url not in not_url):
                if (my_url[:4] != "http"):
                    my_url = urljoin(response.url, my_url)

                for file_type in file_types:
                    if (file_type in my_url):
                        pdf_links.append(my_url)
                        # print(my_url)
                    elif (my_url not in follow_links):
                        follow_links.append(my_url)

                # print(my_url)

        for link in item_links:
            convertURL(link);

        if folow_links[i]:
            print(follow_links[i])
            # absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(follow_links[i])

    def parse_item(self, response):
        print('Processing..' + response.url)
        # print(response.text)


print("Hello!!")
