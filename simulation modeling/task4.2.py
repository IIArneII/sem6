import random


def with_probability(p):
    return random.random() <= p


if __name__ == '__main__':
    n = 100000
    count = 0
    error = 0

    n1, n2, n3 = 0.2, 0.3, 0.5
    p1, p2, p3 = 0.8, 0.9, 0.95

    for i in range(n):
        if with_probability(1 - n1) and with_probability(1 - n2) and with_probability(1 - n3):
            continue
        o = random.random()
        error += 1
        if o < n1:
            if with_probability(p1):
                count += 1
        elif n1 <= o < n1 + n2:
            if with_probability(p2):
                count += 1
        elif n1 + n2 <= o <= n1 + n2 + n3:
            if with_probability(p3):
                count += 1

    print(f'Обноружено {count} ошибок из {error}')
    print(f'Вероятность, что ошибка обнаружена: {count / error}')
    print(f'Вероятность безотказной работы: {(n - error) / n}')
