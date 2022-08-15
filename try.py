import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.bol.com/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

productlinks = []

for x in range(1,109):
    r = requests.get(f'https://www.bol.com/nl/s/?searchtext=beard+balm&searchContext=media_all&appliedSearchContextId=&suggestFragment=&adjustedSection=&originalSection=&originalSearchContext=&section=main&N=0&defaultSearchContext=media_all?page={x}')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='product-item__info hit-area')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])

print(len(productlinks))
#print(productlinks)

testlink = 'https://www.bol.com/nl/s/?searchtext=beard+balm&searchContext=media_all&appliedSearchContextId=&suggestFragment=&adjustedSection=&originalSection=&originalSearchContext=&section=main&N=0&defaultSearchContext=media_all'
r = requests.get(testlink, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
name=soup.find('h1', class_='page-heading')
rating=soup.find('div', class_='rating-horizontal__average-score')
price = soup.find('section', class_='price-block price-block--large')
print(name,price, rating)
