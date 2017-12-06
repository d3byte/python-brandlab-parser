#m
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
pageSoup = soup(page_html, 'html.parser')

containers = pageSoup.findAll('div', {'class': 'item-container'})

f = open('data.txt', 'w')

for container in containers:
    brand = container.div.div.a.img['title']

    title_container = container.findAll('a', { 'class': 'item-title' })
    product_name = title_container[0].text

    shipping_container = container.findAll('li', { 'class': 'price-ship' })
    shipping_price = shipping_container[0].text.strip()

    f.write('brand: ' + brand + '\n' + 'product_name: ' + product_name + '\n' + 'shipping_price: ' + shipping_price + '\n\n\n')

f.close()