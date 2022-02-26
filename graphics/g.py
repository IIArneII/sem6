from typing import Any, List, Optional, Sequence, Text, Tuple, Union, overload, Iterable
import pygame
from pygame import draw
import math


_ColorInput = Union[
    pygame.color.Color, str, List[int], Tuple[int, int, int], Tuple[int, int, int, int]
]


class Screen:
    def __init__(self, width=500, height=500):
        self.screen = pygame.display.set_mode((width, height))

    def set_at(self, x_y: Sequence[int], color: _ColorInput):
        self.screen.set_at(x_y, color)


class Window:
    def __init__(self, width=500, height=500, title='Window'):
        self.width = width
        self.height = height
        self.title = title
        self.FPS_limitation = 30
        self.running = False
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        pygame.display.set_caption(title)

    def event_handling(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass
        self.sprites.update()

    def rendering(self):
        self.screen.fill((150, 200, 200))

        draw.line(self.screen, (100, 0, 100), (20, 10), (40, 200))
        draw.aaline(self.screen, (100, 0, 100), (10, 10), (20, 200))

        for i in range(self.height):
            self.screen.set_at((int(self.width / 2), i), 0)

        for i in range(self.width):
            self.screen.set_at((i, int(self.height / 2)), 0)
            x = int(i - (self.width / 2))
            y = int(-30 * math.sin(x / 30) + self.height / 2)
            self.screen.set_at((i, y), (255, 255, 255))

        pygame.display.flip()

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(self.FPS_limitation)
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.event_handling()
            self.update()
            self.rendering()


if __name__ == '__main__':
    w = Window()
    w.run()
