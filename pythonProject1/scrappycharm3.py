#working----------

import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

d = {"title": [], "price": [], "rating": [], "discount": [], "reviews": [], "highlights": []}
title = []
price = []
rating = []
discount = []
reviews = []
highlights = []

for i in range(1, 20):
    url = (
              "https://www.flipkart.com/search?q=smartphone+5g+4g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=") + str(
        i)
    webpage = requests.get(url)
    soup1 = BeautifulSoup(webpage.content, "html.parser")
    soup = soup1.find("div", attrs={"class": "DOjaWF gdgoEp"})
    if (soup):
        raw_title = soup.find_all("div", attrs={"class": "KzDlHZ"})
        raw_price = soup.find_all("div", attrs={"class": "Nx9bqj _4b5DiR"})
        raw_rating_reviews = soup.find_all("span", attrs={"class": "Wphh3N"})
        raw_rating = soup.find_all("div", attrs={"class": "XQDdHH"})
        raw_highlights = soup.find_all("ul", attrs={"class": "G4BRas"})
        raw_discount = soup.find_all("div", attrs={"class": "UkUFwK"})

        #for title
        for i in raw_title:
            # d['title'].append(i.text)
            title.append(i.text)
        for i in raw_price:
            # d['price'].append(i.text)
            price.append(i.text)
        for i in raw_rating_reviews:
            # d['reviews'].append(i.text)
            reviews.append(i.text)
        for i in raw_rating:
            # d['rating'].append(i.text)
            rating.append(i.text)
        for i in raw_highlights:
            # d['highlights'].append(i.text)
            highlights.append(i.text)
        for i in raw_discount:
            # d['discount'].append(i.text)
            discount.append(i.text)

# flipkart_df = pd.DataFrame.from_dict(d)
# flipkart_df.replace({'title': {'': np.nan}}, inplace=True)
# flipkart_df.dropna(subset=['title'],inplace=True)
# print(flipkart_df)

# print(len(d['title']))
# print(len(d['price']))
# print(len(d['reviews']))
# print(len(d['rating']))
# print(len(d['highlights']))
# print(len(d['discount']))

print(len(title))
print(len(price))
print(len(reviews))
print(len(rating))
print(len(highlights))
print(len(discount))
