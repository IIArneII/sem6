import random as rand
from matplotlib import pyplot as plt
from scipy.stats import poisson

if __name__ == '__main__':
    lambd = 8 / 24
    m = 10
    sigma = 4
    t = 100

    train = 0
    cart = 0

    plt.plot([0, t], [0, 0], 'b')
    for i in range(t):
        for j in range(poisson.rvs(mu=lambd)):
            train += 1
            cart += round(rand.normalvariate(m, sigma))
            plt.bar([i], [j + 1])

    print(f'Прибыло {train} поездов за {t} часов')
    print(f'Прибыло {cart} вагонов за {t} часов')
    print(f'За сутки в среднем прибывало {train / t * 24} поездов')
    print(f'За сутки в среднем прибывало {cart / t * 24} вагонов')
    plt.show()
