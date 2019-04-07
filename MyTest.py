import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import AKF
import LogMap
import ExtendedFunc
import WorkWFiles
import math
import ApproximationFunc


def do_profile(array):
    p_array = []
    sr = np.mean(array)
    for i in range(len(array)):
        y_array = []
        for j in range(i):
            y_array.append(array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


def do_plot(*args):
    for i in args:
        plt.plot(i)
    plt.show()


if __name__ == '__main__':
    y = LogMap.do_map()
    z = do_profile(y)

    # задача 1 - разбить массив на n равных частей
    # аппроксимировать каждую часть
    u = ApproximationFunc.parting(z, 2)
    x0 = ApproximationFunc.do_x_data(0, len(u[0]))
    x1 = ApproximationFunc.do_x_data(len(u[0]), len(u[0]) + len(u[1]))

    bf0 = ApproximationFunc.best_fit(x0, u[0])
    bf1 = ApproximationFunc.best_fit(x1, u[1])
    do_plot(bf0 + bf1, u[0] + u[1])
