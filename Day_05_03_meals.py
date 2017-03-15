# Day_05_03_meals.py
import requests
import re

# 문제
# 손곡초등학교의 2016년 12월 식단을 출력해 주세요.
# 날짜, 메뉴
def notuse():
    url = 'http://www.songok.es.kr/segio/meal_v2/meal_month.php?year=2016&month=12&day=17&bld_cho=2&shell='
    recvd = requests.get(url)
    # print(recvd.text)

    # items = re.findall(r'<div class="mon_list">(.+?)</a></div>', recvd.text, re.DOTALL)
    # print(len(items))
    # print(items[0])

    items = re.findall(r'<a href="meal_view.php".+?name="(.+?)">(.*?)</a></div>', recvd.text, re.DOTALL)


    # print(len(items))
    # print(items[0])

    # for meal in items:
    for date, menu in items:
        menu = re.sub(r'\n', '', menu)
        menu = re.sub(r'\(.+?\)', '', menu)
        menu = re.sub(r'<br />', ',', menu)
        menu = menu[:-1]

        year, month, day, _ = date.split(',')

        print('{}-{}-{}'.format(year, month, day), menu)

def showMeals(year,month):
    # url = 'http://www.songok.es.kr/segio/meal_v2/meal_month.php?year='+year+'&month='+month
    url = 'http://www.songok.es.kr/segio/meal_v2/meal_month.php?year={}$month={}'.format(year,month)
    recvd = requests.get(url)

    items = re.findall(r'<div class="mon_list">(.+?)</a></div>', recvd.text, re.DOTALL)


    for date, menu in items:
        menu = re.sub(r'\n', '', menu)
        menu = re.sub(r'\(.+?\)', '', menu)
        menu = re.sub(r'<br />', ',', menu)
        menu = menu[:-1]

        year, month, day, _ = date.split(',')

        print('{}-{}-{}'.format(year, month, day), menu)

for i in range(12):
    showMeals(2016, i+1)