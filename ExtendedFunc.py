import matplotlib.pyplot
import ApproximationFunc
import math


# построение dfa-метода сложностью log(n)
def do_dfa(array, n, step=2):
    z_array = []
    for i in range(1, optimal_step(n)):
        interp = ApproximationFunc.do_approximation(array, n, step**i)
        z_array.append(
            (sum(do_sq_diff_arrays(array, interp)) / n)**(1/2)
        )
    matplotlib.pyplot.semilogy(z_array)
    matplotlib.pyplot.title('Dependence between $lg$n and $lg F_{dna}$')
    matplotlib.pyplot.show()


def step_interpolation(array, n, step=2):
    for i in range(optimal_step(n)):
        interp = ApproximationFunc.do_approximation(array, n, step**i)
        matplotlib.pyplot.plot(interp)
        matplotlib.pyplot.plot(array)
        # интервалы значений по осям X и Y
        matplotlib.pyplot.axis([0, 1000, -10.0, 10.0])
        matplotlib.pyplot.title('Profile - orange, approximation - blue')
        matplotlib.pyplot.show()


# give a a square different result between real values in two one-dimensional arrays / lists
def do_sq_diff_arrays(x, y):
    a = [x]
    b = [y]
    c = [list(map(lambda a, b: (a - b)**2, a[i], b[i])) for i in range(len(a))]
    return c[0]


def optimal_step(n):
    return math.floor(math.log2(n))
