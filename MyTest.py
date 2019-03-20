import matplotlib.pyplot


ITER = 1024


# функция
def log_map(x, r):
    return r * x * (1 - x)


def do_map(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return x_array


def do_map_w_average(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    sr = sum(do_map()) / ITER
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r) - sr)
    return x_array


# составление профиля функции - НЕ ТРОГАТЬ!!!! РАБОТАЕТ!!!
def do_profile(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    sr = sum(do_map()) / ITER
    p_array = []
    for i in range(itter_n):
        y_array = []
        for j in range(i):
            y_array.append(x_array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


# построение dfa-метода сложностью log(n)
def do_dfa(array, steps):
    z_array = []
    for i in range(2, 10):
        interp = do_interpolation(array, steps**i)
        z_array.append(
            (sum(do_sq_diff_arrays(array, interp)) / ITER)**(1/2)
        )
    matplotlib.pyplot.semilogy(z_array)
    matplotlib.pyplot.title('Dependence between $lg$n and $lg F_{dna}$')
    matplotlib.pyplot.show()


def step_interpolation(array, steps):
    for i in range(10):
        interp = do_interpolation(array, steps**i)
        matplotlib.pyplot.plot(interp)
        matplotlib.pyplot.plot(array)
        # интервалы значений по осям X и Y
        matplotlib.pyplot.axis([0, 2000, -5.0, 5.0])
        matplotlib.pyplot.title('Profile - orange, approximation - blue')
        matplotlib.pyplot.show()


def write_to_file(array, filename):
    f = open(filename, 'w')
    for index in array:
        f.write(str(index) + '\n')
    f.close()


def do_x_data(n0, n):
    x_data = []
    for i in range(n0, n):
        x_data.append(i)
    return x_data


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
def do_interpolation(array, j):
    i = 0
    fit_array = []
    while(i < ITER):
        x = do_x_data(i, i + ITER//j)
        y = array[i::]
        fit_array = fit_array + best_fit(x, y)
        i = i + ITER // j
    return fit_array


# give a a square different result between real values in two one-dimensional arrays / lists
def do_sq_diff_arrays(x, y):
    a = [x]
    b = [y]
    c = [list(map(lambda a, b: (a - b)**2, a[i], b[i])) for i in range(len(a))]
    return c[0]


def write_to_list(f):
    data_list = list()
    with open(f, "r") as file:
        for line in file:  # file.readlines()
            data_list = data_list + list(map(float, line.split()))
    return(data_list)


if __name__ == '__main__':
    data = write_to_list('RR.txt')
    print(data)
