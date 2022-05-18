from scipy.stats import poisson
from matplotlib import pyplot as plt
import numpy as np
import random


def with_probability(p):
    return random.random() <= p


start = 0
stop = 120

plt.plot([start, stop], [0, 0], 'b')
for i in range(120):
    if with_probability(0.01):
        plt.plot([i], [0], 'ro')

plt.show()
