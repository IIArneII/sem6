xi = [0.1, 0.3, 0.6, 0.2, 0.7]
series = [1 if i >= 0.5 else 0 for i in xi]
d = sum([1 if series[i] != series[i - 1] else 0 for i in range(1, len(series))]) + 1
print(d)
