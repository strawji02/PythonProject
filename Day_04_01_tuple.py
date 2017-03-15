
a = (1, 2, 3)
print(a)
print(a[0], a[len(a)-1])

# a[0] = -1/    # 변경 불가
# a.apppend(4)  #변경 불가

b1, b2 = 1, 2
print(b1, b2)

b3 = 1, 2   # pack (tuple)
print(b3)

# b4, b5 = 1    #불가능
# print(b4)

b4, b5 = b3     #unpack
print(b4, b5)

b6, _ = b3      # placeholder , 2번째 값은 사용하지 않겠다

def dummy():
    return 56, 78

a = dummy()
print(a)
print(a[0],a[1])