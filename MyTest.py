import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import AKF
import LogMap
import WorkWFiles


def do_profile(array):
    p_array = []
    sr = np.mean(array)
    for i in range(len(array)):
        y_array = []
        for j in range(i):
            y_array.append(array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


if __name__ == '__main__':
    t = np.linspace(0, 1, 500, endpoint=False)
    x = signal.square(2 * np.pi * 5 * t)
    y = LogMap.do_map()
    plt.plot(y)
    plt.show()
    AKF.do_all_akf(y)
