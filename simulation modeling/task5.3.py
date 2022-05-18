import random as rand
from scipy.stats import poisson

# if __name__ == '__main__':
#     m = 1.5
#     sigma = 0.5
#     t = 100
#
#     bulb = 0
#     later = 0
#
#     while later < t:
#         later += rand.normalvariate(m, sigma)
#         bulb += 1
#
#     print(f'Сгорело {bulb} ломпочек за {t} лет')
#     print(f'Среднее время жизни лампочки: {t / bulb}')

if __name__ == '__main__':
    m = 1.5
    sigma = 0.5
    t = 100

    lamb_k = 1 / m
    k = round(1 / (lamb_k ** 2 * sigma ** 2))
    lamb = lamb_k * k

    print(f'Порядок потока Эрланга: {k}')
    print(f'Интенсивность потока Эрланга: {lamb_k}')
    print(f'Интенсивность потока Пуассона: {lamb}')

    bulb = 0
    events = 0
    for i in range(t):
        events += poisson.rvs(mu=lamb)
        if events >= k:
            bulb += 1
            events -= k

    print(f'Сгорело {bulb} ломпочек за {t} лет')
    print(f'Среднее время жизни лампочки: {t / bulb}')