# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlparse, urljoin

new_links = [];
visited_links = [];
pdf_links = []

main_url = 'http://www.paavam.com'
domain = urlparse(main_url).netloc


class MhrdSpider(scrapy.Spider):
    name = 'mhrd'
    allowed_domains = ['www.paavam.com']
    start_urls = ['https://www.paavam.com/']

    def __init__(self):
        print('Scraping spider sent!')

    def __del__(self):
        cleaned_arr = []

        for j in new_links:
            k = urlparse(j)
            new_links.remove(j)
            cln_str = "" + k.scheme + "://" + k.netloc + k.path

            if (cln_str not in cleaned_arr):
                cleaned_arr.append(cln_str)

        print(main_url)
        for i in cleaned_arr:
            print(i)

    #first parsed homepage only
    def parse(self, response):
        item_links = response.css('a::attr(href)').extract()

        not_url = ['/', '#', 'javascript:void(0)']
        file_types = ['pdf', 'docx', 'docx']

        def isDomainOnlyURL(link):
            link_p = urlparse(link)
            response_p = urlparse(response.url)
            if (link_p.netloc == domain and link_p.path != "/"):
                # print(link)
                return True

        # href with '/#about' to convert to full href link
        def convertURL(my_url):
            if (my_url not in not_url):
                if (my_url[:5] != urlparse(response.url).scheme):
                    my_url = urljoin(response.url, my_url)

                # Adding all links to array
                for file_type in file_types:
                    if (isDomainOnlyURL(my_url)):
                        # Adding PDF's links
                        if (file_type in my_url and my_url not in pdf_links):
                            pdf_links.append(my_url)
                        # Appending new follow links
                        elif (my_url not in new_links and my_url not in pdf_links):
                            new_links.append(my_url)

                        # print(my_url)

        # Loop through the entire links
        for link in item_links:
            convertURL(link)

        # print(response.url + " : " + str(len(new_links)))
        # print(new_links)

        if (response.url in new_links):
            new_links.remove()
        visited_links.append(response.url)

        for url in new_links:
            if (url not in visited_links):
                # We make a request to each url and call the parse function on the http response.
                yield scrapy.Request(url=url, callback=self.parse_item)


    # For future visiting links
    def parse_item(self, response):
        item_links = response.css('a::attr(href)').extract()

        not_url = ['/', '#', 'javascript:void(0)']
        file_types = ['pdf', 'docx', 'docx']

        def isDomainOnlyURL(link):
            link_p = urlparse(link)
            response_p = urlparse(response.url)
            if (link_p.netloc == domain and link_p.path != "/"):
                # print(link)
                return True

        # href with '/#about' to convert to full href link
        def convertURL(my_url):
            if (my_url not in not_url):
                if (my_url[:5] != urlparse(response.url).scheme):
                    my_url = urljoin(response.url, my_url)

                # Adding all links to array
                for file_type in file_types:
                    if (isDomainOnlyURL(my_url)):
                        # Adding PDF's links
                        if (file_type in my_url and my_url not in pdf_links):
                            pdf_links.append(my_url)
                        # Appending new follow links
                        elif (my_url not in new_links and my_url not in pdf_links):
                            new_links.append(my_url)

                        # print(my_url)

        if (response.url not in visited_links):
            visited_links.append(response.url)

        # Loop through the entire links
        for link in item_links:
            convertURL(link)

        # print(response.url + " : " + str(len(new_links)))
        # print(new_links)
