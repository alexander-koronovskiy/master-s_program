import matplotlib.pyplot
from scipy.interpolate import interp1d
import numpy as np

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
    #профиль функции
    p_array = do_profile()
    # разбиение с количеством шагов num_x на интервале
    num_x = 10
    x = np.linspace(0, 1000, num=num_x, endpoint=True)
    y = p_array[::ITER // num_x]
    # интерполяция
    f = interp1d(x, y)
    xnew = np.linspace(0, 1000, num=1000, endpoint=True)
    # графики
    matplotlib.pyplot.plot(f(xnew))
    matplotlib.pyplot.plot(p_array)
    matplotlib.pyplot.legend(['лин.интерп.шагов=' + str(num_x), 'профиль функции'], loc='best')
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()
