# Задание 1
class Matrix:
    def __init__(self,a,b,c,d):
        self.a = [[a,b],
                  [c,d]]
    def __str__(self):
        return f'{self.a[0][0]} | {self.a[0][1]}\n--|--\n{self.a[1][0]} | {self.a[1][1]}'

    def __add__(self, other):
        return Matrix(self.a[0][0] + other.a[0][0], self.a[0][1] + other.a[0][1], self.a[1][0] + other.a[1][0], self.a[1][1] + other.a[1][1])


m1 = Matrix(1,2,3,4)
m2 = Matrix(1,1,1,1)
print(m1 + m2)

# Задание 2
from abc import ABC, abstractmethod
class MyAbstract(ABC):
    @abstractmethod
    def fab(self):
        pass

class Clothes(MyAbstract):
    def __init__(self,name):
        self.name = name

class Coat(Clothes):
    def __init__(self,size):
        self.__size = size
    @property
    def g(self):
        return self.__size
    @g.setter
    def g(self,size):
        if size > 62 or size < 40:
            print('Неподходящее значение')
        else:
            self.__size = size

    def fab(self):
        f = self.__size / 6.5 + 0.5
        return f

class Suit(Clothes):
    def __init__(self, growth):
        self.__growth = growth
    @property
    def g(self):
        return self.__growth
    @g.setter
    def g(self,growth):
        if growth > 220 or growth < 100:
            print('Неподходящее значение')
        else:
            self.__growth = growth

    def fab(self):
        f = 2 * self.__growth + 0.3
        return f



coat = Coat(52)
suit = Suit(170)
suit.fab()
coat.fab()
print(f'Общий расход ткани: {suit.fab() + coat.fab()}')
suit.g = 160
print(suit.g)
coat.g = 42
print(coat.g)

# Задание 3
class Cell:
    def __init__(self,n):
        self.n = n
    def __str__(self):
        return f'Количество ячеек клетки: {self.n}'
    def __add__(self, other):
       return Cell(self.n + other.n)
    def __sub__(self, other):
        if self.n - other.n > 0:
            return Cell(self.n - other.n)
        else:
            print('Действие невозможно!')
    def __mul__(self, other):
        return Cell(self.n * other.n)
    def __truediv__(self, other):
        if other.n != 0:
            return Cell(self.n // other.n)
        else:
            print('Делить на 0 нельзя!')

    def make_order(self,a):
        self.a = a
        c = self.n % self.a
        if c == 0:
            b = self.n // self.a
            str = ''.join(['*' * self.a,'\n'])
            new_str = str * b
            print(new_str)
        else:
            b = self.n // self.a
            str = ''.join(['*' * self.a, '\n'])
            new_str = str * b
            new_str1 = ''.join([new_str,'*' * c])
            print(new_str1)


cell1 = Cell(15)
cell2 = Cell(14)
cell3 = Cell(1)
print(cell1)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1+cell2+cell3)
cell1.make_order(4)
