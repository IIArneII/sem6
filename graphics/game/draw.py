from pygame import draw
from figure2 import Figure2
from mesh import Mesh
from pygame import Surface
import numpy as np
from numba import njit
import pygame
import time


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
        for x in range(st[0], en[0]):
            surface.set_at((x, y), color)
            d += 2 * dy
            if d > dx:
                y += add
                d -= 2 * dx
    else:
        x = st[0]
        if dy > 0:
            for y in range(st[1], en[1], 1):
                surface.set_at((x, y), color)
                d += 2 * dx
                if d > dy:
                    x += add
                    d -= 2 * dy
        else:
            for y in range(st[1], en[1], -1):
                surface.set_at((x, y), color)
                d -= 2 * dx
                if d < dy:
                    x += add
                    d -= 2 * dy


def ellipse(surface: Surface, p, r, color=(0, 0, 0)):
    point = int(p[0]), int(p[1])
    x = 0
    y = r
    delta = 3 - 2 * r
    while y >= x:
        surface.set_at((point[0] + x, point[1] + y), color)
        surface.set_at((point[0] + x, point[1] - y), color)
        surface.set_at((point[0] - x, point[1] + y), color)
        surface.set_at((point[0] - x, point[1] - y), color)
        surface.set_at((point[0] + y, point[1] + x), color)
        surface.set_at((point[0] + y, point[1] - x), color)
        surface.set_at((point[0] - y, point[1] + x), color)
        surface.set_at((point[0] - y, point[1] - x), color)
        if delta < 0:
            delta += 4 * x + 6
        elif delta >= 0:
            y -= 1
            delta += 4 * (x - y) + 10
        x += 1


def figure_points(surface: Surface, f: Figure2, color=(0, 0, 0), coord_transform=True):
    if coord_transform:
        temp = f.points * np.array([1, -1, 1]) + np.array(
            [int(surface.get_width() / 2), int(surface.get_height() / 2), 0])
        for p in temp:
            surface.set_at((int(p[0]), int(p[1])), color)
    else:
        for p in f.points:
            surface.set_at((int(p[0]), int(p[1])), color)


def figure(surface: Surface, f: Figure2, color=(0, 0, 0), coord_transform=True):
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
        if len(f.points) > 2:
            line(surface, f.points[-1], f.points[0], color)


def mesh(surface: Surface, m: Mesh, v: np.ndarray, color=(0, 0, 0), coord_transform=True):
    e = m.points.dot(v)
    if coord_transform:
        e = e * np.array([1, -1, 1, 1]) + np.array(
            [int(surface.get_width() / 2), int(surface.get_height() / 2), 0, 0])
        for polygon in m.polygons:
            for p in range(1, len(polygon)):
                line(surface, e[polygon[p - 1]], e[polygon[p]], color)
            if len(polygon) > 2:
                line(surface, e[polygon[-1]], e[polygon[0]], color)
    else:
        for polygon in m.polygons:
            for p in range(1, len(polygon)):
                line(surface, e[p - 1], e[p], color)
            if len(polygon) > 2:
                line(surface, e[polygon[-1]], e[polygon[0]], color)


@njit(fastmath=True)
def ok(e, polygon, x, y):
    s1 = (e[polygon[0]][0] - x) * (e[polygon[1]][1] - e[polygon[0]][1]) - (
            e[polygon[1]][0] - e[polygon[0]][0]) * (e[polygon[0]][1] - y)
    s2 = (e[polygon[1]][0] - x) * (e[polygon[2]][1] - e[polygon[1]][1]) - (
            e[polygon[2]][0] - e[polygon[1]][0]) * (e[polygon[1]][1] - y)
    s3 = (e[polygon[2]][0] - x) * (e[polygon[0]][1] - e[polygon[2]][1]) - (
            e[polygon[0]][0] - e[polygon[2]][0]) * (e[polygon[2]][1] - y)
    if (s1 < 0 and s2 < 0 and s3 < 0) or (s1 > 0 and s2 > 0 and s3 > 0):
        return True
    else:
        return False


@njit()
def zz(p1, p2, p3, x, y):
    return -(p1[0]*p3[1]*p1[2]-p2[0]*p3[1]*p1[2]-p3[1]*p1[2]-p1[0]*p2[1]*p1[2]+p3[0]*p2[1]*p1[2]+p2[1]*p1[2]+p1[0]*p1[1]*p2[2]-p3[0]*p1[1]*p2[2]-p1[1]*p2[2]+p3[1]*p2[2]-p1[0]*p1[1]*p3[2]+p2[0]*p1[1]*p3[2]+p1[1]*p3[2]-p2[1]*p3[2]+p3[1]*p1[2]*x-p2[1]*p1[2]*x+p1[1]*p2[2]*x-p3[1]*p2[2]*x-p1[1]*p3[2]*x+p2[1]*p3[2]*x+p2[0]*p1[2]*y-p3[0]*p1[2]*y-p1[0]*p2[2]*y+p3[0]*p2[2]*y+p1[0]*p3[2]*y-p2[0]*p3[2]*y)/(-p2[0]*p1[1]+p3[0]*p1[1]-p1[0]*p3[1]+p2[0]*p3[1]+p1[0]*p2[1]-p3[0]*p2[1])


@njit()
def Il(p1, p2, p3, x, y, fi, nn, light, Ia, Ks, Kd, P):
    z = zz(p1, p2, p3, x, y)
    M = np.array([x, y, z])
    ML = light - M
    teta = np.arccos(np.sum(ML * nn) / np.linalg.norm(ML))
    if -np.pi / 2 <= teta <= np.pi / 2:
        al = fi - teta
        return Ia * Ks * np.cos(al) ** P * Kd * np.cos(teta)
    return 0


@njit(fastmath=True)
def render(e, nn, polygons, mon, light, Ia, Ks, Kd, P):
    mon[:] = np.array([0, 0, 0])
    for i, polygon in enumerate(polygons):
        fi = np.arccos(np.sum(n_e * nn[i]))
        if -np.pi / 2 <= fi <= np.pi / 2:
            xx = [int(e[polygon[0]][0]), int(e[polygon[1]][0]), int(e[polygon[2]][0])]
            yy = [int(e[polygon[0]][1]), int(e[polygon[1]][1]), int(e[polygon[2]][1])]
            for x in range(min(xx), max(xx)):
                for y in range(min(yy), max(yy)):
                    if ok(e, polygon, x, y):
                        I = Il(e[polygon[0]], e[polygon[1]], e[polygon[2]], x, y, fi, nn[i], light, Ia, Ks, Kd, P)
                        mon[x + 250][y + 250][0] = I
                        mon[x + 250][y + 250][1] = I
                        mon[x + 250][y + 250][2] = I
    return mon


n_e = np.array([-1, -1, -1]) / np.sqrt(3)
light = np.array([300, 300, 0, 1])
Ia = 255
Ks = 0.8
Kd = 0.8
P = 2


def mesh_normals(surface: Surface, m: Mesh, v: np.ndarray, color=(0, 0, 0)):
    e = m.points.dot(v)
    light_v = light.dot(v)
    nn = m.normals_s
    mon = np.full((surface.get_width(), surface.get_height(), 3), (0, 0, 0))
    mon = render(e, nn, m.polygons, mon, light_v[:3], Ia, Ks, Kd, P)
    pygame.surfarray.blit_array(surface, mon)
    # surface.set_at((int(x + surface.get_width() / 2), int(-y + surface.get_height() / 2)),
    #                (I, I, I))
