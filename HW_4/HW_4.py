from functools import reduce
from itertools import cycle, count
from math import factorial
from sys import argv

# Задание 1
print(argv)
print(f'Выроботка в часах: {argv[1]}. Cтавка в час: {argv[2]}. Премия: {argv[3]}')
path, ar1, ar2, ar3 = argv
print(ar1,ar2,ar3)
p1, p2, p3 = map(int, argv[1:])
n = p1 * p2 + p3
print(f'Заработная плата сотрудника: {n}')


# Задание 2
li = [12,13,6,67,1]
i = 0
l = len(li) - 2
for el in li:
    if li[i] < li[i+1]:
        print(li[i+1])
    if i < l:
        i += 1

# Через генератор:
li = [1,2,1,5,7,9,2,1,13]
new = [li[i+1] for i in range(len(li) - 1) if li[i+1] > li[i]]
print(new)

# Задание 3
new = [i for i in range(20,241) if i % 20 == 0 or i % 21 == 0]
print(new)

# Задание 4
li = [1,1,2,3,3,56,78,7,7,7,9,12,11,11]
new = [el for el in li if li.count(el) == 1]
print(new)

# Задание 5
def f1(a,b):
    return a * b
new = [i for i in range(100,1001) if i % 2 == 0]
print(reduce(f1, new))

# Задание 6
for el in count(5):
    print(el)
    if el > 15:
        break

li = [1, 4, 5]
i = 0
for el in cycle(li):
    print(el)
    i += 1
    if i > 10:
        break

# Задание 7
def f1(a, b):
    return a * b
def fact(n):
    new = [i for i in range(1,n + 1)]
    print('n! = ', reduce(f1, new))
    i = 0
    for el in new:
        if i < len(new):
            n = factorial(new[i])
            i += 1
            yield n

for el in fact(5):
    print(el)