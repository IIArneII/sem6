import pygame
from pygame import draw
import math
from draw import axes
import matrix
import numpy as np


class Window:
    def __init__(self, width=500, height=500, title='Window'):
        self.width = width
        self.height = height
        self.title = title
        self.FPS_limitation = 30
        self.running = False
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        pygame.display.set_caption(title)

        self.section = np.array([[0, 0, 1], [0, 0, 1]])
        self.setting = False

    def event_handling(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            elif e.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.setting:
                    self.setting = False
                else:
                    self.setting = True
                    self.section[1][0] = e.pos[0] - int(self.screen.get_width() / 2)
                    self.section[1][1] = e.pos[1] - int(self.screen.get_height() / 2)
                    self.section[0][0] = e.pos[0] - int(self.screen.get_width() / 2)
                    self.section[0][1] = e.pos[1] - int(self.screen.get_height() / 2)
            elif e.type == pygame.MOUSEMOTION:
                if self.setting:
                    self.section[1][0] = e.pos[0] - int(self.screen.get_width() / 2)
                    self.section[1][1] = e.pos[1] - int(self.screen.get_height() / 2)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.section = matrix.reflect_2x(self.section)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.section = matrix.rotation_2r(self.section)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.section = matrix.rotation_2l(self.section)

    def update(self):
        pass

    def rendering(self):
        self.screen.fill((150, 200, 200))
        axes(self.screen, (0, 0, 0))
        draw.aaline(self.screen, (0, 0, 0), (self.section[0][0] + int(self.screen.get_width() / 2),
                                             self.section[0][1] + int(self.screen.get_height() / 2)),
                                            (self.section[1][0] + int(self.screen.get_width() / 2),
                                             self.section[1][1] + int(self.screen.get_height() / 2)))
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
