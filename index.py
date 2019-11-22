from modules import WorkWFiles

import numpy as np
import DFA


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
    a = WorkWFiles.write_to_list('data/RR.txt')
    b = do_profile(a)
    DFA.do_dfa(b)
    # MFDFA
    # DFA extended
    # time series visualisation
