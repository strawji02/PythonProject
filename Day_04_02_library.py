# Day_04_02_library.py
import requests
import re

def readKma(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return ''.join(lines)

text = readKma('Data/library.txt')
# print(text)

# url = 'http://211.251.214.169:8080/SeatMate_sj/SeatMate.php?classInfo=5'
# recvd = requests.get(url)
# text = bytes(recvd.text, encoding='iso-8859-1').decode('euc-kr')

# 문제
# 빈 자리의 갯수는 몇 개일까요?

def not_used():
    # items = re.findall(r'padding-top:0px; ">(.+?)</div></TD>', text)
    items = re.findall(r'>(.+?)</div></TD>', text)
    print(len(items))

    # empty = 0
    # for i in items:
    #     if i != '배정':
    #         print(i)
    #         empty += 1
    #
    # print('empty :', empty)

    empty = []
    for i in items:
        if i != '배정':
            empty.append(i)

    print('empty :', len(empty))
    print(empty)


items = re.findall(r'>([0-9]+)</div></TD>', text)
print(items)

items = re.findall(r'>(.+?)</div></TD>', text)
print(items)
