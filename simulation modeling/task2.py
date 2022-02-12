import math


x = 38
a = 37
b = 1
M = 1000


def rand():
    global x
    x = (a * x + b) % M
    return x / M


if __name__ == '__main__':
    n = 100
    xi = [rand() for i in range(1, n)]
    h = (max(xi) - min(xi)) / (1 + 3.3221 * math.log(n, 10))
    intervals = [min(xi) + i * h for i in range(0, round(1 / h) + 1)]
    ni = [0 for i in range(len(intervals) - 1)]
    for i in xi:
        for j in range(1, len(intervals)):
            if i < intervals[j]:
                ni[j - 1] += 1
                break
    print(intervals)
    print(ni)
    print(sum(ni))
