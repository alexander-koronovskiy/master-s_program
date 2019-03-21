import matplotlib.pyplot
import ApproximationFunc


# построение dfa-метода сложностью log(n)
def do_dfa(array, n, steps):
    z_array = []
    for i in range(2, 10):
        interp = ApproximationFunc.do_approximation(array, n, steps**i)
        z_array.append(
            (sum(ApproximationFunc.do_sq_diff_arrays(array, interp)) / n)**(1/2)
        )
    matplotlib.pyplot.semilogy(z_array)
    matplotlib.pyplot.title('Dependence between $lg$n and $lg F_{dna}$')
    matplotlib.pyplot.show()


def step_interpolation(array, n, steps):
    for i in range(10):
        interp = ApproximationFunc.do_approximation(array, n, steps**i)
        matplotlib.pyplot.plot(interp)
        matplotlib.pyplot.plot(array)
        # интервалы значений по осям X и Y
        matplotlib.pyplot.axis([0, 2000, -10.0, 10.0])
        matplotlib.pyplot.title('Profile - orange, approximation - blue')
        matplotlib.pyplot.show()
