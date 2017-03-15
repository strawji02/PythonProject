import Day_08_01_lambda

# for i in range(10):
#     for j in range(5):
#         if j%2 == 1:
#             j

print([i for i in range(10)])
print([0 for _ in range(10)])

a = [1, 3, 5, 7, 9]
print([i*i for i in a])

a1 = Day_08_01_lambda.makerandoms(5)
a2 = Day_08_01_lambda.makerandoms(5)
a3 = Day_08_01_lambda.makerandoms(5)

a = [a1, a2, a3]

print(a)
print(sum(a1), max(a1), min(a1))

print([i for i in a])
print([0 for i in a])
print([sum(i)for i in range])















