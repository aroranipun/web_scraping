# Notes
# Add parallel processing

import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import time

def chunker(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def normalize(text):
    if not text:
        return text
    return re.sub('\s+', ' ', re.sub(r'[\r\n]', ' ', text.strip()))

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# A function to get information from a weblink
def get_page(page_link):
    page = requests.get(page_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = normalize(soup.title.string) if soup.title else None
    keywords = soup.find("meta", attrs={'name': 'keywords'})
    description = soup.find("meta", attrs={'name': 'description'})
    keywords = normalize(keywords['content']) if keywords and keywords.has_attr('content') else None
    description = normalize(description['content']) if description and description.has_attr('content') else None
    text = normalize(' '.join(filter(tag_visible, soup.findAll(text=True))))
    info = {
        'web_link': page_link,
        'title': title,
        'keywords': keywords,
        'description': description,
        # 'text': text,
    }

    return (info)

def get_page_multi(list_webpages):
    info = []
    start = time.perf_counter()

    info = [get_page(i) for i in list_webpages]

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} seconds')

    return info

# Test-------------------------------
# def get_weblink(gene_id):
#     web_link_partial = "https://www.ncbi.nlm.nih.gov/gene/"
#     full_link = web_link_partial + str(gene_id)
#     return (full_link)
#
# web_list = [get_weblink(i) for i in range(2000, 2020)]
# f1 = get_page_multi(list_webpages=web_list, parallel=True)
