# Задание 1
import time
class Trafficlight:
    def __init__(self,color):
        self.__color = color
    def running(self):
        count = 0
        while True:
            print('Red')
            time.sleep(7)
            print('Yellow')
            time.sleep(2)
            print('Green')
            time.sleep(7)
            count += 1
            if count == 10:
                break
tl = Trafficlight('gray')
tl.running()

# Второй способ
class Trafficlight:
    color = ['Red','Yellow','Green']
    def running(self):
        i = 0
        while True:
            if i < len(self.color):
                print(self.color[i])
                if i == 0:
                    time.sleep(7)
                else:
                    time.sleep(2)
            else: i = -1
            i += 1
tl = Trafficlight()
print(tl.running())

# Задание 2
class Road:
    def __init__(self,length,width):
        self._length = length
        print(f'Длина дороги в километрах: {self._length}')
        self._width = width
        print(f'Ширина дороги в метрах: {self._width}')
    def m(self,metr,sm):
        self.metr = metr
        print(f'Масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см: {metr}')
        self.sm = sm
        print(f'Число см толщины полотна: {sm}')
        n = self._length * self._width * self.metr * self.sm
        print(f'Масса асфальта, необходимая для покрытия всей дороги: {n}')

road1 = Road(10,3)
road1.m(25,100)

# Задание 3
class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Wage': wage, 'Bonus': bonus}
        print(self._income)
class Position(Worker):
    def get_full_name(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')
    def get_total_income(self):
        print('Доход сотрудника:', self._income.get('Wage') + self._income.get('Bonus'))

worker1 = Position('Sasha', 'Drobysheva', 'Doctor', 150,100)
worker1.get_full_name()
worker1.get_total_income()

# Задание 4
class Car:
    def __init__(self, speed,color,name):
        self.speed = speed
        self.color = color
        self.name = name
    def go(self):
        print('Car goes')
    def stop(self):
        print('Car stops')
    def turn(self):
        print('Car turns')
    def show_seed(self):
        print(f'Car`s speed is {self.speed}')
class TownCar(Car):
    def show_seed(self):
        if self.speed > 60:
            print('Скорость автомобиля превышена!')
        else:
            print(f'Car`s speed is {self.speed}')
class WorkCar(Car):
    def show_seed(self):
        if self.speed > 40:
            print('Скорость автомобиля превышена!')
        else:
            print(f'Car`s speed is {self.speed}')
class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

town_car1 = TownCar(70,'White','Opel')
print(town_car1.name)
town_car1.show_seed()

# Задание 5
class Stationery:
    def __init__(self,title):
        self.title = title
        print(self.title)
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self,color):
        self.color = color
        print(f'Цвет чернила:{self.color}')
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандаша')
class Handle(Stationery):
    def draw(self,thickness):
        self.thickness = thickness
        print(f'Толщина прорисовки: {self.thickness}мм.')

pen1 = Pen('Ручка')
pen1.draw('Cиний')

pencil1 = Pencil('Карандаш')
pencil1.draw()

handle1 = Handle('Маркер')
handle1.draw(5)