import pygame
import math
import draw
import matrix
import numpy as np
import figure2


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

        self.setting = False
        self.f = figure2.Figure2([0, 0, 1], [0, 0, 1])

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
                    self.f.points[1][0] = e.pos[0] - int(self.screen.get_width() / 2)
                    self.f.points[1][1] = -(e.pos[1] - int(self.screen.get_height() / 2))
                    self.f.points[0][0] = e.pos[0] - int(self.screen.get_width() / 2)
                    self.f.points[0][1] = -(e.pos[1] - int(self.screen.get_height() / 2))
            elif e.type == pygame.MOUSEMOTION:
                if self.setting:
                    self.f.points[1][0] = e.pos[0] - int(self.screen.get_width() / 2)
                    self.f.points[1][1] = -(e.pos[1] - int(self.screen.get_height() / 2))
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.f.points = matrix.reflect_2x(self.f.points)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.f.rotation(-1)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.f.rotation(1)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.f.scaling(1.1, 1.1)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.f.scaling(0.9, 0.9)
        if pygame.key.get_pressed()[pygame.K_w]:
            self.f.shift(0, 1)
        if pygame.key.get_pressed()[pygame.K_s]:
            self.f.shift(0, -1)
        if pygame.key.get_pressed()[pygame.K_d]:
            self.f.shift(1, 0)
        if pygame.key.get_pressed()[pygame.K_a]:
            self.f.shift(-1, 0)

    def update(self):
        pass

    def rendering(self):
        self.screen.fill((150, 200, 200))
        draw.axes(self.screen, (0, 0, 0))

        draw.draw_figure(self.screen, self.f)

        pygame.display.flip()

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(self.FPS_limitation)
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.event_handling()
            self.update()
            self.rendering()


from matplotlib import pyplot as plt


def line(start, end, color=(0, 0, 0)):
    y = int(start[1])
    dx = int(end[0]) - int(start[0])
    dy = int(end[1]) - int(start[1])
    d = 0
    if dx < 0:
        dx *= -1
    for x in range(int(start[0]), int(end[0]) + 1):
        d += 2 * dy
        if d > dx:
            y += 1
            d -= 2 * dx
        print(x, y)
        plt.plot(x, -y, 'o')


if __name__ == '__main__':
    w = Window()
    w.FPS_limitation = 120
    w.run()
