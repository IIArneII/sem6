from pygame import draw
from pygame import Surface


def axes(surface: Surface, color) -> None:
    x = int(surface.get_width() / 2)
    y = int(surface.get_height() / 2)
    draw.aaline(surface, color, (x, 0), (x, surface.get_height()))
    draw.aaline(surface, color, (0, y), (surface.get_width(), y))
