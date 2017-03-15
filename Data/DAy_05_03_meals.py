# 문제
# 손곡초의 16년 12월 식단을 출력해 주세요

import requests
import re

url = 'view-source:http://www.songok.es.kr/segio/meal_v2/meal_month.php?year=2016&month=12&day=17&bld_cho=2&shell='
recvd = requests.get(url)

items = re.findall(r'name="(.)')
