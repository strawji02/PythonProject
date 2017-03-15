# csv : Comma Seperated Values
import csv
import Day_03_03_kma


def read_2(filename):
    f = open(filename, 'r', encoding='utf-8')

    lines = []
    for line in csv.reader(f):
        lines.append(line)
    f.close()
    return lines

def writeCsv(filename, rows):
    f = open(filename, 'w', encoding='utf-8', newline='')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter='*')

    for  r in rows:
        writer.writerow(r)

    f.close()
if __name__ == '__main__':
    filename = 'Data/us-500.csv'
    lines = read_2(filename)
    print(*lines, sep='\n')

    writeCsv('Data/us-500_copy.csv', lines)


# print(__name__)     #현재 파일을 실행한 경우 : __main__
# Day_07_02_sqlite.py 에서 실행한 경우 : Day_05_02_csv

Day_03_03_kma.start()



