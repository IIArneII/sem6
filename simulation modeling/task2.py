import math


x = 38
a = 37
b = 1
M = 1000


def rand():
    global x
    t = x
    x = (a * x + b) % M
    return t / M


if __name__ == '__main__':
    n = 100
    xi = [rand() for i in range(n)]
    h = (max(xi) - min(xi)) / (1 + 3.3221 * math.log(n, 10))    # надо брать целую часть от знаменателя?
    # intervals = [min(xi) + i * h for i in range(0, round(1 / h) + 1)]
    intervals = [min(xi), min(xi) + h]

    while max(xi) >= intervals[-1]:
        intervals.append(intervals[-1] + h)

    ni = [0 for i in range(len(intervals) - 1)]
    ni_ = [0 for i in range(len(intervals) - 1)]
    for i in xi:
        for j in range(1, len(intervals)):
            if i < intervals[j]:
                ni[j - 1] += 1
                break

    x_m = sum(xi) / n
    #x_m = sum([ni[i - 1] * (intervals[i - 1] + intervals[i]) / 2 for i in range(1, len(intervals))]) / n

    d = sum([(i - x_m) ** 2 for i in xi]) / n
    #d = sum([ni[i - 1] * (((intervals[i - 1] + intervals[i]) / 2) - x_m) ** 2 for i in range(1, len(intervals))]) / n

    if n % 2 == 1:
        m = sorted(xi)[int(n / 2)]
    else:
        m = (sorted(xi)[int(n / 2) - 1] + sorted(xi)[int(n / 2)]) / 2

    o = math.sqrt(d)
    a = x_m - math.sqrt(3) * o     # Нужен ли корень над 3?
    b = x_m + math.sqrt(3) * o
    f = 1 / (b - a)

    ni_[0] = n * ((intervals[0] + intervals[1]) / 2 - a) / (b - a)
    for i in range(1, len(ni_) - 1):
        ni_[i] = n * ((intervals[i] + intervals[i + 1]) / 2 - (intervals[i - 1] + intervals[i]) / 2) / (b - a)
    ni_[-1] = n * (b - (intervals[-2] + intervals[-1]) / 2) / (b - a)

    # print(f'-----{b} - {(intervals[-2] + intervals[-1]) / 2} = {b - (intervals[-2] + intervals[-1]) / 2}')

    X2 = sum([((ni[i] - ni_[i]) ** 2) / ni_[i] for i in range(len(ni) - 3)])

    series = [1 if i >= m else 0 for i in xi]
    S = sum([1 if series[i] != series[i - 1] else 0 for i in range(1, len(series))]) + 1

    r = sum([(i + 1) * xi[i] for i in range(len(xi))]) / n - sum(xi) / n * (n + 1) / 2
    r /= math.sqrt((sum([i ** 2 for i in xi]) / n - (sum(xi) / n) ** 2) * (n ** 2 - 1) / 12)

    r_ = (1 - r ** 2) / math.sqrt(n)

    print('min:', min(xi))
    print('max:', max(xi))
    print('h: ', h)
    print('Интервалы:', intervals)
    print('Количество интервалов:', len(ni))
    print('Частоты:', ni)
    print('Сумма частот:', sum(ni))
    print('Выборочное среднее:', x_m)
    print('Медиана:', m)
    print('Дисперсия:', d)
    print('Сигма:', o)
    print('a*:', a)
    print('b*:', b)
    print('Плотность вероятности:', f)
    print('Теоритические частоты:', ni_)
    print('\nX^2:', X2, "< 11.1")
    print(f'Количество серий S: 40 < {S} < 61')
    print('Коэффициент корреляции r:', r)
    print('r_max:', r_)
    print('Верхняя граница r_max при a = 0.95:', r_ * 0.06)
    print('Верхняя граница r_max при a = 0.05:', r_ * 1.96)




