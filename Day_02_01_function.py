# Day_02_01_func
#
# 프로그램 : 코드(함수), 데이터(변수)

# def f_1(a):
#     print(a,'+ ? :')
#     b = int(input())
#     return b
# def temp():
#     a = int(input('정수 입력 : '))
#     b = f_1(a)
#     print(a + b)
#     None
#
# def f_4():
#     print('F_4')
#     return 56
#
# b = f_4()
# print(b)
# print(f_4())
#
# temp()

# None : 반환값을 명시하지 않았을 때의 반환값

# 2개의 정수 중에서 큰 값을 찾는 함수를 만드세요

def max2(a, b):
    # if a > b:
    #     return a
    #     # print(a, ' 가 ', b, ' 보다 더 큽니다')
    # elif a < b:
    #     return b
    #     # print(b, ' 가 ', a, ' 보다 더 큽니다')
    # else:
    #     return 0
    #     # print(a, ' 와  ', b, '는 같습니다')
    if a > b:
        # return a
        b = a
    return b




def max4(a, b, c, d):
    # max = 0
    # if a > b:
    #     max = a
    # else:
    #     max = b
    # if max < c:
    #     max = c
    # if max < d:
    #     max = d
    #
    # return max

    # return max2(max2(a,b),max2(c,d))
    return max2(max2(max2(a,b),c),d)

print(max4(1, 20, 20, 4))
