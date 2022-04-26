import numpy as np
from matrix import scaling_3, shift_3, rotation_3


class Mesh:
    def __init__(self):
        self.points = np.array([[]])
        self.polygons = np.array([[]])
        self.normals = np.array([[]])

    def rotation(self, angle_x: float, angle_y: float, angle_z: float):
        self.points = rotation_3(self.points, angle_x, angle_y, angle_z)
        self.normals = rotation_3(self.normals, angle_x, angle_y, angle_z)

    def scaling(self, x: float, y: float, z: float):
        self.points = scaling_3(self.points, x, y, z)

    def shift(self, x: float, y: float, z: float):
        self.points = shift_3(self.points, x, y, z)

    def centre(self):
        return self.points.sum(axis=0) / len(self.points)


class Line(Mesh):
    def __init__(self, p1, p2):
        super(Line, self).__init__()
        self.points = np.array([[p1[0], p1[1], p1[2], 1],
                                [p2[0], p2[1], p2[2], 1]])
        self.polygons = np.array([[0, 1]])


class Cube(Mesh):
    def __init__(self, width: float = 1., height: float = 1., length: float = 1., c=(0., 0., 0.)):
        super(Cube, self).__init__()
        self.points = np.array([[c[0] + width / 2, c[1] - height / 2, c[2] - length / 2, 1],
                                [c[0] - width / 2, c[1] - height / 2, c[2] - length / 2, 1],
                                [c[0] + width / 2, c[1] + height / 2, c[2] - length / 2, 1],
                                [c[0] - width / 2, c[1] + height / 2, c[2] - length / 2, 1],
                                [c[0] + width / 2, c[1] - height / 2, c[2] + length / 2, 1],
                                [c[0] - width / 2, c[1] - height / 2, c[2] + length / 2, 1],
                                [c[0] + width / 2, c[1] + height / 2, c[2] + length / 2, 1],
                                [c[0] - width / 2, c[1] + height / 2, c[2] + length / 2, 1]])
        self.polygons = np.array([[0, 3, 1], [0, 3, 2],
                                  [4, 2, 0], [4, 2, 6],
                                  [5, 6, 4], [5, 6, 7],
                                  [1, 7, 5], [1, 7, 3],
                                  [0, 5, 4], [0, 5, 1],
                                  [2, 7, 6], [2, 7, 3]])
        self.normals = []
        for k, i in enumerate(self.polygons):
            if k % 2 == 0:
                s = np.cross(self.points[i[0]][:3] - self.points[i[1]][:3],
                             self.points[i[0]][:3] - self.points[i[2]][:3])
            else:
                s = np.cross(self.points[i[0]][:3] - self.points[i[1]][:3],
                             self.points[i[2]][:3] - self.points[i[0]][:3])
            self.normals.append(s / np.linalg.norm(s))
        self.normals = np.array(self.normals)
        self.normals = np.c_[self.normals, np.ones(len(self.normals))]
