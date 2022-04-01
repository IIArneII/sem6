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

    o_ni = ni.copy()
    o_ni_ = ni_.copy()
    for i in range(2, len(o_ni)):
        if o_ni[i] < 5:
            for j in range(i + 1, len(o_ni)):
                o_ni[i] += o_ni[j]
                o_ni_[i] += o_ni_[j]
            del o_ni[i + 1: len(o_ni)]
            del o_ni_[i + 1: len(o_ni_)]
            break

    o_ni[1] += o_ni[0]
    o_ni_[1] += o_ni_[0]
    del o_ni[0]
    del o_ni_[0]

    print('\nИнтервалы:', intervals)
    print('Количество интервалов:', len(o_ni))
    print('Частоты:', o_ni)
    print('Теоритические частоты:', o_ni_)

    X2 = sum([((ni[i] - ni_[i]) ** 2) / ni_[i] for i in range(len(ni) - 3)])

    print('\nX^2:', X2, "< 6")

    n_ni = [sum(ni[0: i]) for i in range(1, len(ni) + 1)]

    lap = lambda g: math.erf(g)
    max = 0
    print('\nСередины', '\t\t\tЧастоты', '\tНакопленные', '\tFn(x)', '\tF(x)', '\t\t\t\t|Fn(x) - F(x)|')
    for i in range(len(ni)):
        print((intervals[i] + intervals[i + 1]) / 2, end='\t')
        print(ni[i], end='\t\t\t')
        print(n_ni[i], end='\t\t\t\t')
        print(n_ni[i] / n, end='\t')
        if n_ni[i] / n == 1:
            print(end='\t')
        fx = 0.5 + lap((((intervals[i] + intervals[i + 1]) / 2) - m_o) / math.sqrt(d_o))
        print(round(fx, 16), end='\t')
        fx = math.fabs(n_ni[i] / n - fx)
        print(fx)
        if fx > max:
            max = fx

    print('\nМаксимальное расхождение:', max)
    print('Лямбда:', max * math.sqrt(n), '> 1.36')
