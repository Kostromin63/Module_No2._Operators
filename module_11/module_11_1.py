# Домашнее задание по теме "Обзор сторонних библиотек Python"
#
# Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.
#
# Задача:
# Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
# После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями.
# К каждой библиотеке дана ссылка на документацию ниже.
# Если вы выбрали:
# requests - запросить данные с сайта и вывести их в консоль.
# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
# В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека
# и как вы расширили возможности Python с её помощью.
# Примечания:
# Можете выбрать не более 3-х библиотек для изучения.
# Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
# Файл module_11_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него и комментарий к
# использованным инструментам библиотек(-и).
# Успехов!
#
# ************************************************************************************************************
# **********************                     == PIL ==                     ***********************************
#
from PIL import Image, ImageDraw

im = Image.open("Вовка.jpg")
draw_text = ImageDraw.Draw(im)
draw_text.text((50, 50), 'Please thank you - pillow', fill=('red'))

im.show()

# ************************************************************************************************************
# **********************                    == REQUEST ==                  ***********************************
# Урбан на сайт не пустил (ошибка 403), пришлось на гит хаб

import requests


r = requests.get('https://api.github.com/events')

print(r.raise_for_status())
print(r.status_code)
print(r.encoding)
print(r.content)
print(r.text)
print(r.json())
print(r.headers)
print(r.cookies)
print(r.history)

# ************************************************************************************************************
# **********************                    == NUMPY ==                      *********************************
#

import numpy as np


a = np.arange(15).reshape(3, 5)

print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
type(a)
b = np.array([6, 7, 8])
print(b)
print(type(b))

# ************************************************************************************************************
# **********************                    == PYGAME ==                     *********************************
# Реализуйте игровую сцену, состоящую из движущейся цели и пушки, стреляющей снарядами.

import random
import sys
from time import sleep

import pygame
from pygame.color import THECOLORS

pygame.init()

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Cannon:
    def __init__(self):
        # TODO(1.1): создайте атрибуты пушки:
        #  * Цвет
        self.color = (255, 0, 0)
        #  * Список точек
        #  Пусть пушка отображается как равнобедренный треугольник с высотой
        #  и основанием по 50px. Отображается в середине окна
        #  на нижней границе, см. схему в начале файла.
        self.simbol = ((295, 479), (320, 429), (345, 479))
        ...

    def draw(self):
        # TODO(1.2): отобразите созданную в __init__ последовательность точек
        #  заданным цветом.
        ...
        return pygame.draw.lines(screen, self.color, True, self.simbol, width=1)


class Bullet:

    def __init__(self):
        # TODO(2.1): создайте атрибуты снаряда.
        #  * Центр окружности снаряда
        ...
        self.center_bullet = (320, 429)
        #  * Радиус
        self.radius = 5
        #  * Цвет
        self.color = (0, 0, 255)
        #  * Скорость (для тестов использовать значение 3)
        self.speed = 12

    def draw(self):
        # TODO(2.2): отобразите снаряд.
        ...
        return pygame.draw.circle(screen, self.color, self.center_bullet, self.radius, 0)

    def move(self):
        # TODO(2.3): реализуйте перемещение снаряда.
        #  Для этого нужно создать его новый центр со смещением speed по оси OY
        #  к началу коориднат.
        # TODO(2.4): если снаряд достиг верхней границы окна, создать новый снаряд.
        ...
        x = self.center_bullet[0]
        y = self.center_bullet[1] - self.speed
        if y <= 0:
            y = 429
        self.center_bullet = (x, y)


class Target:
    def __init__(self):
        # TODO(3.1): создайте атрибуты мишени.
        #  * Цвет
        ...
        self.color = (65, 72, 51)
        #  * Скорость
        self.speed = 3
        #  * Прямоугольник
        self.rect = pygame.Rect(0, 0, 50, 30)

    def draw(self):
        # TODO(3.2): отобразите мишень.
        ...
        pygame.draw.rect(screen, self.color, self.rect, 0)

    def move(self):
        # TODO(3.3): реализуйте движение мишени.
        #  При достижении края окна мишень должна менять направление движения
        #  на противположное. Это можно реализовать сменой знака сокрости.
        ...
        x = self.rect[0]
        y = self.rect[1]

        if x >= WIDTH - self.rect[2]:
            self.speed = -3
        elif x <= 0:
            self.speed = 3

        x = x + self.speed
        self.rect = pygame.Rect(x, y, 50, 30)


colors = list(THECOLORS.values())


def get_random_color():
    return random.choice(colors)


screen.fill(THECOLORS['white'])
font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('HELLO PLAYER!'), True, THECOLORS['green'])
screen.blit(text, (175, 50))
pygame.display.flip()
sleep(1)

text = font.render(str("FORWARD, LET'S LET'S GO."), True, THECOLORS['green'])
screen.blit(text, (50, 180))
pygame.display.flip()
sleep(3)

cannon = Cannon()
target = Target()
bullet = Bullet()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(THECOLORS['black'])

    target.move()
    bullet.move()

    # TODO(4.1): если мишень и снаряд пересеклись, сменить цвет мишени на
    #  случайный, создать новй снаряд.
    #  Для определения пересечения используйте метод прямоугольника:
    #    Rect.collidepoint(point)
    xb = bullet.center_bullet[0]
    yb = bullet.center_bullet[1]
    if target.rect.collidepoint((xb, yb)):
        pygame.draw.polygon(screen, (255, 0, 0), [(xb+30, yb+50), (xb+10, yb+30), (xb+50, yb-70), (xb, yb-5),
                                                  (xb-60, yb-50), (xb-10, yb), (xb-60, yb+40), (xb, yb+20)], width=0)
        font = pygame.font.SysFont('couriernew', 20)
        text = font.render(str("BA-BANG!!!..."), True, THECOLORS['yellow'])
        screen.blit(text, (xb+5, yb))
        pygame.display.flip()
        sleep(1)
        target.color = get_random_color()
        bullet.center_bullet = (320, 429)

    cannon.draw()
    target.draw()
    bullet.draw()

    pygame.display.flip()
    pygame.time.wait(33)
