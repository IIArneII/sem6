from pygame import draw
from pygame import Surface
import math


def axes(surface: Surface, color) -> None:
    x = int(surface.get_width() / 2)
    y = int(surface.get_height() / 2)
    draw.aaline(surface, color, (x, 0), (x, surface.get_height()))
    draw.aaline(surface, color, (0, y), (surface.get_width(), y))


def line(surface: Surface, color, start_pos, end_pos):
    if start_pos[0] > end_pos[0]:
        start_pos, end_pos = end_pos, start_pos
    for x in range(int(start_pos[0]), int(end_pos[0])):
        y = start_pos[1] + int(30 * math.tan((end_pos[1] - start_pos[1]) * (x - start_pos[0]) / (end_pos[0] - start_pos[0] + 0.1) + start_pos[1]))
        surface.set_at((x, y), color)
