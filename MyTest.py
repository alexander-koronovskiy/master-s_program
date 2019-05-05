import numpy as np
import matplotlib.pyplot as plt
from accessory import WorkWFiles
import DFA
import os
from pylab import figure, plot, xlabel, grid, legend, title, savefig
from matplotlib.font_manager import FontProperties


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
    # take a solution; save plots in png format
    ld = os.listdir(path="indata")
    for i in ld:
        for j in range(1, 4):
            # get a solution
            solution = WorkWFiles.write_to_list('indata/' + i); s = solution[j::4]
            t = DFA.do_dfa(s)

            # save results as png
            plt.plot(t[0]); grid(True)
            plt.plot(t[1])
            figure(1, figsize=(10, 8))
            xlabel('$log_2 n$'); plt.ylabel('$log_2 dfa$')
            title(t[2]); grid(True)
            legend((r'$dfa_n$', r'$fit line$'), prop=FontProperties(size=12))
            savefig('outdata/' + str(i[:-4:]) + '_'+str(j)+'.png', dpi=100); plt.clf()
