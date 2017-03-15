# 파일 : 글자로 된 파일, 글자로 되지 않은 파일
#        텍스트 파일     바이너리(이진 non-text) 파일
def read_1(filename):
    f = open(filename, 'r', encoding='utf-8')

    lines = f.readlines()
    # print(lines)
    #
    # for i in lines:
    #     print(i)
    f.close()
    return ''.join(lines)

def read_2(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readline()
    while True:

        print(lines)

        if not line == 0:
            break

        line = line.strip()
        lines.append(line)

    f.close()
    return line

def write(filename,lines):
    f = open(filename,'w',encoding='utf-8')
    f.close()

    for i in lines:
        f.write(i)
        f.write('\n')
    f.close()
def readPome(filename):
    f = open(filename,'r', encoding='utf-8')
    lines = f.readline()
    f.close()
    return '*'.join(lines)




filename = 'Data/poem.txt'
# all = readPome(filename)
# print(all)

# read_1(filename)
#lines = read_2(filename)
# write('Data/write.txt',lines)


names = ['kim','han','nam']
print(''.join(names))
print('\n'.join(names))

save = '*'.join(names)
print(save.split())



def read_3(filename):
    f = open(filename,'r',encoding='utf-8')

    # i = 1
    # for line in f:
    #     print(i, line.strip())
    #     i += 1

    for i, line in enumerate(f):
        print(i + 1, line, end='')

    f.close()


read_3(filename)