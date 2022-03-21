import math
from matplotlib import pyplot as plt

x = 38
a = 37
b = 1
M = 1000
lam = 0.1


def rand():
    global x
    t = x
    x = (a * x + b) % M
    return -1 / lam * math.log(t / M)


if __name__ == '__main__':
    n = 100
    xi = [rand() for i in range(n)]

    m_t = 1 / lam
    d_t = m_t ** 2

    m_o = sum(xi) / n
    d_o = sum([(i - m_o) ** 2 for i in xi]) / n

    h = (max(xi) - min(xi)) / (1 + 3.3221 * math.log(n, 10))

    intervals = [min(xi), min(xi) + h]

    while max(xi) >= intervals[-1]:
        intervals.append(intervals[-1] + h)

    ni = [0 for i in range(len(intervals) - 1)]
    for i in xi:
        for j in range(1, len(intervals)):
            if i < intervals[j]:
                ni[j - 1] += 1
                break

    x_m = sum([ni[i - 1] * (intervals[i - 1] + intervals[i]) / 2 for i in range(1, len(intervals))]) / n

    l = 1 / x_m
    P = [math.exp(-l * intervals[i]) - math.exp(-l * intervals[i + 1]) for i in range(len(ni) - 1)]
    ni_ = [i * n for i in P]

    X2 = sum([((ni[i] - ni_[i]) ** 2) / ni_[i] for i in range(len(ni) - 3)])

    print('Теоритическое мат ожидание:', m_t)
    print('Теоритическая дисперсия:', d_t)
    print('\nОценка мат ожидания:', m_o)
    print('Оценка дисперсии:', d_o)
    print('\nОшибка мат ожидания:', math.fabs(m_t - m_o))
    print('Ошибка дисперсии:', math.fabs(d_t - d_o))
    print('\nh:', h)
    print('min:', min(xi))
    print('max:', max(xi))
    print('Интервалы:', intervals)
    print('Количество интервалов:', len(ni))
    print('Частоты:', ni)
    print('Выборочное среднее через интервалы:', x_m)
    print('Теоритические частоты:', ni_)
    print('\nX^2:', X2, "< 12.6")
