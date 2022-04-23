import random


def with_probability(p):
    return random.random() <= p


if __name__ == '__main__':
    n = 100
    success = 0
    for i in range(n):
        a = with_probability(0.8)
        b = with_probability(0.7)
        c = with_probability(0.95)
        d = with_probability(0.85)
        e = with_probability(0.9)
        f = with_probability(0.7)
        if (a or b) and c and (d or e or f):
            success += 1
    print('Вероятность безотказной работы:', success / n)

