import os
from zipfile import ZipFile
import json
import shutil
import datetime
import schedule


def normal_size(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    current = 0
    while size >= 1024:
        current += 1
        size = round(size / 1024)
    return size, sizes[current]


def make_reserve_arc(source, dest):
    date = datetime.datetime.now()
    name = str(date.date()) + '-' + str(date.hour) + '-' + str(date.minute) + '-' + str(date.second)
    shutil.make_archive(os.path.join(dest, name), 'zip', root_dir=source)


def ku():
    h = datetime.datetime.now().hour % 12
    if h == 0:
        h = 12
    print('Ку ' * h)


def ku_pro(msg='Ку ', time=None):
    h = datetime.datetime.now().hour
    if time:
        time = list(map(int, time.split('-')))
        if time[0] < time[1] and (h < time[0] or h > time[1]):
            h %= 12
            if h == 0:
                h = 12
            print(msg * h)
        elif time[0] > time[1] and h > time[1] and h < time[0]:
            h %= 12
            if h == 0:
                h = 12
            print(msg * h)
    else:
        h %= 12
        if h == 0:
            h = 12
        print(msg * h)


if __name__ == '__main__':
    task = int(input('Ввежите номер задания: '))
    if task == 1:
        for f in os.listdir():
            if os.path.isfile(f):
                size = normal_size(os.path.getsize(f))
                print(f, '-', size[0], size[1])
    if task == 2:
        with ZipFile('sem.zip') as z:
            for f in z.infolist():
                path = os.path.split(f.filename)
                if not path[1]:
                    path = path[0].split('/')
                    print('  ' * len(path), path[-1])
                else:
                    size = normal_size(f.file_size)
                    print('  ' * len(path[0].split('/')) + '  ', path[1], '-', size[0], size[1])
    if task == 4:
        make_reserve_arc('dir', '.')
    if task == 5:
        n = 0
        with ZipFile('task5.zip') as z:
            for f in z.namelist():
                if os.path.splitext(f)[1] == '.json':
                    with z.open(f) as jf:
                        if json.load(jf)['city'] == 'Москва':
                            n += 1
        print(f'В Москве проживает {n} человек')
    if task == 6:
        schedule.every().hour.do(ku)
        while True:
            schedule.run_pending()
    if task == 7:
        schedule.every().second.do(ku_pro, msg='Привет ', time='20-02')
        while True:
            schedule.run_pending()

# # m = [0, 1, 0, 1, 0, 0, 1, 0, 0]
# # a = 0
# # b = 1
# # for i in m:
# #     if i == 0:
# #         b -= (b - a) / 2.
# #     else:
# #         a += (b - a) / 2.
# # print(a, b)
# n = 4
# a = 0.32482771
#
# for i in range(0, 500):
#     a = float('0.' + str(a ** 2)[n: 3 * n])
#     print(a)
#     plt.plot(a, i, '.')
# plt.show()
#
# # a *= a
# # a *= str(a * 1000)
# # a = int(a[n: n * 3]) / (n * 2)
# # print(a)
