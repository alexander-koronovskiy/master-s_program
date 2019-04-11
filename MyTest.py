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


if __name__ == '__main__':
    # dyn sys solutions or heartbeat RR txt files data
    y = WorkWFiles.write_to_list('RR.txt')
    ExtendedFunc.do_plot(y)
    # y = LogMap.do_map()[:1024:]
    z = do_profile(y)
    ExtendedFunc.do_dfa(z)
