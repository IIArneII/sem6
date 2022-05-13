import random as rand

if __name__ == '__main__':
    m = 1.5
    sigma = 0.5
    t = 100

    bulb = 0
    later = 0

    while later < t:
        later += rand.normalvariate(m, sigma)
        bulb += 1

    print(f'Сгорело {bulb} ломпочек за {t} лет')
    print(f'Среднее время жизни лампочки: {t / bulb}')
