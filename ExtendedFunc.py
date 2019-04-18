import matplotlib.pyplot as plt
import math
import ApproximationFunc


# log(n) complicity dfa algorithm building
def do_dfa(array):
    # выбор оптимального шага алгоритма:
    # логарифмический - iter_log или линейный - iter
    iter_log = optimal_step(len(array)) // 2 + 1
    dfa_p = []
    for i in range(iter_log):
        fits = ApproximationFunc.do_approximation(array, pow(2, i))
        point = pow(sum(do_sq_diff_arrays(array, fits))/len(array), 0.5)
        dfa_p.append(point)
        # visualization of approximation
        do_plot(fits, array)
    dfa_p.reverse()
    plt.plot(dfa_p); plt.xlabel("$log_2 n$"); plt.ylabel("$log_2 F(n)$"); plt.show()

    # scaling rate coefficient printing
    dfa_x = ApproximationFunc.do_x_data(0, iter_log)
    ApproximationFunc.print_coefficient(dfa_x, dfa_p)


# give a square different result between real values in two one-dimensional arrays
def do_sq_diff_arrays(x, y):
    a = [x]
    b = [y]
    c = [list(map(lambda a, b: (a - b)**2, a[i], b[i])) for i in range(len(a))]
    return c[0]


# optimal binary logarithmic step for dfa algorithm
def optimal_step(n):
    return math.floor(math.log2(n))


# base plotting method
def do_plot(*args):
    for i in args:
        plt.plot(i)
    plt.show()
