import matplotlib.pyplot
import ExtendedFunc

ITER = 2048


def log_map(x, r):
    return r * x * (1 - x)


def do_map(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return x_array


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


if __name__ == '__main__':
    data = do_profile()
    ExtendedFunc.step_interpolation(data, ITER, 2)
