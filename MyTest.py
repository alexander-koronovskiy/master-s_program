import matplotlib.pyplot
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

ITER = 2048


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
    p_array = []
    for i in range(itter_n):
        y_array = []
        for j in range(i):
            y_array.append(x_array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


def do_interpolation(array, i):
    x = np.linspace(0, ITER, num=i, endpoint=True)
    y = array[::ITER // i]
    f = interp1d(x, y)
    x_new = np.linspace(0, ITER, num=ITER, endpoint=True)
    return f(x_new)


# входные данные: массив / выходные - тоже массив данных, но с разным n
def do_dfa(array, steps):
    z_array = []
    for i in range(2, 11):
        interp = do_interpolation(array, steps**i)
        z_array.append((sum((array - interp)**2)/ITER)**(1/2))
        print(z_array[::-1])
    matplotlib.pyplot.semilogy(z_array[::-1])
    matplotlib.pyplot.title('Dependence between $lg$n and $lg F_{dna}$')
    matplotlib.pyplot.show()


def step_interpolation(array, steps):
    for i in range(1, 9):
        interp = do_interpolation(array, steps**i)
        matplotlib.pyplot.plot(interp)
        # write_to_file(f(x_new), 'interpolation_first.txt')
        # print(f(x_new))
        matplotlib.pyplot.plot(array)
        matplotlib.pyplot.title('Profile - orange, Interpolation - blue, segments = ' + str(steps**i - 1))
        matplotlib.pyplot.show()


def write_to_file(array, filename):
    f = open(filename, 'w')
    for index in array:
        f.write(str(index) + '\n')
    f.close()


def do_x_data(n):
    x_data = []
    for i in range(n):
        x_data.append(i)
    return x_data


def do_2d_x_data(n):
    x_data = []
    for i in range(n):
        x_data.append([i])
    return x_data


if __name__ == '__main__':
    data = do_profile()
    step_interpolation(data, 2)
