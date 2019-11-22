from modules import ApproximationFunc

import math
import matplotlib.pyplot as plt


# DFA algorithm building
# chose the step type: logarithmic - iter_log defined by this.optimal_step function
# fits - X; point - Yk; dfa_p - array of F(L)
# closer_p - Linear approximation of F(L)
def do_dfa(array):
    iter_log = optimal_step(len(array)) // 2 + 1
    dfa_p = []

    for i in range(iter_log):
        fits = ApproximationFunc.do_approximation(array, pow(2, i))
        point = sum(do_sq_diff_arrays(array, fits))/len(array)
        dfa_p.append(math.log2(pow(point, 0.5)))

    dfa_p.reverse()
    do_plot(dfa_p)
    closer_p = ApproximationFunc.do_approximation(dfa_p, 1)
    return dfa_p, closer_p


# invent to wheel for arrays quadratic difference (c)
def do_sq_diff_arrays(x, y):
    a = [x]
    b = [y]
    c = [list(map(lambda a, b: (a - b)**2, a[i], b[i])) for i in range(len(a))]
    return c[0]


# binary logarithmic step for dfa algorithm
def optimal_step(n):
    return math.floor(math.log2(n))


# invent to wheel for many graphics in one pic
def do_plot(*args):
    for i in args:
        plt.plot(i)
    plt.show()
