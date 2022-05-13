import random


def with_probability(p):
    return random.random() <= p


if __name__ == '__main__':
    n = 1000000

    detail_cost = 35
    material_cost = 20
    expenditure_cnc = 5
    expenditure_polish = 4
    expenditure_gt_thick = 3
    expenditure_polish_correction = 2

    cnc_less = 0.08
    cnc_gt = 0.12
    polish_up_proc = 0.03
    polish_dn_proc = 0.06

    cost = 0
    detail_count = 0
    profit = 0

    for i in range(n):
        cost += material_cost
        cost += expenditure_cnc
        if with_probability(cnc_gt + cnc_less):
            if with_probability(cnc_less / (cnc_less + cnc_gt)):
                continue
            else:
                cost += expenditure_gt_thick
        cost += expenditure_polish
        up, down = with_probability(polish_up_proc), with_probability(polish_dn_proc)
        if up and down:
            continue
        if up or down:
            cost += expenditure_polish_correction
        detail_count += 1
        cost -= detail_cost

    print(f'Выпущено {detail_count} деталей из {n}')
    print(f'Вероятность выпуска годной детали: {detail_count / n}')
    print(f'Средняя прибыль за одну деталь: {-cost / n}')
