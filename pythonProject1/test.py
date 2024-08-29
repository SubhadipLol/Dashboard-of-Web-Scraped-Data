import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

d = {"title": [], "price": [], "rating": [], "discount": [], "reviews": [], "highlights": []}

for i in range(1, 10):
    url = "https://www.flipkart.com/search?q=smartphone+5g+4g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(
        i)
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    product_cards = soup.find_all("div", attrs={"class": "_1AtVbE"})

    for card in product_cards:
        # Title
        title_tag = card.find("a", attrs={"class": "IRpwTa"})
        if not title_tag:
            title_tag = card.find("a", attrs={"class": "s1Q9rs"})
        title = title_tag.text if title_tag else "N/A"
        d['title'].append(title)

        # Price
        price_tag = card.find("div", attrs={"class": "_30jeq3"})
        price = price_tag.text if price_tag else "N/A"
        d['price'].append(price)

        # Rating
        rating_tag = card.find("div", attrs={"class": "_3LWZlK"})
        rating = rating_tag.text if rating_tag else "N/A"
        d['rating'].append(rating)

        # Discount
        discount_tag = card.find("div", attrs={"class": "_3Ay6Sb"})
        discount = discount_tag.text if discount_tag else "N/A"
        d['discount'].append(discount)

        # Reviews
        review_tag = card.find("span", attrs={"class": "_2_R_DZ"})
        reviews = review_tag.text if review_tag else "N/A"
        d['reviews'].append(reviews)

        # Highlights
        highlights_tag = card.find("ul", attrs={"class": "_1xgFaf"})
        highlights = highlights_tag.text if highlights_tag else "N/A"
        d['highlights'].append(highlights)

# Convert to DataFrame
flipkart_df = pd.DataFrame.from_dict(d)
flipkart_df.replace({'title': {'N/A': np.nan}}, inplace=True)
flipkart_df.dropna(subset=['title'], inplace=True)
print(flipkart_df)
