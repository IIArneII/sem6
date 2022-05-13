import random as rand

if __name__ == '__main__':
    n = 100
    t = 1.5
    
    all_work = 0
    all_break = 0
    t2_break = 0
    for i in range(n):
        t1 = rand.expovariate(lambd=0.5)
        t2 = rand.expovariate(lambd=1)
        if t1 < t and t2 < t:
            all_break += 1
        elif t1 >= t and t2 >= t:
            all_work += 1
        elif t1 >= t and t2 < t:
            t2_break += 1
    print(f'Вероятность, что не откажет ни один: {all_work / n}')
    print(f'Вероятность, что откажет только второй: {t2_break / n}')
    print(f'Вероятность, что все откажут: {all_break / n}')
