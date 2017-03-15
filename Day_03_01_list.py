import random
# int, float, bool, str
# collection : list, tuple, set, dictionary
#               []     ()   {}     {}
a = [1, 3, 5]
print(a, type(a))
print(a[0], a[1], a[2])

# for문을 사용해 리스트의 모든 데이터를 출력해 보세요

i = 0
for i in range(len(a)):
    print(a[i], end=' ')
print()

for i in range(5):
    # print(random.randrange(10), end=' ')
    # print(random.randrange(10,20),end=' ')
    print(random.randrange(0, 100, 10), end=' ')

print()


# 10개짜리 난수 리스트를 반환하는 함수를
def makerandoms(size):
    # b = [0] * size
    # for i in range(size):
    #     b[i] = random.randrange(100)
    #
    # return b

    a = []
    for _ in range(size):   # for 사이 i를 사용하지 않는 경우 _로 대신할수 있음
        a.append(random.randrange(100))  # append 함수는 배열의 마지막에 하나씩 추가함
    return a

def sumation(a):
    # for i in range(len(a)):
    #     print(i)
    #
    # for i in a:
    #     print(i)

    s = 0
    for i in a:
        s += i
    return s

a = makerandoms(10)
print(a)

print(sumation(a))

# 리스트에서 가장 큰 값을 찾는 함수를 만드세요

def findMaxInList(a):
    Max = a[0]
    # for i in a:
    #     if Max < i:
    #         m = i
    for i in range(1,len(a)):
        if Max < a[i]:
            Max = a[i]
    return Max

def maxMinValue(a):
    mx, mn = a[0], a[0]
    for i in a:
        if mx < i:
            mx = i
        elif mn > i:
            mn = i
        return [mx, mn]
print(findMaxInList(a))
print(maxMinValue(a))