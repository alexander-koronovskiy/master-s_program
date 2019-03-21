# linear approximation
def best_fit(X, Y):
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X)
    numer = sum([xi*yi for xi, yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2
    b = numer / denum
    a = ybar - b * xbar
    # print('fit line: y = {:.2f} + {:.2f}x'.format(a, b))
    vfit = [a + b * xi for xi in X]
    return vfit


# linear approximation of the array divided into j parts
def do_approximation(array, n, j):
    i = 0
    fit_array = []
    while(i < n):
        x = do_x_data(i, i + n//j)
        y = array[i::]
        fit_array = fit_array + best_fit(x, y)
        i = i + n // j
    return fit_array


def do_x_data(n0, n):
    x_data = []
    for i in range(n0, n):
        x_data.append(i)
    return x_data
