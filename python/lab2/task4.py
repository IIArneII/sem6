import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('source')
    parser.add_argument('target')
    parser.add_argument('-u', '--upper', action="store_const", const=True)
    parser.add_argument('-l', '--lines', type=int)

    args = parser.parse_args()
    if os.path.isfile(args.source):
        with open(args.source, 'r') as f1:
            with open(args.target, 'w') as f2:
                lines = f1.readlines()
                if args.upper:
                    lines = list(map(lambda x: x.upper(), lines))
                if args.lines:
                    f2.writelines(lines[0: args.lines])
                else:
                    f2.writelines(lines)
    else:
        print('Source file does not exist')
