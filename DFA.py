import math
import matplotlib.pyplot as plt
from accessory import ApproximationFunc


# optimal binary logarithmic step for dfa algorithm
def optimal_step(n):
    return math.floor(math.log2(n))


# dfa algorithm building
def do_dfa(array, q=0.3):
    # chose the step type: logarithm - iter_log or linear - iter
    iter_log = optimal_step(len(array)) // 2 + 1
    dfa_p = []
    for i in range(iter_log):
        # standard dfa algorithm realisation
        fits = ApproximationFunc.do_approximation(array, pow(2, i))
        point = sum(do_sq_diff_arrays(array, fits))/len(array)
        dfa_p.append(pow(point, 0.5))
        # visualization of approximation
        do_plot(fits, array)
    dfa_p.reverse()
    return dfa_p


# give a square different result between real values in two one-dimensional arrays
def do_sq_diff_arrays(x, y):
    a = [x]
    b = [y]
    c = [list(map(lambda a, b: (a - b)**2, a[i], b[i])) for i in range(len(a))]
    return c[0]


def do_plot(*args):
    for i in args:
        plt.plot(i)
    plt.show()
