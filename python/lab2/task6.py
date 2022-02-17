import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('keys', nargs='*')
    parser.add_argument('-s', '--sort', action="store_const", const=True)

    args = parser.parse_args()
    keys = args.keys
    if args.sort:
        keys.sort(key=lambda x: x.split('=')[1])
    for i in keys:
        i = i.split('=')
        print(f'Key: {i[0]} Value: {i[1]}')
