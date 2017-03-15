import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# print(db)

ns = re.findall(r'[A-Z][a-z]+', db)
print(ns)

name = re.findall(r'T[a-z]+', db)
print(name)
name2 = re.findall(r'[A-SU-Z][a-z]+', db)
print(name2)

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634'''