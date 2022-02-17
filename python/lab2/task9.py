import argparse


def format_text_block(frame_width, frame_height, file_name):
    with open(file_name, 'r') as f:
        lines = ''.join(list(map(lambda x: x[:-1] if x[-1] == '\n' else x, f.readlines())))
        return ''.join([lines[i: i + frame_width] + '\n' for i in range(0, len(lines), frame_width)][0: frame_height])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('frame_width', type=int)
    parser.add_argument('frame_height', type=int)
    parser.add_argument('file', type=str)

    args = parser.parse_args()
    try:
        lines = format_text_block(args.frame_width, args.frame_height, args.file)
        print(lines)
    except Exception as e:
        print(e)
