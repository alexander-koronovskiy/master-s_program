from math import ceil


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
def do_approximation(z, n):
    u = parting(z, n)
    x = []
    bf = []
    for i in range(n):
        x0 = do_x_data(0, len(u[i]))
        bf0 = best_fit(x0, u[i])
        x = x + x0
        bf = bf + bf0
    return bf


# split data list in quantity parts
def parting(xs, parts):
    part_len = ceil(len(xs)/parts)
    return [xs[part_len*k:part_len*(k+1)] for k in range(parts)]


# do x data for opportunity of approximation one-dimensional data lists
def do_x_data(n0, n):
    x_data = []
    for i in range(n0, n):
        x_data.append(i)
    return x_data
