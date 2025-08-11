#!/usr/bin/env python3

import sys
import time
import requests
from bs4 import BeautifulSoup


def get_financial_data(ticker: str, field: str):
    """

    :param ticker:
    :param field:
    :return: tuple
    """
    time.sleep(5)

    url = f"https://finance.yahoo.com/quote/{ticker}/financials"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Ticker not found or URL is incorrect")

    soup = BeautifulSoup(response.text, "html.parser")

    data = soup.find("div", attrs={'title': field})
    if hasattr(data, 'parent'):
        data = data.parent.parent
    if not data:
        raise Exception(f"Field '{field}' not found in financial data")

    res = [field]
    for f in data.contents[2:]:
        if hasattr(f, 'contents') and f.contents:
            res.append(f.contents[0].strip())
    return tuple(res)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./financial.py <TICKER> <FIELD>")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        data = get_financial_data(ticker, field)
        print(data)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
