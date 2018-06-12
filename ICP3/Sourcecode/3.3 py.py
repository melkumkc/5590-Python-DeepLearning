from bs4 import BeautifulSoup
import urllib.request
import os

html = ("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
source_code = urllib.request.urlopen(html)
plain_text = source_code
soup = BeautifulSoup(plain_text,'html.parser')

print(soup.title.string)

all = soup.find_all ('a')
for link in all:
    print (link.get('href'))
for row in soup.find_all ('tr'):
    for col in row.find_all('td'):
        print(col.text)
for row in soup.find_all ('tr'):
    for col in row.find_all('th'):
        print(col.text)




