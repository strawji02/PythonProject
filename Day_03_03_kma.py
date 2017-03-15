# Day_03_03_kma.py
import requests
import re
def start():
    # print("날씨 정보 읽기 완료")

    def readKma(filename):
        f = open(filename, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        return ''.join(lines)

    def writeKma(filename, text):
        f = open(filename, 'w', encoding='utf-8')
        f.write(text)
        f.close()


    url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
    recvd = requests.get(url)
    # print(recvd)
    # print(recvd.text)
    # writeKma('Data/kma.txt', '')
    writeKma('Data/kma.txt', recvd.text)

    def not_used():
        text = readKma('Data/kma.txt')

        # temp = re.findall(r'<province>(.+)</province>', text)
        # print(temp)
        # print(len(temp))
        #
        # for i in temp:
        #     print(i)

        # 탐욕적(greedy) : .+
        # 비탐욕적(non-greedy) : .+?
        locations = re.findall(r'<location wl_ver="3">(.+?)</location>',
                               text, re.DOTALL)
        # print(len(locations))
        # print(locations[0])

        for loc in locations:
            # print(loc)

            prov = re.findall(r'<province>(.+)</province>', loc)
            city = re.findall(r'<city>(.+)</city>', loc)
            # print(prov, city)

            # 문제
            # data를 찾아주세요.
            data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
            # print(len(data))

            for datum in data:
                mode = re.findall(r'<mode>(.+?)</mode>', datum)
                tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', datum)
                wf   = re.findall(r'<wf>(.+?)</wf>', datum)
                tmn  = re.findall(r'<tmn>(.+?)</tmn>', datum)
                tmx  = re.findall(r'<tmx>(.+?)</tmx>', datum)
                reli = re.findall(r'<reliability>(.+?)</reliability>', datum)
                # print(mode, mode[0])
                row = '{},{},{},{},{},{},{},{}'.format(prov[0], city[0],
                                mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reli[0])
                print(row)



    f = open('Data/kma.csv', 'w', encoding='utf-8')

    import csv
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    # ----------------------------------- #

    text = readKma('Data/kma.txt')
    locations = re.findall(r'<location wl_ver="3">(.+?)</location>', text, re.DOTALL)

    for loc in locations:

        header = re.findall(r'<province>(.+)</province>.+?<city>(.+)</city>',
                            loc, re.DOTALL)
        # print(header)
        # print(header[0])
        # print(header[0][0])
        prov, city = header[0]
        # print(prov, city)

        # data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
        #
        # for datum in data:
        #     pattern = r'<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>.+?<tmn>(.+?)</tmn>.+?<tmx>(.+?)</tmx>.+?<reliability>(.+?)</reliability>'
        #     item = re.findall(pattern, datum, re.DOTALL)
        #     # print(item)

        pattern = r'<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>.+?<tmn>(.+?)</tmn>.+?<tmx>(.+?)</tmx>.+?<reliability>(.+?)</reliability>'
        item = re.findall(pattern, loc, re.DOTALL)
        # print(len(item))

        # for row in item:
        #     # print(row)
        #     mode, tmEf, wf, tmn, tmx, reli = row
        #     line = '{},{},{},{},{},{},{},{}'.format(prov, city, mode, tmEf, wf, tmn, tmx, reli)
        #     print(line)

        for mode, tmEf, wf, tmn, tmx, reli in item:
            line = '{},{},{},{},{},{},{},{}'.format(prov, city, mode, tmEf, wf, tmn, tmx, reli)
            # print(line)
            f.write(line)
            f.write('\n')

            # writer.writerow([prov, city, mode, tmEf, wf, tmn, tmx, reli])
    # print("날씨 정보 읽기 완료")

    f.close()
f = open('Data/kma.csv', 'w', encoding='utf-8')
start()