from bs4 import BeautifulSoup
import pandas as pd
import requests
import random

url="https://www.flipkart.com/search?q=smartphone%205g%204g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
webpage=requests.get(url)
# print(webpage.content)

soup=BeautifulSoup(webpage.content,"html.parser")

links=soup.find_all("a",attrs={'class':'CGtC98'})

link = links[0].get('href')

product_list="https://www.flipkart.com"+link


new_webpage=requests.get(product_list)
# print(new_webpage)
soup=BeautifulSoup(new_webpage.content,"html.parser")
print(soup)

