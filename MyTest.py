import matplotlib.pyplot
from scipy.interpolate import interp1d
import numpy as np
import scipy.interpolate
import sys
sys.path.insert(0, "c:\\users\\alexander\\anaconda3\\lib\site-packages")
from pandas import *

ITER = 1000


# функция
def log_map(x, r):
    return r * x * (1 - x)


# запись значений функции
# входные данные: число итераций, шаг, параметр нелинейности
# выходные данные: массив значений итеративной функции
# пока i в массиве, применяем к точке функцию, затем - добавляем в общий массив
def do_map(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return x_array


def do_map_w_average(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    sr = sum(do_map()) / ITER
    print(sr)
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r) - sr)
    return x_array


# составление профиля функции - НЕ ТРОГАТЬ!!!! РАБОТАЕТ!!!
# входные данные: число итераций, шаг, параметр нелинейности
# выходные данные: массив значений профиля функции
# пока i в массиве, запоминаем i, и до значения i суммируем значения функции
def do_profile(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    sr = sum(do_map()) / ITER
    #print(sr)
    p_array=[]
    for i in range(itter_n):
        y_array = []
        for j in range(i):
            y_array.append(x_array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


# разделение списка на n частей
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


# главный метод
# построить профиль функци ++
# линейная апроксимация при на n-ном участке
# вычисление функции fdfa
if __name__ == '__main__':
    p_array = do_profile()

    matplotlib.pyplot.plot(p_array)
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()
