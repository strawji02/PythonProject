

a = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
print(a[0], a[-2], a[len(a)-1])

print(a[:])
print(a[2:5])


print(a[:5])
print(a[:len(a)//2])
print(a[len(a)//2:])

print(a[::2])
print(a[1::2])

print(a[::-1])


print(a[-2::-2])

def cahnge(t):
    t[-1] = 99


b = a           # 얕은 복사
c = a.copy()    # 김픙 복사
d = a[:]        # 깊은 복사
a[0] = - 1
cahnge(a)
print(a)
print(b)
print(c)
print(d)










