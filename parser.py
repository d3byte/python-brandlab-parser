from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import json


# Данные для логина
url = 'https://users.wix.com/wix-sm/api/member/login'

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'users.wix.com',
    'Origin': 'https://www.brandlab.club',
    'Referer': 'https://www.brandlab.club/forum/baza-znaniy',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

formData = {
    'email': '89505105005@mail.ru',
    'password': 'DVilyavin89',
    'rememberMe': 'false',
    'collectionId': '14d49782-0975-85d9-4ebf-d8ce76a1da5f',
    'metaSiteId': '2d798e2d-fc4a-428a-8774-ab19d2605d80',
    'svSession': 'a0d8b9dab387f0b95db42a0aa0c86f3deabff126d4d80cda8d13b9bda934537e74e18c5fc85cf9c874fd9846e3b423ec1e60994d53964e647acf431e4f798bcd1490bfd9a0053c511e6623c437e5dad3b6c22ed7d7ccf428f3809f9832d84823',
    'appUrl': 'https://www.brandlab.club/forum/baza-znaniy'
}

response = requests.post(url, formData, headers)
print(response.headers)
cookies = response.headers['Set-Cookie'].split(', ')
XSRF_TOKEN = cookies[0].split('|')
XSRF_TOKEN = XSRF_TOKEN[0][11:]
ENC_KEY = cookies[0].split('|')[1].split(';')[0]
print('XSRF_TOKEN: ', XSRF_TOKEN)
print('ENCENC_KEY: ',ENC_KEY)

# Информация о пользователе
user = response.content.decode('utf8').replace("'", '"')
user = json.loads(user)
userString = json.dumps(user, indent=4, sort_keys=True)
print('Пользователь:\n', userString, '\n\n')

sessionToken = user['payload']['sessionToken']
siteMemberDto = user['payload']['siteMemberDto']
# collectionId = user['payload']['collectionId']
# owner = user['payload']['owner']
# name = user['payload']['name']
# email = user['payload']['email']
# attributes = user['payload']['attributes']
# expirationDate = user['payload']['expirationDate']

# 
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'hs=' + XSRF_TOKEN + '; svSession=' + 'a0d8b9dab387f0b95db42a0aa0c86f3deabff126d4d80cda8d13b9bda934537e74e18c5fc85cf9c874fd9846e3b423ec1e60994d53964e647acf431e4f798bcd1490bfd9a0053c511e6623c437e5dad3b6c22ed7d7ccf428f3809f9832d84823',
    'Host': 'www.brandlab.club',
    'Origin': 'https://www.brandlab.club',
    'Referer': 'https://www.brandlab.club/forum/baza-znaniy',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

formData = {
    'token': sessionToken
}

url = 'https://www.brandlab.club/_api/wix-sm/verify/2d798e2d-fc4a-428a-8774-ab19d2605d80/99298aaf-4a38-4d4a-ace4-da2fee87862c'

response = requests.post(url, formData, headers=headers)
print('Запрос-1:\n', response.content, '\n\n')

# uClient = uReq(url)
# page_html = uClient.read()
# uClient.close()
# pageSoup = soup(page_html, 'html.parser')

# containers = pageSoup.findAll('div', {'class': 'item-container'})

# f = open('data.txt', 'w')

# for container in containers:
#     brand = container.div.div.a.img['title']

#     title_container = container.findAll('a', { 'class': 'item-title' })
#     product_name = title_container[0].text

#     shipping_container = container.findAll('li', { 'class': 'price-ship' })
#     shipping_price = shipping_container[0].text.strip()

#     f.write('brand: ' + brand + '\n' + 'product_name: ' + product_name + '\n' + 'shipping_price: ' + shipping_price + '\n\n\n')

# f.close()
