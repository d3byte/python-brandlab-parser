import re
pat = re.compile(r'\s+')

def handleData(posts):
    index = 0

    for post in posts:
        f = open('wolf/data-' + str(index) + '.txt', 'w+')
        title = post['title'].strip()
        text = post['content']['blocks'][0]['text'].strip()
        f.write(title + '\n\n' + text + '\n')
        index += 1
        f.close()
