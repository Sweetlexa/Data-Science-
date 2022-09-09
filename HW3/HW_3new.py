# Задание 1
def my_fun(a,b):
    if b != 0:
        res = a / b
        return res
    else:
        print('Делить на 0 нельзя!')

a = int(input('Введите а: '))
b = int(input('Введите b: '))
s = my_fun(a,b)
print(s)


def my_f(a,b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
a = int(input('Введите а: '))
b = int(input('Введите b: '))
s = my_f(a,b)
print(s)



# Задание 2
def info(fname, lname, yearb, city, email, phone):
    print(f'Ваши персональные данные: Имя: {fname}, Фамилия: {lname}, год рождения: {yearb}, город проживания: {city}, почта: {email}, телефон: {phone}.')

info(fname='Александра', lname= 'Дробышева', yearb= 1998, city= 'Москва', email= 'sweet@mail.ru', phone=123)

# Задание 3
def my_func(a,b,c):
    if a >= b and c >= b:
        n = a + c
        return n
    elif a >= c and b >= c:
        n = a + b
        return n
    elif b >= a and c >= a:
        n = c + b
        return n

s = my_func(2,1,7)
print(s)

# Второй способ
def my_fun(a,b,c):
    li = [a,b,c]
    m = min(li)
    if m in li:
        li.remove(m)
        s = sum(li)
        return s
print(my_fun(2,4,6))


# Задание 4
# Первый способ

def my_func(x,y):
    n = x ** y
    return n
s = my_func(2,-3)
print(s)

# Второй способ

def my_func(x,y):
    i = 1
    m = 1
    while i < abs(y):
        i += 1
        m = m * 1 / x
    if y == 0:
        x = 1
        return x
    x = 1 / x * m
    return x
s = my_func(2,-3)
print(s)


# Задание 5
#
def my_sum():
    while True:
        while True:
            li = (input('Enter data: ')).split()
            if 'stop' in li:
                r = li.index('stop')
                li = li[0:r]
                li = list(map(int, li))
                s = sum(li)
                print(s)
                return
            else:
                li = list(map(int, li))
                s = sum(li)
                print(s)
            while True:
                li = (input('Enter data: ')).split()
                if 'stop' in li:
                    r = li.index('stop')
                    li = li[0:r]
                    li = list(map(int, li))
                    s = s + sum(li)
                    print(s)
                    return
                else:
                    li = list(map(int, li))
                    s = s + sum(li)
                    print(s)
my_sum()


# Задание 6

def int_func(a):
    a = a.title()
    print(a)

int_func('sasha')

# Задание 7
def int_func():
    li = input(('Введите слова: ')).split()
    for word in li:
        word = word.title()
        print(word)

int_func()

