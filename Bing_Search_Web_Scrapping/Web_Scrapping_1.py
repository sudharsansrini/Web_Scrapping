from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

my_url = Request('https://www.bing.com/images/search?q=dell+laptop&form=HDRSC3&first=1&tsc=ImageBasicHover')

page = urlopen(my_url)
page_html = page.read()
# print(page_html)

page.close()


PageSoup = BeautifulSoup(page_html, "html.parser")

containers = PageSoup.find_all("div", {"class": "img_cont hoff"})

print(containers)
print(len(containers))

"""
titles = []
prices = []
imgs = []
links = []

headers = "Title, Img_Url, Product_Url, Price"

for container in containers:
    title = container.findAll("h2", {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
    titles.append(title[0].text.strip())
    price = container.findAll("span", {"class": "a-price-whole"})
    prices.append(str(price))
    img = container.findAll("img", {"class": "s-image"})
    image_src = img[0]["src"]
    imgs.append(image_src)
    
    url = container.findAll("a", {"class": "_1fQZEK"})
    link = url[0]["href"]
    links.append(link)
    


with open("amazon.csv", "w", encoding="utf-8") as f:
    f.write(headers + "\n")
    for i in range(16):
         f.write(titles[i] + "," + imgs[i] + "," + prices[i] + "\n")



print(prices)
print(titles)
print(imgs)
print(links)

f.close()
"""