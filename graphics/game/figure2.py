import numpy as np
from matrix import rad, scaling_2, rotation_2, shift_2


class Figure2:
    def __init__(self, *points):
        self.points = np.array(list(points))
        assert len(self.points.shape) == 2
        assert 2 <= self.points.shape[1] <= 3
        if self.points.shape[1] == 2:
            self.points = np.c_[self.points, np.ones(len(self.points))]

    def rotation(self, angle: float):
        self.points = rotation_2(self.points, angle)

    def scaling(self, x: float, y: float):
        self.points = scaling_2(self.points, x, y)

    def shift(self, x: float, y: float):
        self.points = shift_2(self.points, x, y)

    def mean(self):
        return self.points.sum(axis=0) / len(self.points)
