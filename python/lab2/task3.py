import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('args', nargs='*')

    args = parser.parse_args()
    if args.args:
        print('\n'.join(args.args))
    else:
        print('no args')
