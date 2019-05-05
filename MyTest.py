import numpy as np
import matplotlib.pyplot as plt
from accessory import WorkWFiles, ApproximationFunc
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
    # step 1: take a solution; save plot as png format
    solution = WorkWFiles.file_to_list(); s = solution[1::4]
    WorkWFiles.list_to_graph(s, 'time series')

    # step 1.1: save a profile of func pic
    # profile = do_profile(solution); WorkWFiles.list_to_graph(profile)

    # step 2: save a plot of standard dfa method result as png file
    t = DFA.do_dfa(s)
    WorkWFiles.list_to_graph(t, 'dfa method result')
