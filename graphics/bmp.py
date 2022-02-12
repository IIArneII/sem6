import math


def turn(line, bite=4):
    line = [line[::-1][2 * i: 2 * i + 2][::-1] for i in range(math.ceil(len(line) / 2))]
    if len(line[-1]) == 1:
        line[-1] = '0' + line[-1]
    line += ['00'] * (bite - len(line))
    print(line)
    line = list(map(lambda x: bytes(chr(int(x, 16)), 'utf8'), line))
    print(line)
    print()
    return b''.join(line)


def make_bmp(width=3, height=3):
    file_size = 130
    img_bias = 118
    header_size = 40
    img_size = 12

    bmp = b'BM' + turn(hex(file_size)[2:]) + b'\x00\x00\x00\x00' + turn(hex(img_bias)[2:]) + turn(hex(header_size)[2:]) + turn(
        hex(width)[2:]) + turn(hex(height)[2:]) + b'\x01\x00' + b'\x04\x00' + b'\x00\x00\x00\x00' + turn(
        hex(img_size)[2:]) + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
    bmp += b'\x00\x00\x00\x00' + b'\x00\x00\x80\x00' + b'\x00\x80\x00\x00' + b'\x00\x80\x80\x00' + b'\x80\x00\x00\x00' + b'\x80\x00\x80\x00' + b'\x80\x80\x00\x00' \
           + b'\x80\x80\x80\x00' + b'\xc0\xc0\xc0\x00' + b'\x00\x00\xff\x00' + b'\x00\xff\x00\x00' + b'\x00\xff\xff\x00' + b'\xff\x00\x00\x00' + b'\xff\x00\xff\x00' \
           + b'\xff\xff\x00\x00'
    bmp += b'\xff\xff\xff\x00\xff\xf0\x00\x00\xff\xf0\x00\x00\x0f\xf0\x00\x00'
    return bmp


if __name__ == '__main__':
    w = 3
    h = 3
    with open('f.bmp', 'wb') as f:
        f.write(make_bmp())
