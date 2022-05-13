import numpy as np
from numpy import ndarray


rad = np.pi / 180

REFLECT_2X = np.array([[1., 0, 0], [0, -1, 0], [0, 0, 1]])
REFLECT_2Y = np.array([[-1., 0, 0], [0, 1, 0], [0, 0, 1]])
REFLECT_2XY = np.array([[-1., 0, 0], [0, -1, 0], [0, 0, 1]])

REFLECT_3X = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
REFLECT_3Y = np.array([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
REFLECT_3Z = np.array([[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
REFLECT_3XY = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
REFLECT_3XZ = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
REFLECT_3YZ = np.array([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
REFLECT_3XYZ = np.array([[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])


def reflect_2x(p: ndarray):
    return p.dot(REFLECT_2X)


def reflect_2y(p: ndarray):
    return p.dot(REFLECT_2Y)


def reflect_2xy(p: ndarray):
    return p.dot(REFLECT_2XY)


def scaling_2(point: ndarray, x: float, y: float):
    ab = point.sum(axis=0) / len(point)
    s = np.array([[x, 0., 0], [0, y, 0], [0, 0, 1]])
    s1 = np.array([[1., 0, 0], [0, 1, 0], [-ab[0], -ab[1], 1]])
    s2 = np.array([[1., 0, 0], [0, 1, 0], [ab[0], ab[1], 1]])
    return point.dot(s1.dot(s).dot(s2))


def shift_2(p: ndarray, x: float, y: float):
    return p.dot(np.array([[1., 0, 0], [0, 1, 0], [x, y, 1]]))


def rotation_2(p: ndarray, angle: float):
    r = angle * rad
    return p.dot(np.array([[np.cos(r), np.sin(r), 0], [-np.sin(r), np.cos(r), 0], [0, 0, 1]]))


def reflect_3x(p: ndarray):
    return p.dot(REFLECT_3X)


def reflect_3y(p: ndarray):
    return p.dot(REFLECT_3Y)


def reflect_3z(p: ndarray):
    return p.dot(REFLECT_3Z)


def reflect_3xy(p: ndarray):
    return p.dot(REFLECT_3XY)


def reflect_3xz(p: ndarray):
    return p.dot(REFLECT_3XZ)


def reflect_3yz(p: ndarray):
    return p.dot(REFLECT_3YZ)


def reflect_3xyz(p: ndarray):
    return p.dot(REFLECT_3XYZ)


def scaling_3(point: ndarray, x: float, y: float, z: float):
    ab = point.sum(axis=0) / len(point)
    s = np.array([[x, 0., 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])
    s1 = np.array([[1., 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-ab[0], -ab[1], -ab[2], 1]])
    s2 = np.array([[1., 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [ab[0], ab[1], ab[2], 1]])
    return point.dot(s1.dot(s).dot(s2))


def scaling_3_point(point: ndarray, x: float, y:float, z: float):
    s = np.array([[x, 0., 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])
    return point.dot(s)


def shift_3(p: ndarray, x: float, y: float, z: float):
    return p.dot(np.array([[1., 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [x, y, z, 1]]))


def rotation_3x(p: ndarray, angle_x: float):
    r_x = angle_x * rad
    return p.dot(np.array([[1, 0, 0, 0],
                           [0, np.cos(r_x), np.sin(r_x), 0],
                           [0, -np.sin(r_x), np.cos(r_x), 0],
                           [0, 0, 0, 1]]))


def rotation_3y(p: ndarray, angle_y: float):
    r_y = angle_y * rad
    return p.dot(np.array([[np.cos(r_y), 0, -np.sin(r_y), 0],
                           [0, 1, 0, 0],
                           [np.sin(r_y), 0, np.cos(r_y), 0],
                           [0, 0, 0, 1]]))


def rotation_3z(p: ndarray, angle_z: float):
    r_y = angle_z * rad
    return p.dot(np.array([[np.cos(r_y), np.sin(r_y), 0, 0],
                           [-np.sin(r_y), np.cos(r_y), 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]]))


def rotation_3(p: ndarray, angle_x: float, angle_y: float, angle_z: float):
    return rotation_3z(rotation_3y(rotation_3x(p, angle_x), angle_y), angle_z)


def v(p: ndarray):
    r = np.sqrt(p[0] ** 2 + p[1] ** 2 + p[2] ** 2)
    fi = np.arccos(p[0] / np.sqrt(p[0] ** 2 + p[1] ** 2))
    teta = np.arccos(p[2] / r)
    return reflect_3yz(np.array([[1., 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-p[0], -p[1], -p[2], 1]]).dot(
        np.array([[np.cos(np.pi / 2 - fi), np.sin(np.pi / 2 - fi), 0, 0],
                  [-np.sin(np.pi / 2 - fi), np.cos(np.pi / 2 - fi), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    ).dot(
        np.array([[1, 0, 0, 0],
                  [0, np.cos(-(np.pi - teta)), np.sin(-(np.pi - teta)), 0],
                  [0, -np.sin(-(np.pi - teta)), np.cos(-(np.pi - teta)), 0],
                  [0, 0, 0, 1]])
    ))
