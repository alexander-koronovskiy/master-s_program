import matplotlib.pyplot as plt
from accessory import WorkWFiles, ApproximationFunc
import os
from pylab import figure, plot, xlabel, grid, legend, title, savefig
from matplotlib.font_manager import FontProperties


def c_alpha(array):
    return (max(array) - min(array)) / len(array)


if __name__ == '__main__':
    # take a solution; save plots in png format
    ld = os.listdir(path="nefr_dfa")
    x = [i/10 for i in range(30)]
    for i in ld:
        for j in range(1, 4):
            solution = WorkWFiles.write_to_list('nefr_dfa/' + i); s = solution[j::4]
            t = ApproximationFunc.do_approximation(s, 1)

            # save results as png
            plt.plot(x, s); grid(True)
            plt.plot(x, t)
            title('scaling exponent: {:.3f}'.format(c_alpha(s)*10))
            xlabel('$lg n$'); plt.ylabel('$lg dfa$')
            figure(1, figsize=(10, 8))
            legend((r'$dfa_n$', r'$fit line$'), prop=FontProperties(size=12))
            savefig('nefr_p/' + str(i[:-4:]) + '.png', dpi=100); plt.clf()
