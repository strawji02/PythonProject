import json
# j1 = '{"ip": "8.8.8.8"}'
# d1 = json.loads(j1)
# print(j1,d1)
# print(type(d1),type(j1))
#
# # 문제
# # d1을 문자열로 변환
#
# j2 = json.dumps(d1)
# print(j2)
#
# dt = '''{
#     'time':'03:53:25 AM'
#     'milliseconds_since_epoch': 1362196405309
#     'date': '03-02-2013
# }'''
#
# d2 = json.loads(dt)
# print(d2)
#
# for k, v in d2.items():
#     print(k,v)
#
#

import requests

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
recvd = requests.get(url)
print(recvd.text)
contents = bytes(recvd.text, 'iso-8859-1').decode('utf-8')
print(contents)
items = json.loads(contents)
for item in items:
    # print(item)
    print(item['code'], item['value'])