#  -------------------------------------------------------- 1 ----------------------------------------------------------
from time import sleep, perf_counter
from itertools import cycle


class TrafficLight:
    """ В private переменной color находится матрица, с цветом и временем переключения.
    В методе используется бесконечный цикл, который повторяет перебор элементов перемнной
    с необходимым ожиданием в секундах.
    """

    __color = [["red", 7], ["yellow", 2], ["green", 7], ["yellow", 2]]

    def running(self):
        for el in cycle(self.__color):
            for i, val in enumerate(self.__color):
                print(self.__color[i][0], perf_counter())
                sleep(self.__color[i][1])


light_1 = TrafficLight()
light_1.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import sleep


class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("Trafficlight is red now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)
            print("Trafficlight is green now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import *


class TrafficLight:
    __color = ['Зеленый', 'Желтый', 'Красный']
    stage = 1

    def running(self):
        i = 0
        while True:
            if TrafficLight.stage == 1:
                if i == 3: i = 0
                print('Светофор мигает')
                TrafficLight.stage = 2
                sleep(2)
            else:
                print(TrafficLight.__color[i])
                TrafficLight.stage = 1
                i += 1
                sleep(7)


t = TrafficLight()
t.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import sleep


class TrafficLight:
    __color = 0

    def running(self):
        # [красный, жёлтый, зелёный]
        lights = [
            {
                'name': 'красный',
                'color': '\x1b[41m',
                'delay': 7
            },
            {
                'name': 'жёлтый',
                'color': '\x1b[43m',
                'delay': 2
            },
            {
                'name': 'зелёный',
                'color': '\x1b[42m',
                'delay': 5
            }
        ]

        print('\nИмитация работы светофора:\n')

        while True:
            # формируем строку вывода (светофор)
            s = ''
            for i in range(3):
                if i == self.__color:
                    s += f'({lights[self.__color]["color"]}   \x1b[0m)'
                else:
                    s += '(   )'

            print(f'\r{s}', end='')
            # устанавливаем задержку
            sleep(lights[self.__color]["delay"])
            # меняем цвет
            self.__color = (self.__color + 1) % 3


lights = TrafficLight()
lights.running()


#  -------------------------------------------------------- 2 ----------------------------------------------------------


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def calc(self):
        print(f"Масса асфальта - {self._lenght * self._width * 25 * 5 / 1000} тонн")


def main():
    while True:
        try:
            road_1 = Road(int(input("Enter width of road in m: ")), int(input("Enter lenght of road in m: ")))
            road_1.calc()
            break
        except ValueError:
            print("Only integer!")


#  -------------------------------------------------------- 3 ----------------------------------------------------------


class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


meneger = Position("Dorian", "Grey", "СEO", 500000, 125000)
print(meneger.get_full_name())
print(meneger.position)
print(meneger.get_full_profit())


#  ------------------------------------------- вариант решения ---------------------------------------------------------

#  -------------------------------------------------------- 4 ----------------------------------------------------------

class Car:
    ''' Автомобиль '''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):
    ''' Городской автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):
    ''' Грузовой автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):
    ''' Спортивный автомобиль '''


class PoliceCar(Car):
    ''' Полицейский автомобиль '''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('"Полицайка"', 'белый', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Грузовичок"', 'хаки', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('"Спортивка"', 'красный', 120)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"Малютка"', 'жёлтый', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')


#  -------------------------------------------------------- 5 ----------------------------------------------------------


class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}))")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} pencil!")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} handle!")


stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
handle = Handle("COPIC")
handle.draw()

