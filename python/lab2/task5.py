import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int, help='ssssssss')

    args = parser.parse_args()
    if args.a and args.b is None:
        parser.error("AAAAAAAAAAAAAAAAAAAAAAA")
    print(args)
