import random
import matplotlib.pyplot as plt
import math

def greet():
    print("-------------------")
    print("  Морской бой  ")
    print("  После ввода углов возвышения наблюдаем:  ")
    print("  V - всплеск от снаряда ГК  ")
    print("  О - всплеск от снаряда СК ")
    print("  Закрываем карту (Х), корректируем углы возвышения  ")
    print("-------------------")
greet()

x_ship = random.randint(5000, 10000)  # расположение цели
print('Дистанция до цели: ', x_ship, 'м')

class Gun:  # данные для стрельбы - скорость снаряда и угол орудия
    def __init__(self, projectile_velocity, angolo):
        self.projectile_velocity = projectile_velocity
        self.angolo = angolo


    def get_projectile_velocity(self):
        return self.projectile_velocity
    def get_angolo(self):
        return self.angolo

    def salvo(self):    # расчет дальности стрельбы
        self.range_ = self.projectile_velocity ** 2 * (math.sin(self.angolo * 0.035)) / (9.8 * 2.13)
        return self.range_

velocity_gk = 500   # скорость снаряда главного калибра
velocity_mk = 700   # скорость снаряда среднего калибра

shot = 20           # количество выстрелов
while shot > 0:
    try:
        angolo_gk = float(input('Введите угол возвышения орудий главного калибра (8...35): ').replace(',','.'))
        angolo_mk = float(input('Введите угол возвышения орудий среднего калибра (4...15): ').replace(',','.'))
        if angolo_gk < 8 or angolo_gk > 35 and angolo_mk < 4 or angolo_mk > 15:
            raise ValueError("за пределами")
    except ValueError:
        print("Неправильный диапазон ввода")
        continue

    gk = Gun(velocity_gk, angolo_gk)
    x_gk = (gk.salvo())
    #print('Дальность стрельбы ГК ', x_gk)

    mk = Gun(velocity_mk, angolo_mk)
    x_mk = (mk.salvo())
    #print('Дальность стрельбы СК ', x_mk)


    def map():
        left_edges = [x_ship]
        heights = [20]
        bar_width = 50
        plt.xlabel('Дальность')
        plt.xticks([x_ship], ['ЦЕЛЬ'])
        x_coords = [3, 12]  # координаты дистанции в км
        y_coords = [0, 0]
        x_coords_gk = [x_gk]  # координаты падения снарядов ГК
        y_coords_gk = [10]
        x_coords_mk = [x_mk]  # координаты падения снарядов СК
        y_coords_mk = [5]
        plt.plot(x_coords, y_coords)  # построение дистанции
        plt.plot(x_coords_gk, y_coords_gk, marker='v')  # построение падения снарядов ГК
        plt.plot(x_coords_mk, y_coords_mk, marker='o')  # построение падения снарядов СК
        plt.bar(left_edges, heights, bar_width)  # Построить карту.
        plt.show()  # Показать карту.
    map()

    if x_ship <= x_gk <= (x_ship + 30) or x_ship <= x_mk <= (x_ship + 30):
        print('Цель поражена!')
        print('Конец игры')
        break

    shot -= 1
    if shot == 0:
        print('Боеприпасы закончились')
        print('Конец игры')
        break


