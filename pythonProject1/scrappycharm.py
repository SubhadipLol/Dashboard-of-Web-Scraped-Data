# import requests
# from bs4 import BeautifulSoup
#
# url = ("https://www.flipkart.com/search?q=smartphone%205g%204g&otracker=search&otracker1=search&marketplace=FLIPKART"
#        "&as-show=on&as=off")
# webpage = requests.get(url)
# # print(webpage.content)
#
# soup = BeautifulSoup(webpage.content, "html.parser")
# # print(soup)
#
# links = soup.find_all("a", attrs={'class': 'CGtC98'})
#
# link = links[0].get('href')
#
# product_list = "https://www.flipkart.com" + link
#
# new_webpage = requests.get(product_list)
# # print(new_webpage)
#
# new_soup = BeautifulSoup(new_webpage.content, "html.parser")
# # print(soup)
#
# print(new_soup.find("span", attrs={"class": "VU-ZEz"}).text.strip())
# print(new_soup.find("div", attrs={"class": "Nx9bqj CxhGGd"}).text.strip())
# print(new_soup.find("span", attrs={"class": "Wphh3N"}).text.strip())
# print(new_soup.find("div", attrs={"class": "XQDdHH"}).text.strip())
#
#
#


for i in range(1,10):
       print(i)