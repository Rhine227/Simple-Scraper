import requests as rq
from bs4 import BeautifulSoup
import random

"""NEED TO ADD GUI STILL
    """


def scrapeWikiArticle(url):
    response = rq.get(url=url)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id='firstHeading')

    print(title.text)

    # Get all the links
    all_links = soup.find(id='bodyContent').find_all('a')
    random.shuffle(all_links)
    link_to_scrape = 0
    link_list = []

    for link in all_links:
        # We are only interested in other wiki articles
        if len(link_list) < 10:
            if link['href'].find('/wiki/') == -1:
                link_list.append(link)
                continue
        else:
            break

        # Use this link to scrape
        link_to_scrape = link
        break

    scrapeWikiArticle('https://en.wikipedia.org' + link_to_scrape['href'])


scrapeWikiArticle('https://en.wikipedia.org/wiki/Web_scraping')
