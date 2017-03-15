

# 프로그램 : 코드, 데이터
# 코딩 : 데이터를 함수에 전달



class Info():
    def __init__(self, age):
        print('생성자')
        self.age = age

    def show(self):
        print('show', self.age)

    def printobject(obj):
        print(obj)


# Info가 갖고 있는 생성자 호출
i1 = Info(10)
i2 = Info(20)
print(i1)
# Info.show(1)
# Info.printobject('hellwo')

# i1.age = 10
# i2.age = 20

Info.show(i1)   # unbound method
i1.show()       #   bound method
i2.show()

# a = [3, 7, 1, 5, 9]
# a.sort()
# list.sort(a)
# print(a)
#
class Detail(Info):
    def __init__(self):
        Info.__init__(self, 30)  # Info의 생성자 호출
        print('Detail')

    @property
    def myAge(self):
        return self.age


d1 = Detail()
print(d1)
d1.show()

print('myAge : ', d1.myAge)





