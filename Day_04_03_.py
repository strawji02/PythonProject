

def not_used():
    def f_1(a,b,c):
        print(a,b,c)

    f_1(1,2,3)          # position argument
    f_1(a=1, b=2, c=3)  # keyword argument
    f_1(c=3, a=1, b=2)
    f_1(1, c=3, b=2)
    print(12,34,end='\n', sep='*')
    print(12,34, sep='*', end='\n')

def f_2(a=0, b=0, c=0):
    print(a,b,c)

f_2(1,2,3)
f_2()
f_2(1)
f_2(1,2)

def f_3(*args):     # 가변인자, pack
    print(args)
    a, _ = args
    print(a,_)
# f_3()
# f_3(1)
f_3(1,2)

def f_4(**kwargs):
    print(kwargs) 

f_4()
f_4(a=1)
f_4(a=1, b=2)

a = [1,2,3]
print(a)
print(*a)
print(*a, sep='*')

