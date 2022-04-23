from matplotlib import pyplot as plt
import numpy as np
import random


def f(x, y):
    a = -x ** 2 + y ** 3 < -1
    b = x + y < 1
    c = -2 < x < 2
    d = -2 < y < 2
    return a and b and c and d


if __name__ == '__main__':
    for n in [10, 100, 1000, 10000, 100000]:
        success = 0
        for i in range(n):
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-2, 2)
            if f(x, y):
                success += 1
        print(f'Площадь фигуры для {n} испытаний: {16 * success / n}\nПогрешность: {np.abs(6.84359 - 16 * success / n) / 6.84359}\n')
