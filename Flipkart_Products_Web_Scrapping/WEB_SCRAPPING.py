from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

my_url = 'https://www.flipkart.com/search?q=hp+laptops+i5+10th%20gen&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
page = urlopen(my_url)
page_html = page.read()
# print(page_html)


page.close()

PageSoup = BeautifulSoup(page_html, "html.parser")

containers = PageSoup.find_all("div", {"class": "_2kHMtA"})

print(len(containers))

titles = []
prices = []
imgs = []
links = []

headers = "Title, Img_Url, Product_Url, Price"

for container in containers:
    title = container.findAll("div", {"class": "_4rR01T"})
    titles.append(title[0].text.strip())
    price = container.findAll("div", {"class": "_30jeq3 _1_WHN1"})
    prices.append(price[0].text.strip())
    img = container.findAll("img", {"class": "_396cs4 _3exPp9"})
    image_src = img[0]["src"]
    imgs.append(image_src)
    url = container.findAll("a", {"class": "_1fQZEK"})
    link = url[0]["href"]
    links.append(link)



with open("sample.csv", "w", encoding="utf-8") as f:
    f.write(headers + "\n")
    for i in range(24):
         f.write(titles[i] + "," + imgs[i] + "," + links[i] + "," + prices[i] + "\n")



print(prices)
print(titles)
print(imgs)
print(links)

"""
file = open("sample.csv", 'w')

headers = ['Title', 'Image_Url', 'Product_Url', 'Price']
for i in headers:
    file.write(i + ",")

for i in range(len(titles)):
    file.write(titles[i] + "," + imgs[i] + "," + links[i] + "," + prices[i] + "\n")
"""

f.close()
