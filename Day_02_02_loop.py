# if 문을 사용해서 입력 숫자만큼 인사해 보세요
n = 2
i=0
while i < 9:
    print (i,end=' ')
    print()
    i += 2

for i in range(0,5,1):
    print(i,end=' ')

for i in range(0,100,1):
    print('{:2}'.format(i),end=' ')
    if i % 10 == 0:
        print()