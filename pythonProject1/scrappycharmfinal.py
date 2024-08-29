
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

d = {"title": [], "price": [], "rating": [], "discount": [], "reviews": [], "highlights": []}
# title = []
# price = []
# rating = []
# discount = []
# reviews = []
# highlights = []

for i in range(1, 42):
    url = (
              "https://www.flipkart.com/search?q=smartphone+5g+4g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=") + str(
        i)
    webpage = requests.get(url)
    soup1 = BeautifulSoup(webpage.content, "html.parser")
    products=soup1.find_all("div",attrs={"class":"tUxRFH"})
    if (products):
        for soup in products:

            # print(soup)
            raw_title = soup.find("div", attrs={"class": "KzDlHZ"})
            temp=raw_title.text if raw_title else ""
            d['title'].append(temp)

            raw_price = soup.find("div", attrs={"class": "Nx9bqj _4b5DiR"})
            temp=raw_price.text if raw_price else ""
            d['price'].append(temp)

            raw_rating_reviews = soup.find("span", attrs={"class": "Wphh3N"})
            temp=raw_rating_reviews.text if raw_rating_reviews else ""
            d['reviews'].append(temp)

            raw_rating = soup.find("div", attrs={"class": "XQDdHH"})
            temp=raw_rating.text if raw_rating else ""
            d['rating'].append(temp)

            raw_highlights = soup.find("ul", attrs={"class": "G4BRas"})
            temp=raw_highlights.text if raw_highlights else ""
            d['highlights'].append(temp)

            raw_discount = soup.find("div", attrs={"class": "UkUFwK"})
            temp=raw_discount.text if raw_discount else ""
            d['discount'].append(temp)


flipkart_df = pd.DataFrame.from_dict(d)
flipkart_df.replace({'title': {'': np.nan}}, inplace=True)
flipkart_df.dropna(subset=['title'],inplace=True)
flipkart_df.to_csv("flipkart top phones.csv",header=True,index=False)



