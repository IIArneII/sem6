import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--per-day', type=int)
    parser.add_argument('--per-week', type=int)
    parser.add_argument('--per-month', type=int)
    parser.add_argument('--per-year', type=int)
    parser.add_argument('--get-by', type=str, choices=['day', 'month', 'year'], default='day')

    args = parser.parse_args()

    multipliers = {'day': 1, 'month': 30, 'year': 360}
    if len([i for i in [args.per_day, args.per_week, args.per_month, args.per_year] if i]) == 1:
        if args.per_day:
            print(int(args.per_day * multipliers[args.get_by]))
        if args.per_week:
            print(int(args.per_week / 7 * multipliers[args.get_by]))
        if args.per_month:
            print(int(args.per_month / 30 * multipliers[args.get_by]))
        if args.per_year:
            print(int(args.per_year / 360 * multipliers[args.get_by]))
    else:
        print('Invalid number of arguments')
