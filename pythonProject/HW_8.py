# Задание 1
class Date:
    def __init__(self,date):
        self.d = date
    def __str__(self):
        return f'Day: {self.d[0]}, Month: {self.d[1]}, Year: {self.d[2]}'
    @classmethod
    def set_date(cls,date):
        li = []
        li.append(date[0:2])
        li.append(date[3:5])
        li.append(date[6:10])
        li = list(map(int,li))
        return Date(li)

    @staticmethod
    def get_date(obj):
        if obj.d[0] < 32 and obj.d[0] > 0 and obj.d[1] > 0 and obj.d[1] < 13 and obj.d[2] < 2023:
            return f'Day: {obj.d[0]}, Month: {obj.d[1]}, Year: {obj.d[2]}'
        else:
            return 'Некорректные данные'
date1 = '25-09-2022'
d = Date.set_date(date1)
print(Date.get_date(d))

# Задание 2
class Devision(Exception):
    def __init__(self,txt):
        self.t = txt

a = int(input('Введите значение а: '))
b = int(input('Введите значение b: '))
try:
    c = a / b
    if b == 0:
        raise Devision('делить на 0 нельзя!')
except ZeroDivisionError:
    print('Делить на 0 нельзя!')
else:
    print(c)
finally:
    print('End')

# Задание 3
class Num(Exception):
    def __init__(self,txt):
        self.t = txt

li = []
while True:
    n = input('Введите число: ')
    try:
        n = int(n)
        if isinstance(n,str):
            raise Num('Not a number')
    except ValueError:
        print('Not a number')
    else:
        li.append(n)
    finally:
        print(li)
    if n == 'stop':
        break

# Задания 4,5,6
class Stock:
    name = 'Chemical elements'
    city = 'Moscow'
    director = 'N.P.Petrov'
class Elements(Stock):
    def __init__(self,name,period):
        self.n = name
        self.p = period
    def __str__(self):
        return f'Список изотопов: {li}'
    def get_izotopes(self,*z):
        self.z = list(z)
        li = []
        i = 0
        while True:
            if i < len(self.z):
                di = {self.n : self.z[i]}
                li.append(di)
                i = i + 1
            else:
                break
        return li
class Metal(Elements):
    def __init__(self, name, period):
        super().__init__(name,period)
        self.val = 'const'
class NonMetal(Elements):
    def __init__(self, name, period):
        super().__init__(name,period)
        self.val = 'nonconst'


na = Metal('natrium',3)
print(na.get_izotopes(11,12,13))

# Второй проект
class Person:
    def __init__(self,name,surname):
        self.n = name
        self.s = surname

class Director(Person):
    def manage(self,res,*empl):
        for em in empl:
            em.work(res)

class Employee(Person):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.li = []

    def work(self,res):
        self.li.append(res)

class Responsobilities:
    def __init__(self,*res):
        self.res = list(res)
    def get_li(self):
        return self.res
d = Director('Ivan','Ivanov')
e1 = Employee('Petr','Petrov')
e2 = Employee('Nikita','Smotrov')
res = [1,2,3]
d.manage(res,e1,e2)
print(e1.li[0])


# Задание 7
class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = complex(a,b)
    def __str__(self):
        return f'Комплексное число: {self.c}'
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return Complex(self.a * other.a, self.b * other.b)

c1 = Complex(1,2)
c2 = Complex(3,4)
c3 = Complex(5,6)
print(c1 + c2 + c3)
print(c1 * c2 * c3)