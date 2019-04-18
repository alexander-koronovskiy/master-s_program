import numpy as np
import matplotlib.pyplot as plt
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


if __name__ == '__main__':
    # non-stationary analysed sequence
    y = WorkWFiles.write_to_list('RR.txt')  # or y = LogMap.do_map()[:1024:]

    # white noise sequence
    mean = 0; std = 1
    num_samples = 1000
    y = np.random.normal(mean, std, size=num_samples)
    print(y)

    # time series plot
    plt.plot(y); plt.xlabel("t");
    plt.ylabel("Time series values"); plt.show()

    # one or double profile transform
    z = do_profile(y)
    w = do_profile(z)
    plt.plot(z); plt.show()
    # ExtendedFunc.do_dfa(z)
