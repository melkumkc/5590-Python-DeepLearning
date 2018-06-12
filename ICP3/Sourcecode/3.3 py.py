
import urllib.request
from bs4 import BeautifulSoup
import os

html = requests.get ("https://en.wikipedia.org/wiki/List_of_stat_and union_territory_capitals_in_India")
urllib.request.urlopen('html')
c = html.content
soup = BeautifulSoup (c,"html.parser")
print (soup.title.string)
all = soup.find_all ('a')
for link in all:
    print (link.get('href'))
