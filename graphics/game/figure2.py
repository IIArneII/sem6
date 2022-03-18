import numpy as np
from matrix import rad


class Figure2:
    def __init__(self, *points):
        self.points = np.array(list(points))
        assert len(self.points.shape) == 2
        assert 2 <= self.points.shape[1] <= 3
        if self.points.shape[1] == 2:
            self.points = np.c_[self.points, np.ones(len(self.points))]

    def rotation(self, angle):
        r = angle * rad
        self.points = self.points.dot(np.array([[np.cos(r), np.sin(r), 0], [-np.sin(r), np.cos(r), 0], [0, 0, 1]]))

    def mean(self):
        return self.points.sum(axis=0) / len(self.points)
