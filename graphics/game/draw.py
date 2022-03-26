from pygame import draw
from figure2 import Figure2
from pygame import Surface
import numpy as np


def axes(surface: Surface, color):
    x = int(surface.get_width() / 2)
    y = int(surface.get_height() / 2)
    draw.aaline(surface, color, (x, 0), (x, surface.get_height()))
    draw.aaline(surface, color, (0, y), (surface.get_width(), y))


def line_f(surface: Surface, start, end, color=(0, 0, 0)):
    if start[0] > end[0]:
        start, end = end, start
    for x in range(int(start[0]), int(end[0])):
        k = (end[1] - start[1]) / (end[0] - start[0])
        y = k * (x - start[0]) + start[1]
        surface.set_at((x, int(y)), color)


def line(surface: Surface, start, end, color=(0, 0, 0)):
    st = int(start[0]), int(start[1])
    en = int(end[0]), int(end[1])

    if st[0] > en[0]:
        st, en = en, st

    dx = en[0] - st[0]
    dy = en[1] - st[1]
    d = 0
    add = 1
    if np.abs(dy) < np.abs(dx):
        if dy < 0:
            add = -1
            dy *= -1
        y = st[1]
        print('\r' * 10, 'dx:', np.sign(dx), 'dy:', np.sign(dy), 'add:', add, end='')
        for x in range(st[0], en[0]):
            surface.set_at((x, y), color)
            d += 2 * dy
            if d > dx:
                y += add
                d -= 2 * dx
    else:
        x = st[0]
        if dy > 0:
            print('\r' * 10, 'dx:', np.sign(dx), 'dy:', np.sign(dy), 'add:', add, end='')
            for y in range(st[1], en[1], 1):
                surface.set_at((x, y), color)
                d += 2 * dx
                if d > dy:
                    x += add
                    d -= 2 * dy
        else:
            print('\r' * 10, 'dx:', np.sign(dx), 'dy:', np.sign(dy), 'add:', add, end='')
            for y in range(st[1], en[1], -1):
                surface.set_at((x, y), color)
                d -= 2 * dx
                if d < dy:
                    x += add
                    d -= 2 * dy


def draw_points(surface: Surface, f: Figure2, color=(0, 0, 0), coord_transform=True):
    if coord_transform:
        temp = f.points * np.array([1, -1, 1]) + np.array(
            [int(surface.get_width() / 2), int(surface.get_height() / 2), 0])
        for p in temp:
            surface.set_at((int(p[0]), int(p[1])), color)
    else:
        for p in f.points:
            surface.set_at((int(p[0]), int(p[1])), color)


def draw_figure(surface: Surface, f: Figure2, color=(0, 0, 0), coord_transform=True):
    if coord_transform:
        temp = f.points * np.array([1, -1, 1]) + np.array(
            [int(surface.get_width() / 2), int(surface.get_height() / 2), 0])
        for p in range(1, len(temp)):
            line(surface, temp[p - 1], temp[p], color)
        if len(temp) > 2:
            line(surface, temp[-1], temp[0], color)
    else:
        for p in range(1, len(f.points)):
            line(surface, f.points[p - 1], f.points[p], color)
        line(surface, f.points[-1], f.points[0], color)
