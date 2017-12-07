import requests
import json
from data_handler import handleData
offset = 40
url = 'https://forums.wix.com/_api/posts?categoryId=597751e9a5026f001007ec96&offset=' + str(offset) + '&size=20'
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'XSRF-TOKEN=1512583954|iO4VQYfdvt0F; userType=ANONYMOUS; _wix_browser_sess=29b84120-eacd-47cc-9308-a155a146f40c; incap_ses_584_138990=qapfCi4fm1YU7rIKYckaCCkzKFoAAAAAoMA6Ojd6hlvXBa4GY32P0Q==; incap_ses_584_133961=Zie8Be9e8WO0BsMKYckaCERLKFoAAAAAk0yr8rAM6loflnwHC3fylA==; _wixUIDX=null-user-id; _wixCIDX=36ec823e-fc3d-4a15-afe9-e789319eb8f7; __utma=37294626.77352872.1512590152.1512590159.1512590159.1; __utmc=37294626; __utmz=37294626.1512590159.1.1.utmcsr=ru.wix.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.77352872.1512590152; _wixAB3=43781#1',
    'instance': 'NOn4aAVpnHrpF5r_wYrFp-r7Q1qf8Q71RQfM3qo7Pcs.eyJpbnN0YW5jZUlkIjoiOGExMzUwMzMtOThmNS00YTBjLWFlYWEtOGZiMGJhZGI4ZTFmIiwiYXBwRGVmSWQiOiIxNDcyNGYzNS02Nzk0LWNkMWEtMDI0NC0yNWZkMTM4ZjkyNDIiLCJzaWduRGF0ZSI6IjIwMTctMTItMDZUMjE6Mjg6NTIuMDgzWiIsInVpZCI6ImU3YjIwY2FmLWM5ODctNDVkNC1hMDAwLTVkYzg1ZWQ1NTkzZCIsImlwQW5kUG9ydCI6Ijk1Ljg0LjE4Mi41Mi81NDE5NCIsInZlbmRvclByb2R1Y3RJZCI6bnVsbCwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiJlN2IyMGNhZi1jOTg3LTQ1ZDQtYTAwMC01ZGM4NWVkNTU5M2QiLCJiaVRva2VuIjoiYTc2YWRlMWUtNjRiZi0wODg2LTI5ZGUtMjRhOTY4YmJkMzlmIiwic2l0ZU93bmVySWQiOiIxMDRlM2M3MC03Yzk4LTQ5YTMtYTk4Yy1hZGVjZmIyMGY4MjkifQ',
    'Refer': 'https://forums.wix.com/fakultet-volka?cacheKiller=1512595735867&compId=TPASection_j5jnv7z8&deviceType=desktop&height=2160&instance=NOn4aAVpnHrpF5r_wYrFp-r7Q1qf8Q71RQfM3qo7Pcs.eyJpbnN0YW5jZUlkIjoiOGExMzUwMzMtOThmNS00YTBjLWFlYWEtOGZiMGJhZGI4ZTFmIiwiYXBwRGVmSWQiOiIxNDcyNGYzNS02Nzk0LWNkMWEtMDI0NC0yNWZkMTM4ZjkyNDIiLCJzaWduRGF0ZSI6IjIwMTctMTItMDZUMjE6Mjg6NTIuMDgzWiIsInVpZCI6ImU3YjIwY2FmLWM5ODctNDVkNC1hMDAwLTVkYzg1ZWQ1NTkzZCIsImlwQW5kUG9ydCI6Ijk1Ljg0LjE4Mi41Mi81NDE5NCIsInZlbmRvclByb2R1Y3RJZCI6bnVsbCwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiJlN2IyMGNhZi1jOTg3LTQ1ZDQtYTAwMC01ZGM4NWVkNTU5M2QiLCJiaVRva2VuIjoiYTc2YWRlMWUtNjRiZi0wODg2LTI5ZGUtMjRhOTY4YmJkMzlmIiwic2l0ZU93bmVySWQiOiIxMDRlM2M3MC03Yzk4LTQ5YTMtYTk4Yy1hZGVjZmIyMGY4MjkifQ&locale=en&pageId=wqya4&section-url=https%3A%2F%2Fwww.brandlab.club%2Fforum%2F&target=_top&viewMode=site&vsi=31a264ac-72f1-4684-9522-0a68f4c87f9f&width=1280',
    'Host': 'forums.wix.com',
    'Origin': 'https://www.brandlab.club',
    'Referer': 'https://www.brandlab.club/forum/baza-znaniy',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
response = requests.get(url, headers)
posts = response.content.decode('utf8').replace("'", '"')
posts = json.loads(posts)


while offset <= 5100:
    offset += 20
    print(offset)
    url = 'https://forums.wix.com/_api/posts?categoryId=597751e9a5026f001007ec96&offset=' + str(offset) + '&size=20'
    response = requests.get(url, headers)
    content = response.content.decode('utf8')
    content = json.loads(content)
    posts += content

offset = 40

url = 'https://forums.wix.com/_api/posts?categoryId=597751e9a5026f001007ec96&offset=' + str(offset) + '&size=20'
response = requests.get(url, headers)
content = response.content.decode('utf8').replace("'", '"')
posts += json.loads(content)

while offset <= 2240:
    offset += 20
    print(offset)
    url = 'https://forums.wix.com/_api/posts?categoryId=597751e9a5026f001007ec94&offset=' + str(offset) + '&size=20'
    response = requests.get(url, headers)
    content = response.content.decode('utf8')
    content = json.loads(content)
    posts += content

offset = 40

url = 'https://forums.wix.com/_api/posts?categoryId=597751e9a5026f001007ec96&offset=' + str(offset) + '&size=20'
response = requests.get(url, headers)
content = response.content.decode('utf8').replace("'", '"')
posts += json.loads(content)

while offset <= 2520:
    offset += 20
    print(offset)
    url = 'https://forums.wix.com/_api/posts?categoryId=597755f27d5c7106248b2ca7&offset=' + str(offset) + '&size=20'
    response = requests.get(url, headers)
    content = response.content.decode('utf8')
    content = json.loads(content)
    posts += content

offset = 40

url = 'https://forums.wix.com/_api/posts?categoryId=597751e9a5026f001007ec96&offset=' + str(offset) + '&size=20'
response = requests.get(url, headers)
content = response.content.decode('utf8').replace("'", '"')
posts += json.loads(content)

while offset <= 3120:
    offset += 20
    print(offset)
    url = 'https://forums.wix.com/_api/posts?categoryId=5977562c4f10e9001028f2e7&offset=' + str(offset) + '&size=20'
    response = requests.get(url, headers)
    content = response.content.decode('utf8')
    content = json.loads(content)
    posts += content

handleData(posts)
