import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name=[]
product_prices=[]
product_rating=[]
product_reviewrate=[]
product_description=[]


for i in range(10):
    url="https://www.flipkart.com/search?q=smartphone%205g%204g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    Header=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0','Accept-Language':'en-US,en;q=0.5'})
    r=requests.get(url)
    soup1=BeautifulSoup(r.text,"lxml")
    if(soup1):

        soup=soup1.find("div",class_="DOjaWF YJG4Cf")
    else :
        print("soup parsing failed")
    # np=soup.find("a",class_="_9QVEpD").get("href")
    # cnp="https://www.flipkart.com"+np;
    # print(cnp)
    print(soup)
    if (soup):
        names=soup.find_all("div",class_="KzDlHZ")
        prices=soup.find_all("div",class_="Nx9bqj _4b5DiR")
        rating=soup.find_all("div",class_="XQDdHH")
        reviewrate=soup.find_all("span",class_="Wphh3N")
        description=soup.find_all("ul",class_="G4BRas")
        for i in names:
            product_name.append(i.text)

        for i in prices:
            product_prices.append(i.text)
        for i in rating:
            product_rating.append(i.text)
        for i in reviewrate:
            product_reviewrate.append(i.text)

        for i in description:
            product_description.append(i.text)
    else :
        print("soup failed")


# print(len(product_name))
# print(len(product_prices))
# print(len(product_rating))
# print(len(product_reviewrate))
# print(len(product_description))
df=pd.DataFrame({"Product Name":product_name,
                 "Prices":product_prices,
                 "Product Ratings":product_rating,
                 "Product Reviews":product_reviewrate,
                 "Product Description":product_description})
# print(pd)
df.to_csv("top phones in flipkart.csv")