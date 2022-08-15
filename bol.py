import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.bol.com/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

productlinks = []

for x in range(1,109):
    r = requests.get(f'https://www.bol.com/nl/l/koffiemachines/N/18312/?page={x}')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='product-item__info hit-area')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])

#print(len(productlinks))
#print(productlinks)

#testlink = 'https://www.bol.com/nl/p/krups-nespresso-essenza-mini-xn110b-koffiecupmachine-grijs/9200000075792782/?bltgh=tSzaJyBvL3T52D-pfTJK3g.onnhOtumlGpAd6d55odHJQ_0_42.43.ProductTitle'

whiskylist=[]
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name=soup.find('span', class_='h-boxedright--xs')
    try:
        rating=soup.find('div', class_='rating-horizontal__average-score').text
        price = soup.find('p', class_='price-block__price').text.strip()
        #print(price, rating)
    except:
        rating = 'no rating'
        price = 'no price found'
    whisky = {
        'name': name,
        'rating': rating,
        'price': price
        }
    whiskylist.append(whisky)
    #print('Saving: ', whisky['name'])
df = pd.DataFrame(whiskylist)
data = df.to_csv('GfG.csv', header = False)



                  
