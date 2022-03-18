from pygame import draw
from figure2 import Figure2
from pygame import Surface
import numpy as np


def axes(surface: Surface, color) -> None:
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
    y = start[0]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    k = dy / dx
    for x in range(int(start[0]), int(end[0])):
        surface.set_at((x, int(y)), color)
        y += k


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
