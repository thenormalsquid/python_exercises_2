import re
import requests
from lxml import html
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, urls):
        """
        Base class for different parsers. Urls can be string or collection of urls
        TODO: 
         - convert list of urls to iterator
         - crawl through website (implemented  at child class level)
         - add some meta data in here to 'tag' the author of the quote 
        """
        self.requested = []
        # request urls as soon as object is constructed
        self._request(urls)

    def _make_request(self, url):
        # adds a beautiful soup object of the requested content to the requested list
        req = requests.get(url)
        if req.status_code == 200:
            self.requested.append(BeautifulSoup(req.content, "lxml"))

    def _request(self, urls):
        # makes a request for each url and stores the request's content as a beautiful soup object
        # if successful
        # don't bother with null check for now
        if urls and type(urls) is list:
            for url in urls:
                self._make_request(url)

        if urls and type(urls) is str:
            # if passed urls is a single url
            self._make_request(urls)


class BrainyQuote(Parser):
    def parse(self):
        # extracts all of the quotes from brainy quote
        for soup in self.requested:
            quotes_list = soup.find_all('a', {'class': "b-qt"})
            for a in quotes_list:
                sentences = a.string.strip().split('.')
                # TODO: process string here
                print(sentences)


if __name__ == '__main__':
    # gather all quotes and pass them to text processor
    don = [
        'https://www.brainyquote.com/quotes/authors/d/donald_trump_{0}.html'.format(i) for i in range(1, 12)
    ]

    mlk = [
        'https://www.brainyquote.com/quotes/authors/m/martin_luther_king_jr_{0}.html'.format(i) for i in range(1, 6)
    ]

    urls = don + mlk
    brainy = BrainyQuote(urls)
    brainy.parse()
