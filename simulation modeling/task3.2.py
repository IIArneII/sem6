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
    return t / M


if __name__ == '__main__':
    n = 100
    xi = [[rand() for j in range(12)] for i in range(n)]
    zi = [(sum(i) - 6) * 0.25 + 3 for i in xi]

    m_o = sum(zi) / n
    d_o = sum([(i - m_o) ** 2 for i in zi]) / n

    print('Матожидание:', m_o)
    print('Средне крадратическое отклонение', math.sqrt(d_o))
    print('Погрешность матожидания:', math.fabs(m_o - 3) / 3)
    print('Погрешность дисперсии:', math.fabs(math.sqrt(d_o) - 0.25) / 0.25)

    xi = [[rand() + 0.001 for j in range(2)] for i in range(n)]

    zi = [math.sqrt(-2 * math.log(i[0])) * math.cos(2 * math.pi * i[1]) * 0.25 + 3 for i in xi]

    m_o = sum(zi) / n
    d_o = sum([(i - m_o) ** 2 for i in zi]) / n

    print('\nМатожидание:', m_o)
    print('Средне крадратическое отклонение', math.sqrt(d_o))
    print('Погрешность матожидания:', math.fabs(m_o - 3) / 3)
    print('Погрешность дисперсии:', math.fabs(math.sqrt(d_o) - 0.25) / 0.25)

    h = (max(zi) - min(zi)) / (1 + 3.3221 * math.log(n, 10))

    intervals = [min(zi), min(zi) + h]

    while max(zi) >= intervals[-1]:
        intervals.append(intervals[-1] + h)

    ni = [0 for i in range(len(intervals) - 1)]
    for i in zi:
        for j in range(1, len(intervals)):
            if i < intervals[j]:
                ni[j - 1] += 1
                break

    fi = lambda x: 1 / math.sqrt(2 * math.pi) * math.exp(- (x ** 2) / 2)

    ni_ = [ n * h / math.sqrt(d_o) * fi(((intervals[i - 1] + intervals[i]) / 2 - m_o) / math.sqrt(d_o)) for i in range(1, len(intervals))]

    for i in range(2, len(ni)):
        if ni[i] < 5:
            for j in range(i + 1, len(ni)):
                ni[i] += ni[j]
                ni_[i] += ni[j]
            del ni[i + 1: len(ni)]
            del ni_[i + 1: len(ni_)]
            break

    print('\nИнтервалы:', intervals)
    print('Количество интервалов:', len(ni))
    print('Частоты:', ni)
    print('Теоритические частоты:', ni_)

    X2 = sum([((ni[i] - ni_[i]) ** 2) / ni_[i] for i in range(len(ni) - 3)])

    print('\nX^2:', X2, "< 7.8")

    for i in range(len(xi))
