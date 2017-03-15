
a = 123.45
b = 'python'

print('{}'.format(a))
print('*{:10}*'.format(a))
print('*{:.5f}*'.format(a))

print('#{}#'.format(b))
print('#{:10}#'.format(b))
print('#{:>10}#'.format(b))
print('#{:^10}#'.format(b))
print('#{:<10}#'.format(b))

print('{0} {1}'.format(a, b))
print('{1} {0}'.format(a, b))
print('{1} {0} {1} {0}'.format(a, b))
print('-'*50)

a = [1, 3, 5, 7, 9]

# 문제
# a를 거꾸로 출력해 보세요

# print('{4} {3} {2} {1} {0}'.format(c))
for i in reversed(range(len(a))):   # reversed() 사용시 range(len(a))등을 넣으면 됨
    print(a[i],end=' ')

print('-'*50)

s1={}
print(type(s1))
s2={0}
print(type(s2))
s3=set()
print(type(s3))
s4={1,2,3,1,2,3,1,2,3,1,2,3}
print(s4)
s5=[1,2,3,1,2,3,1,2,3,1,2,3]
print(s5)

# s5에서 중복제거

s5 = list(set(s5))
print(s5)
print('-'*50)


d = {'name': 'univ', 'addr': 'seoul', 'size': 100}
print(d)
print(d['name'], d['size'])

d['area'] = 12.34   # insert
print(d)

d['area'] = 56.78   # update
print(d)

print(d.keys())
print(d.values())
print(d.items())

for k in d.keys():
    print(k, d[k])

for v in d.values():
    print(v)

for i in d.items():
    print(i[0], i[1])

# c =(1, 3)
# a, b = c
# print(a, b)

for k, v in d.items():
    print(k, v)

for i, k in enumerate(d):
    print(i, k)


for i in enumerate(d.items()):
    # print(i)
    # print(i[0], i[1])
    print(i[1][0], i[1][1])

for i, (k, v) in enumerate(d.items()):
    print(i, k, v)