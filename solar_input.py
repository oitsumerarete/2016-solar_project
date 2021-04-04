# coding: utf-8
# license: GPLv3
import math
import matplotlib.pyplot as plt
import numpy as np

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    "Star 10 red 1000 1 2 3 4"
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    line = line.split(" ")
    star.R = int(line[1])
    star.color = line[2]
    star.m = float(line[3])
    star.x = float(line[4])
    star.y = float(line[5])
    star.Vx = float(line[6])
    star.Vy = float(line[7])



def parse_planet_parameters(line, planet):
    """
    Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    line = line.split(" ")
    planet.R = int(line[1])
    planet.color = line[2]
    planet.m = float(line[3])
    planet.x = float(line[4])
    planet.Vx = float(line[6])
    planet.y = float(line[5])
    planet.Vy = float(line[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            line = ""
            if obj.type == "star":
                line += 'Star '
            else:
                line += 'Planet'
            line += str(obj.R) + " "
            line += str(obj.color) + " "
            line += str(obj.m) + " "
            line += str(obj.x) + " "
            line += str(obj.y) + " "
            line += str(obj.Vx) + " "
            line += str(obj.Vy) + "\n"
            print(out_file, line)


def save_statistics(space_objects, time):
    file = open('stats.txt', 'a')
    for obj in space_objects:
        file.write(str(obj.x) + " " + str(obj.y) + " " + str(math.sqrt(obj.Vx ** 2 + obj.Vy ** 2)) + " " + str(time)
                   + "\n")
    file.close()


def process_statistics():
    x_star = np.array([])
    y_star = np.array([])
    v_star = np.array([])
    x_planet = np.array([])
    y_planet = np.array([])
    v_planet = np.array([])
    time_star = np.array([])
    time_planet = np.array([])
    file = open('stats.txt', 'r')
    type_ = True
    for line in file:
        line = line.split(" ")
        if type_:
            x_star = np.append(x_star, float(line[0]))
            y_star = np.append(y_star, float(line[1]))
            v_star = np.append(v_star, float(line[2]))
            time_star = np.append(time_star, float(line[3]))

        if not type_:
            x_planet = np.append(x_planet, float(line[0]))
            y_planet = np.append(y_planet, float(line[1]))
            v_planet = np.append(v_planet, float(line[2]))
            time_planet = np.append(time_planet, float(line[3]))

        type_ = not type_
    ro = np.sqrt((x_star - x_planet) ** 2 + (y_star - y_planet) ** 2)
    plt.plot(ro, v_planet)
    plt.xlabel('Расстояние, м')
    plt.ylabel('Скорость, м/с')
    plt.title('Зависимость скорости спутника \n от расстояния до звезды')
    plt.grid()
    plt.savefig('velocity(distance).png')
    plt.show()
    file.close()


if __name__ == "__main__":
    print("This module is not for direct call!")