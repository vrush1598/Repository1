hey = lambda z: z + 10
print(type(hey))
print(hey(7))

r = 'python'
rev = lambda x: x.upper()
print(rev(r))

lis1 = [1, 2, 3, 4, 5, 6, 7, 8]
x = tuple(filter(lambda x: x % 2 == 0, lis1))
print(x)
r = tuple(map(lambda x: x * 2, lis1))
print(r)
from functools import reduce
t = reduce(lambda x, y: x * y, lis1)
print(t)
t = reduce(lambda x, y: x - y, lis1)
print(t)



