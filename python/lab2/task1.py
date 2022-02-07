import sys


if __name__ == "__main__":
    argv = sys.argv[1:]
    if '--sort' in argv:
        argv.remove('--sort')
        argv.sort(key=lambda x: x.split('=')[1])
    for i in argv:
        i = i.split('=')
        print(f'Key: {i[0]} Value: {i[1]}')
