import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('file', type=str)
    parser.add_argument('-s', '--sort', action="store_const", const=True)
    parser.add_argument('-c', '--count', action="store_const", const=True)
    parser.add_argument('-n', '--num', action="store_const", const=True)

    args = parser.parse_args()

    if os.path.isfile(args.file):
        with open(args.file, 'r') as f:
            lines = f.readlines()
            if args.sort:
                lines.sort()
            for i in range(len(lines)):
                if args.num:
                    print(i, end=' ')
                print(lines[i], end='')
            if args.count:
                print('rows count:', len(lines))
    else:
        print('ERROR')
