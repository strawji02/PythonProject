import requests
import re

def readTed(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return ''.join(lines)

def writeTed(filename, text):
    f = open(filename, 'w', encoding='utf-8')
    f.write(text)
    f.close()

def showTedBySort(sort_by):
    url = 'https://www.ted.com/talks?sort={}'.format(sort_by)
    recvd = requests.get(url)
    # print(recvd)
    # print(recvd.text)

    writeTed('Data/Ted.txt', recvd.text)
    text = readTed('Data/Ted.txt')

    items = re.findall(r"<div class='media__message'>.+?</span>.+?</div>",recvd.text, re.DOTALL)

    # print(len(items))
    for item in items:
        # print(item)
        # speaker = re.findall("<h4 class='h12 talk-link__speaker'>(.+?)</h4>", item)
        # print(speaker[0])
        speaker = re.search("<h4 class='h12 talk-link__speaker'>.+?(.+?)</h4>", item)
        # print(speaker.group())
        print('speaker : ' + speaker.group(1))

        title = re.search(r"<a class=.+?>.+?(.+?)</a>", item, re.DOTALL)

        print('title : ' + title.group(1).strip())

        posted = re.search(r"<span class='meta__item'>.+?<span class='meta__val'>(.+?)</span>", item, re.DOTALL)
        print("posted : "+posted.group(1).strip())

        rated = re.search(r"<span class='meta__row'.+?<span class='meta__val'>(.+?)</span>", item, re.DOTALL)
        if rated:
            print("rated : "+rated.group(1).strip())
        else:
            print("rated : **empty")

        print()

categoris=['oldest', 'popular', 'jaw-dropping', 'funny','persuasive', 'courageous', 'ingenious'
           , 'fascinating', 'inspiring', 'beautiful', 'informative']
for sort_by in categoris:
    showTedBySort('persuasive')
    print(sort_by, '='*50)


# <option value="oldest">Oldest</option>
# <option value="popular">Most viewed</option>
# <option value="jaw-dropping">Jaw-dropping</option>
# <option value="funny">Funny</option>
# <option value="persuasive">Persuasive</option>
# <option value="courageous">Courageous</option>
# <option value="ingenious">Ingenious</option>
# <option value="fascinating">Fascinating</option>
# <option value="inspiring">Inspiring</option>
# <option value="beautiful">Beautiful</option>
# <option value="informative">Informative</option></optgroup></select>