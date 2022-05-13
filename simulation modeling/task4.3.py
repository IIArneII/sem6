from matplotlib import pyplot as plt
import numpy as np
import random


def ff(x):
    y = np.cbrt(-1 + x ** 2)
    return y


def ff2(x):
    y = 1 - x
    return y


def f(x, y):
    a = -x ** 2 + y ** 3 < -1
    b = x + y < 1
    c = -2 < x < 2
    d = -2 < y < 2
    return a and b and c and d


if __name__ == '__main__':
    for j, n in enumerate([10, 100, 1000]):
        success = 0
        if j < 3:
            plt.subplot(1, 3, j + 1)
            xx = np.linspace(-2, 2, 100)
            plt.plot(xx, ff(xx), 'g')
            xx = np.linspace(-2, 2, 100)
            plt.plot(xx, ff2(xx), 'g')
        for i in range(n):
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-2, 2)
            if f(x, y):
                if j < 3:
                    plt.plot([x], [y], '.b')
                success += 1
            elif j < 3:
                plt.plot([x], [y], '.r')
        print(
            f'Площадь фигуры для {n} испытаний: {16 * success / n}\nПогрешность: {np.abs(6.84359 - 16 * success / n) / 6.84359}\n')
    plt.show()
