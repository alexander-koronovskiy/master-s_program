import matplotlib.pyplot
from scipy.interpolate import interp1d
import numpy as np
import math

ITER = 1024


# функция
def log_map(x, r):
    return r * x * (1 - x)


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
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r) - sr)
    return x_array


# составление профиля функции - НЕ ТРОГАТЬ!!!! РАБОТАЕТ!!!
def do_profile(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    sr = sum(do_map()) / ITER
    p_array=[]
    for i in range(itter_n):
        y_array = []
        for j in range(i):
            y_array.append(x_array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


# входные данные: массив / выходные - тоже массив данных, но с разным n
def do_dfa(array, steps):
    z_array = []
    for i in range(2, 9):
        x = np.linspace(0, ITER, num=steps**i, endpoint=True)
        y = array[::ITER // (steps**i)]
        f = interp1d(x, y)
        x_new = np.linspace(0, ITER, num=ITER, endpoint=True)
        z_array.append((sum((array - f(x_new))**2)/ITER)**(1/2))
        print(z_array[::-1])
    matplotlib.pyplot.semilogy(z_array[::-1])
    matplotlib.pyplot.title('Dependence between $log$n and $log F_{dna}$')
    matplotlib.pyplot.show()


if __name__ == '__main__':
    data = do_dfa(do_profile(), 2)
