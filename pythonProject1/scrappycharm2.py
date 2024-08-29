import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_title(local_soup):
    try:
        title = local_soup.find("span", attrs={"class": "VU-ZEz"}).text.strip()
    except:
        title = ""
    return title


def get_price(local_soup):
    try:
        price = local_soup.find("div", attrs={"class": "Nx9bqj CxhGGd"}).string.strip()
    except:
        price = ""
    return price


def get_rating(local_soup):
    try:
        rating = local_soup.find("div", attrs={"class": "XQDdHH"}).text.strip()
    except:
        rating = ""
    return rating


def get_reviews(local_soup):
    try:
        reviews = local_soup.find("span", attrs={"class": "Wphh3N"}).text.strip()
    except:
        reviews = ""
    return reviews


def get_highlights(local_soup):
    try:
        highlights = [local_soup.find("li", attrs={"class": "_7eSDEz"}).text.split()]
    except:
        highlights = ""
    return highlights


def get_payments(local_soup):
    try:
        payments = local_soup.find("li", attrs={"class": "g11wDd"}).text.strip()
    except:
        payments = ""
    return payments


def get_details(local_soup):
    try:
        detail=local_soup.find_all("div",attrs={"class":"_1OjC5I"})
        details=[]
        for i in detail:
            details.append(i.text)
    except:
        details=""
    return details


def small_rating(local_soup):
    try:
        camrat = local_soup.find_all("div", attrs={"class": "Nwhkb3"})
        rating=[]
        for i in camrat:
            rating.append(i.text)
    except:
        rating = ""
    return rating


d = {"title": [], "price": [], "rating": [], "reviews": [], "highlights": [],
     "payments":[], "details": [], "small rating": []}

for i in range(1, 2):
    url = (
              "https://www.flipkart.com/search?q=smartphone+5g+4g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=") + str(
        i)
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    links = soup.find_all("a", attrs={'class': 'CGtC98'})
    links_list = []
    for link in links:
        links_list.append(link.get('href'))

    for link in links_list:
        new_webpage = requests.get("https://www.flipkart.com" + link)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_reviews(new_soup))
        d['highlights'].append(get_highlights(new_soup))
        d['payments'].append((get_payments(new_soup)))
        d['details'].append(get_details(new_soup))
        d['small rating'].append(small_rating(new_soup))

flipkart_df = pd.DataFrame.from_dict(d)
# flipkart_df.replace({'title': {'': np.nan}}, inplace=True)
# flipkart_df.dropna(subset=['title'],inplace=True)
flipkart_df.to_csv("flipkart top phones.csv", header=True, index=False)
