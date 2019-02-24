from urllib.parse import urlparse, urljoin
import requests

import lxml.html

new_links = [];
visited_links = [];
pdf_links = []

not_url = ['/', '#', 'javascript:void(0)']
file_types = ['pdf', 'docx', 'docx']

# main_url = 'http://www.paavam.com'
url = 'http://mhrd.gov.in/'
domain = urlparse(url).netloc

def scrapeIt(new_url):
    content = requests.get(new_url).content
    def extractLinks(content):
        dom = lxml.html.fromstring(content)
        for link in dom.xpath('//a/@href'):

            # convert '/gallery' to full link "https://../gallery"
            if (urlparse(link).scheme != urlparse(new_url).scheme):
                link = urljoin(new_url, link)

            # check for same domain links
            if(link not in not_url and urlparse(link).netloc == domain):
                for file_type in file_types:
                        if(file_type in link and link not in pdf_links):
                            pdf_links.append(link)

                if(link not in new_links and link not in pdf_links):
                    new_links.append(link)
                    

    extractLinks(content)

# First scrape
scrapeIt(url)

# Second time scrape
for i in new_links:
    print(i)
    # scrapeIt(i)

print("completed!")    
