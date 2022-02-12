if __name__ == '__main__':
    task = int(input('Номер задания: '))
    if task == 1:
        m = [0, 1, 0, 1, 0, 0, 1, 0, 0]
        a = 0
        b = 1
        for i in m:
            if i == 0:
                b -= (b - a) / 2.
            else:
                a += (b - a) / 2.
        print(a, '-', b)
    if task == 2:
        n = 2
        a = 0.2152
        for i in range(0, 100):
            print('a**2:', round(a ** 2, n * 4))
            a = '0.' + str(round(a ** 2, n * 4))[n + 2: 3 * n + 2]
            if 'e' not in a:
                a = float(a)
            else:
                print('---', a)
                a = float(a[:a.find('e')])
            print(a, '\n')
