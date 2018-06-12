import urllib.requests
from bs4 import BeautifulSoup
import os

html = requests.get ("https://en.wikipedia.org/wiki/table")
urllib.request.urlopen ('html')
c = html.content
soup = BeautifulSoup (c, "html.parser")
all = soup.find_all ("tr", {'class':"wikitable sortable plainrowheaders"})
for item in all:
    print (item.get ('td'), item.get('tr'))
