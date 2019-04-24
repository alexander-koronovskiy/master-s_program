import numpy as np
import matplotlib.pyplot as plt
import ExtendedFunc
import accessory.AKF as AKF
import accessory.Runge as runge
from scipy import signal
import scipy
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
    plt.xlim(0, 100)
    plt.show()


def dfa_plot():
    y = WorkWFiles.write_to_list('solutions/RR.txt')
    z = do_profile(y)
    q = - 20; t = ExtendedFunc.do_dfa(z, q)
    do_plot(t[0], t[1])
    # WorkWFiles.write_to_file(t[1], 'dfa_q/' + str(q) + '.txt')


def xx(x): return x[0] * np.exp(complex(0, 1)*np.arctan(x[0]))


if __name__ == '__main__':
    # stationary quadrant signal
    t = np.linspace(0, 1, 500, endpoint=False)
    x = signal.square(2 * np.pi * 5 * t)

    # data
    y = WorkWFiles.write_to_list('solutions/u.txt'); y_np = np.array(y)

    # AKF and it's plot
    y_ak = AKF.autocorr5(y_np, range(100))

    # Fourier
    yf = scipy.fftpack.fft(y); yf = abs(np.array(yf)) / (2 * np.pi * 100)

    # integrate AKF
    X = []
    for i in range(len(y_ak)):
        x = runge.rKN([y_ak[i]], [xx], 1, 1)
        X = X + x

    # integrate Fourier
    Y = []
    for i in range(len(yf)):
        x = runge.rKN([yf[i]], [xx], 1, 1)
        Y = Y + x

    # y_ak, X, yf, Y
    do_plot(X, yf)
