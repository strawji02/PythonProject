import requests
import json

def tran(text, sorce, target):
    headers = {'x-naver-client-id': 'labspace'}
    payload = {'source': sorce,'target': target, 'text': text}

    url = 'http://labspace.naver.com/api/n2mt/translate'
    recvd = requests.post(url, data=payload, headers=headers)
    # print(recvd)
    # print(recvd.text)

    item = json.loads(recvd.text)
    # print(item.keys())
    # print(item['message'])

    message = item['message']
    result = message['result']
    # print(result)
    tranText = result['translatedText']
    return tranText


# print(tran('', 'ko', 'en'))
# print(tran('', 'en', 'ko'))
while(1):
    a = input("번역시킬 언어(입력할 문장) 한국어, 영어중 선택 입력, 종료 입력시 프로그램 종료 : ")
    if a == '한국어':
        b = input("번역할 한국어 문장 : ")
        print(tran(b, 'ko', 'en'))
    elif a == '영어':
        b = input("번역할 영어 문장 : ")
        print(tran(b, 'en', 'ko'))
    elif a == '종료':
        break;
    else:
        print('잘못 입력')









