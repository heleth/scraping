#!/usr/bin/env python3
"""
scrape nikkei webpage and get stock-price

output
------
stdout
"""


import requests
from bs4 import BeautifulSoup


if (__name__ == '__main__'):
    # ------------------------------------------------------------------------
    ## get content of webpage
    # ------------------------------------------------------------------------
    url = "https://www.nikkei.com/markets/kabu/"
    r = requests.get(url)

    # ------------------------------------------------------------------------
    ## parse html
    # ------------------------------------------------------------------------
    soup = BeautifulSoup(r.content, "html.parser")
    for line in soup.find_all("span"):
        try:
            class_name = line.get("class").pop(0)
            if (class_name == "mkc-stock_prices"):
                print("stock price : {}".format(line.string))
                break
        except:
            pass

