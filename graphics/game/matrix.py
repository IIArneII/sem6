import numpy as np
from numpy import ndarray

rad = np.pi / 180

REFLECT_2X = np.array([[1., 0, 0], [0, -1, 0], [0, 0, 1]])
REFLECT_2Y = np.array([[-1., 0, 0], [0, 1, 0], [0, 0, 1]])
REFLECT_2XY = np.array([[-1., 0, 0], [0, -1, 0], [0, 0, 1]])


def reflect_2x(p: ndarray):
    return p.dot(REFLECT_2X)


def reflect_2y(p: ndarray):
    return p.dot(REFLECT_2Y)


def reflect_2xy(p: ndarray):
    return p.dot(REFLECT_2XY)


def scaling_2(point: ndarray, x: float, y: float):
    print('sss')
    ab = point.sum(axis=0) / len(point)
    s = np.array([[x, 0., 0], [0, y, 0], [0, 0, 1]])
    s1 = np.array([[1., 0., 0], [0, 1, 0], [-ab[0], -ab[1], 1]])
    s2 = np.array([[1., 0., 0], [0, 1, 0], [ab[0], ab[1], 1]])
    return point.dot(s1.dot(s).dot(s2))


def shift_2(p: ndarray, x: float, y: float):
    return p.dot(np.array([[1., 0, 0], [0, 1, 0], [x, y, 1]]))


def rotation_2(p: ndarray, angle: float):
    r = angle * rad
    return p.dot(np.array([[np.cos(r), np.sin(r), 0], [-np.sin(r), np.cos(r), 0], [0, 0, 1]]))
