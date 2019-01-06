#!/usr/bin/env python3
"""
scrape nikkei webpage and get title

output
------
stdout
"""


import requests
from bs4 import BeautifulSoup


if (__name__ == '__main__'):
    # define url to access
    url = "http://www.nikkei.com/"

    # get html
    r = requests.get(url)

    # parse html with BeautifulSoup
    soup = BeautifulSoup(r.content, "html.parser")
    # --   "html.parser" : parser for html

    # get title_tag
    title_tag = soup.title

    # get title str
    title = title_tag.string

    print('title_tag : {}\ntitle : {}'.format(title_tag, title))
