# Задание 1
a = 15
b = 17 // 4
c = a + b / 13
print(c)
print(a % b)
text = 'Hello!'
text2 = ' My name is Sasha.'
print(text + text2)



# Задание 2
sec = int(input('Секунд: '))
h = sec // 3600
sec2 = sec % 3600
min = sec2 // 60
sec3 = sec2 % 60
print(f'{h}:{min}:{sec3}')



# Задание 3
n = input('n = ')
n2 = n + n
n3 = n + n + n
n = int(n)
n2 = int(n2)
n3 = int(n3)
print(n + n2 + n3)



# Задание 4
n = int(input('Введите число: '))
max = 0
while n > 0:
     last = n % 10
     if last > max:
         max = last
     n = n // 10
print('Наибольшая цифра в числе: ', max)


# Задание 5
v = int(input('Выручка: '))
i = int(input('Издержки: '))
if v > i:
    print('Фирма работает в прибыль.')
    p = v - i
    print('Прибыль:', p)
    rent = (p / v) * 100
    print('Рентабельность выручки:', rent, '%')
    n = int(input('Количество сотрудников: '))
    m = p / n
    print('Прибыль в расчете на одного сотрудника: ', m)
else:
    print('Фирма работает в убыток.')



# Задание 6
a = int(input('Пробежал километров в первый день: '))
b = int(input('Цель пробежать километров: '))
i = 1
while a < b:
    a = a + a * 0.1
    i = i + 1
print('Достигнет результата на', i, 'день.')
