
def not_use():
    def twice(a):
        return a*2

    t = twice       #함수 포인터
    print(t(3))

    # 값을 반환하는 한 줄짜리 함수
    double = lambda a: a*2

    print(double(3))

    def proxy(f):
        print(f)
        print(f(3))

    proxy(twice)
    proxy(lambda a: a*2)



import random
def makerandoms(size):
    a = []
    for _ in range(size):   # for 사이 i를 사용하지 않는 경우 _로 대신할수 있음
        a.append(random.randrange(100))  # append 함수는 배열의 마지막에 하나씩 추가함
    return a

ns = makerandoms(10)
print(ns)

# ns = sorted(ns)   # 정렬된 리스트 반환
# ns.sort()         # 내가 정렬됨
print(sorted(ns))
print(sorted(ns, reverse=True))
print(sorted(ns, key=lambda a: a%10))

colors = ['RED', 'green', 'bLuE', 'Black', 'White']
print(sorted(colors))
print(sorted(colors, key=lambda s: s.lower()))

if __name__ == '__main__':
    colors = ['RED', 'green', 'bLuE', 'Black', 'White']
    print(sorted(colors))
    print(sorted(colors, key=lambda s: s.lower()))

    print(sorted(colors, key=lambda s: len(s)))

print(__name__)


















