import numpy as np
from numpy import ndarray

rad = np.pi / 180

REFLECT_2X = np.array([[1., 0, 0], [0, -1, 0], [0, 0, 1]])
REFLECT_2Y = np.array([[-1., 0, 0], [0, 1, 0], [0, 0, 1]])
REFLECT_2XY = np.array([[-1., 0, 0], [0, -1, 0], [0, 0, 1]])

SCALING_2 = np.array([[1., 0, 0], [0, 1, 0], [0, 0, 1]])

SHIFT_2 = np.array([[1., 0, 0], [0, 1, 0], [0, 0, 1]])

ROTATION_2R = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]])
ROTATION_2L = np.array([[np.cos(-rad), np.sin(-rad), 0], [-np.sin(-rad), np.cos(-rad), 0], [0, 0, 1]])


def reflect_2x(p: ndarray):
    return p.dot(REFLECT_2X)


def reflect_2y(p: ndarray):
    return p.dot(REFLECT_2Y)


def reflect_2xy(p: ndarray):
    return p.dot(REFLECT_2XY)


def scaling_2(p: ndarray, x=None, y=None):
    if x and y:
        s1 = np.array([[1., 0., 0], [0, 1, 0], [-p[0], -p[1], 1]])
        s = np.array([[x, 0., 0], [0, y, 0], [0, 0, 1]])
        s2 = np.array([[1., 0., 0], [0, 1, 0], [p[0], p[1], 1]])
        print('ddd:')
        print(p.dot(s1.dot(s).dot(s2)))
        return p.dot(s1.dot(s).dot(s2))
    return p.dot(SCALING_2)


def shift_2(p: ndarray, x=None, y=None):
    if x and y:
        return p.dot(np.array([[1., 0, 0], [0, 1, 0], [x, y, 1]]))
    return p.dot(SHIFT_2)


def rotation_2r(p: ndarray):
    return p.dot(ROTATION_2R)


def rotation_2l(p: ndarray):
    return p.dot(ROTATION_2L)