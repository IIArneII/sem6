import sys
import os


if __name__ == "__main__":
    path = sys.argv[1:]
    if '--sort' in path:
        path.remove('--sort')
    if '--count' in path:
        path.remove('--count')
    if '--num' in path:
        path.remove('--num')
    if path and os.path.isfile(path[0]):
        with open(path[0], 'r') as f:
            lines = f.readlines()
            if '--sort' in sys.argv:
                lines.sort()
            for i in range(len(lines)):
                if '--num' in sys.argv:
                    print(i, '', end='')
                print(lines[i], end='')
            if '--count' in sys.argv:
                print('rows count:', len(lines))
    else:
        print('ERROR')
