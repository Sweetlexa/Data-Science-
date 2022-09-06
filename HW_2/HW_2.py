# Задание 1
li = ['Sasha', 4,9876,34,[2,9], 67.9, 'I am a student']
for el in li:
    print(type(el))


# Задание 2
li = input('Введите значения: ').split()
a = 0
b = 1
i = 0
while i + 2 <= len(li):
    li[a + i], li[b + i] = li[b + i], li[a + i]
    i = i + 2
print(li)


# Задание 3

di = {'Лето' : [6,7,8], 'Зима' : [12,1,2], 'Осень' : [9,10,11],'Весна' : [3,4,5]}
n = int(input('Введите месяц: '))
for el in di:
    if n in di[el]:
        print(el)
        break

li = ['Лето', 'Зима','Весна','Осень']
n = int(input('Введите месяц: '))
if n == 12 or n == 1 or n == 2:
    print(li[1])
elif n == 3 or n == 4 or n == 5:
    print(li[2])
elif n == 6 or n == 7 or n == 8:
    print(li[0])
elif n == 9 or n == 10 or n == 11:
    print(li[3])


# Задание 4
li = input('Введите слова: ').split()
for i, el in enumerate(li, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f'{i}. {el}')

# Задание 5
r = [8,6,5,3]
n = int(input('Введите новый элемент рейтинга: '))
i = 0
for el in r:
    while n < el:
        i = i + 1
        break
r.insert(i,n)
print(r)

# Задание 5 (Через сортировку)
r = [8,6,5,3]
n = int(input('Введите новый элемент рейтинга: '))
r.append(n)
r.sort()
reverse = True
r.reverse()
print(r)

# Задание 6
name = input('Введите название товара: ')
price = int(input('Введите стоимость товара: '))
amount = int(input('Введите количество товара: '))
ed = input('Введите единицу измерения: ')
di = {'Название' : name, 'Стоимость' : price, 'Количество' : amount, 'Ед.' : ed}

name2 = input('Введите название товара: ')
price2 = int(input('Введите стоимость товара: '))
amount2 = int(input('Введите количество товара: '))
di2 = {'Название' : name2, 'Стоимость' : price2, 'Количество' : amount2, 'Ед.' : ed}

name3 = input('Введите название товара: ')
price3 = int(input('Введите стоимость товара: '))
amount3 = int(input('Введите количество товара: '))
di3 = {'Название' : name3, 'Стоимость' : price3, 'Количество' : amount3, 'Ед.' : ed}

li = [(1,di), (2,di2),(3,di3)]
print(li)
dic = {'Названия товаров' : [name, name2, name3], 'Стоимости товаров': [price, price2, price3], 'Количество товаров' : [amount, amount2, amount3], 'Ед.' : [ed]}
print(dic)