import math
import os


def turn(line, bite=4):
    line = [line[::-1][2 * i: 2 * i + 2][::-1] for i in range(math.ceil(len(line) / 2))]
    if len(line[-1]) == 1:
        line[-1] = '0' + line[-1]
    line += ['00'] * (bite - len(line))
    line = list(map(lambda x: bytes.fromhex(x), line))
    return b''.join(line)


def make_bmp(width=3, height=3):
    if width % 8:
        file_size = 118 + height * int((width + 8 - width % 8) / 2)
    else:
        file_size = 118 + height * int(width / 2)
    img_bias = 118
    header_size = 40
    if width % 8:
        img_size = height * int((width + 8 - width % 8) / 2)
    else:
        img_size = height * int(width / 2)

    bmp = b'BM' + turn(hex(file_size)[2:]) + b'\x00\x00\x00\x00' + turn(hex(img_bias)[2:]) + turn(hex(header_size)[2:]) + turn(
        hex(width)[2:]) + turn(hex(height)[2:]) + b'\x01\x00' + b'\x04\x00' + b'\x00\x00\x00\x00' + turn(
        hex(img_size)[2:]) + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
    bmp += b'\x00\x00\x00\x00' + b'\x00\x00\x80\x00' + b'\x00\x80\x00\x00' + b'\x00\x80\x80\x00' + b'\x80\x00\x00\x00' + b'\x80\x00\x80\x00' + b'\x80\x80\x00\x00' \
           + b'\x80\x80\x80\x00' + b'\xc0\xc0\xc0\x00' + b'\x00\x00\xff\x00' + b'\x00\xff\x00\x00' + b'\x00\xff\xff\x00' + b'\xff\x00\x00\x00' + b'\xff\x00\xff\x00' \
           + b'\xff\xff\x00\x00'
    bmp += b'\xff\xff\xff\x00'

    print(len(bmp))

    if width % 8:
        width = width + 8 - width % 8

    for i in range(height):
        line = ''
        for j in range(width):
            if (i + j) % 2 == 0:
                line += '0'
            else:
                line += 'f'
        bmp += bytes.fromhex(line)

    return bmp


if __name__ == '__main__':
    # with open('f.bmp', 'wb') as f:
    #     f.write(make_bmp(10, 13))
    # os.startfile('f.bmp')
    print('hi')
