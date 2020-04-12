import requests as rq
from bs4 import BeautifulSoup as bs

my_url = 'https://www.othoba.com/laptop'

p_html = rq.get(my_url)

p_soup = bs(p_html.text,"html.parser")


p_con = p_soup.findAll("div",{"class":"details"})
brand_con = p_soup.findAll("span",{"class":"value"})
price_con = p_soup.findAll("span",{"class":"price actual-price"})

filename = "laptop.csv"

f = open(filename,"w")

headers = "Brand, Product_Name, Price\n"
f.write(headers)

product_name = []
product_brand = []
product_price = []

for p_name in p_con:
    product_name.append(p_name.h2.a.text)

for p_brand in brand_con:
    product_brand.append(p_brand.text.strip())
for p_price in price_con:
    product_price.append(p_price.text)


for i,j,k in zip(product_name, product_brand, product_price):
    f.write(j + "," + i.replace(",","|")+","+k+ "\n")
f.close()
