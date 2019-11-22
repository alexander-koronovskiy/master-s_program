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


def do_pic():
    # take a solution; save plots in png format
    ld = os.listdir(path="nefr")
    for i in ld:
        for j in range(1, 4):
            # get a solution
            solution = WorkWFiles.write_to_list('nefr/' + i);
            s = solution[j::4]
            # s = do_profile(s)
            # t = DFA.do_dfa(s)

            # save results as png
            plt.plot(s);
            grid(True)
            # plt.plot(t[1])
            figure(1, figsize=(10, 8))
            # xlabel('$log_2 n$'); plt.ylabel('$log_2 dfa$')
            xlabel('$Time, t$');
            plt.ylabel('Proximal pressure, mm Hg')
            # title('scaling exponent: {:.3f}'.format((max(t[0])-min(t[0]))/len(t[0])))
            # legend(('nefr'), prop=FontProperties(size=12))
            savefig('nefr_pics/' + str(i[:-4:]) + '_' + str(j) + '.png', dpi=100);
            plt.clf()


if __name__ == '__main__':
    a = WorkWFiles.write_to_list('RR.txt', 'r')
    b = do_profile(a)
    # DFA.do_dfa(b)
