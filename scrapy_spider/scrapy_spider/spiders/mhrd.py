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
        # print(response.url + " : " + str(len(item_links)))

        not_url = ['/', '#', 'javascript:void(0)']
        file_types = ['pdf', 'docx', 'docx']

        def isDomainOnlyURL(link):
            link_p = urlparse(link)
            response_p = urlparse(response.url)
            # print(link_p.path)
            if (link_p.netloc == response_p.netloc and link_p.path != "/"):
                return True
                # print(link)

        # href with '/#about' to convert to full href link
        def convertURL(my_url):
            if (my_url not in not_url):
                if (my_url[:4] != "http"):
                    my_url = urljoin(response.url, my_url)

                # Adding all links to array
                for file_type in file_types:
                    if (isDomainOnlyURL(my_url)):
                        # Adding PDF's links
                        if (file_type in my_url and my_url not in pdf_links):
                            pdf_links.append(my_url)
                            # print(my_url)
                        # Appending new follow links
                        elif (my_url not in new_links and my_url not in pdf_links):
                            new_links.append(my_url)

                # print(my_url)

        # Loop through the entire links
        for link in item_links:
            convertURL(link)

        print(new_links)

        # if new_links[i]:
        #     print(new_links[i])
        #     # absolute_next_page_url = response.urljoin(next_page_url)
        #     yield scrapy.Request(new_links[i])

    def parse_item(self, response):
        print('Processing..' + response.url)
        # print(response.text)


print("Hello!!")
