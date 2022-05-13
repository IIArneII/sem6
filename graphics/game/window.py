import pygame
import draw
import matrix
import numpy as np
import figure2
import mesh


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

        self.m1 = mesh.Line((0., 0, 0), (50., 0, 0))
        self.m2 = mesh.Line((0., 0, 0), (0., 50, 0))
        self.m3 = mesh.Line((0., 0, 0), (0., 0, 50))
        self.cube = mesh.Cube(200, 200, 200)
        self.v = matrix.v(np.array([500, 500, 500]))

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
            self.cube.rotation(1, 0, 0)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.cube.rotation(0, 1, 0)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.cube.rotation(0, 0, 1)
        if pygame.key.get_pressed()[pygame.K_d]:
            draw.light = matrix.rotation_3x(np.array([draw.light[0], draw.light[1], draw.light[2], 1]), 1)
            self.info()
        if pygame.key.get_pressed()[pygame.K_w]:
            draw.light = matrix.rotation_3z(np.array([draw.light[0], draw.light[1], draw.light[2], 1]), 1)
            self.info()
        if pygame.key.get_pressed()[pygame.K_a]:
            draw.light = matrix.rotation_3y(np.array([draw.light[0], draw.light[1], draw.light[2], 1]), 1)
            self.info()
        if pygame.key.get_pressed()[pygame.K_z]:
            draw.light = matrix.scaling_3_point(draw.light, 0.8, 0.8, 0.8)
            self.info()
        if pygame.key.get_pressed()[pygame.K_x]:
            draw.light = matrix.scaling_3_point(draw.light, 1.2, 1.2, 1.2)
            self.info()
        if pygame.key.get_pressed()[pygame.K_r]:
            draw.Ia += 1
        if pygame.key.get_pressed()[pygame.K_f]:
            draw.Ia -= 1
        if pygame.key.get_pressed()[pygame.K_t]:
            draw.Ks += 0.05
        if pygame.key.get_pressed()[pygame.K_g]:
            draw.Ks -= 0.05
        if pygame.key.get_pressed()[pygame.K_y]:
            draw.Kd += 0.05
        if pygame.key.get_pressed()[pygame.K_h]:
            draw.Kd -= 0.05
        if pygame.key.get_pressed()[pygame.K_u]:
            draw.P += 0.5
        if pygame.key.get_pressed()[pygame.K_j]:
            draw.P -= 0.5

    def info(self):
        print('\r' * 10, end='')
        print('%15s  %15s  %15s  %15s' % (draw.light[0], draw.light[1], draw.light[2], np.linalg.norm(draw.light)), end='')

    def update(self):
        pass

    def rendering(self):
        self.screen.fill((100, 100, 100))
        # draw.axes(self.screen, (0, 0, 0))

        # p1 = self.m1.points.dot(self.v)
        # p2 = self.m2.points.dot(self.v)
        # p3 = self.m3.points.dot(self.v)
        # draw.line(self.screen, (p1[0][0], p1[0][1]), (p1[1][0], p1[1][1]))
        # draw.line(self.screen, (p2[0][0], p2[0][1]), (p2[1][0], p2[1][1]))
        # draw.line(self.screen, (p3[0][0], p3[0][1]), (p3[1][0], p3[1][1]))

        # draw.mesh(self.screen, self.m1, self.v, color=(255, 0, 0))
        # draw.mesh(self.screen, self.m2, self.v, color=(0, 255, 0))
        # draw.mesh(self.screen, self.m3, self.v, color=(0, 0, 255))
        # draw.mesh(self.screen, self.cube, self.v)
        draw.mesh_normals(self.screen, self.cube, self.v)

        # draw.figure(self.screen, self.f)

        # draw.ellipse(self.screen, (150, 150), 50)



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
