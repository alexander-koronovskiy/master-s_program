import numpy as np
import matplotlib.pyplot as plt
import ApproximationFunc
import scipy
import ExtendedFunc
import accessory.WorkWFiles as WorkWFiles


def do_profile(array):
    p_array = []
    sr = np.mean(array)
    for i in range(len(array)):
        y_array = []
        for j in range(i):
            y_array.append(array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


# base plotting method
def do_plot(*args):
    for i in args:
        plt.plot(i)
    plt.show()


def dfa_plot(q):
    y = WorkWFiles.write_to_list('solutions/white_noise.txt'); print(len(y))
    z = do_profile(y)
    t = ExtendedFunc.do_dfa(z, q)
    do_plot(t[0], t[1])
    WorkWFiles.write_to_file(t[1], 'dfa_q/' + str(q) + '.txt')


def q_a():
    q_arr = [-20, -15, -10, -5, -3, -2, -1, 1, 2, 3, 5, 10, 15, 20]
    a_array = []
    b_array = []
    for i in q_arr:
        dfa_plot(i)
        q_a = WorkWFiles.write_to_list('dfa_q/' + str(i) + '.txt')
        t = [0, 1, 2, 3, 4, 5, 6, 7]
        alpha = ApproximationFunc.print_coefficient(t, q_a)
        a_array.append(alpha)
        b_array.append(q_a)
    plt.plot(q_arr, a_array);
    plt.xlabel("q")
    plt.ylabel("alfa")
    plt.show()
    do_plot(b_array[0], b_array[1], b_array[2], b_array[3], b_array[4], b_array[5],
            b_array[6], b_array[7], b_array[8], b_array[9])


def w_noise_gen():
    mean = 0
    std = 1
    num_samples = 2000
    return np.random.normal(mean, std, size=num_samples)


if __name__ == '__main__':
    dfa_plot(20)
