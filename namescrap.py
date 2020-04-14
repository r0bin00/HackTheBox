import requests as rq
from bs4 import BeautifulSoup as bs

my_url = 'https://github.com/TheBinitGhimire/Web-Shells'

p_html = rq.get(my_url)

p_soup = bs(p_html.text,"html.parser")


p_con = p_soup.findAll("a",{"class":"js-navigation-open"})


name = []


for p_name in p_con:
    name.append(p_name.text)

for i in name:
    print(i + "\n")
