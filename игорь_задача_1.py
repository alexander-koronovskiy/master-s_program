import matplotlib.pyplot
import numpy


# функция
def log_map(x, r):
    return r * x * (1 - x)


# карта значений функции
def do_map(
        itter_n=10000,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return x_array


# условие для создания последовательности
def map_to_bin(float_array):
    bin_array = [1 if i >= 0.5 else 0 for i in float_array]
    return bin_array


#функция блоков / интервалов
def find_p(bin_str, block_len):
    countdict = {}
    for i in numpy.arange(0, len(bin_str) - block_len, block_len):
        key = bin_str[i:(i + block_len)]
        try:
            countdict[key] += 1
        except:
            countdict[key] = 1
    return countdict


def do_H(countdict, str_len, block_len):
    probdict = {}
    probdict.fromkeys(countdict)
    for i in countdict.keys():
        probdict[i] = countdict[i] / str_len * block_len
    Hdict = {}
    for i in probdict.keys():
        Hdict[i] = probdict[i] * numpy.log2(probdict[i])
    H = -sum(Hdict.values())
    return H


if __name__ == '__main__':
    x_array = do_map()
    bin_array = map_to_bin(x_array)

    bin_str = "".join(str(i) for i in bin_array)
    #matplotlib.pyplot.plot([i for i in range(1, blockrange)], plot_array)
    print(bin_str)

    # варьируемый параметр
    block_len = 10
    countdict = find_p(bin_str, block_len)
    H = do_H(countdict, len(bin_str), block_len)


    def plot_H_n(blockrange):
        x_array = do_map()
        bin_array = map_to_bin(x_array)

        bin_str = "".join(str(i) for i in bin_array)

        plot_array = []
        for i in range(1, blockrange):
            countdict = find_p(bin_str, i)
            H = do_H(countdict, len(bin_str), i)
            plot_array.append(H)
            print(countdict, "H", H)

        # эта строчка отвечает за график
        matplotlib.pyplot.plot([i for i in range(1, blockrange)], plot_array)
        matplotlib.pyplot.grid()
        matplotlib.pyplot.show()


    plot_H_n(block_len)
