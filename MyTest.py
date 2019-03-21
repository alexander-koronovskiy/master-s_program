import matplotlib.pyplot
import ExtendedFunc
import LogMap
import WorkWFiles


def do_mean_value(array):
    n = len(array)
    return sum(array) / n


def do_profile(array):
    p_array = []
    sr = do_mean_value(array)
    for i in range(len(array)):
        y_array = []
        for j in range(i):
            y_array.append(array[j] - sr)
        p_array.append(sum(y_array))
    return p_array


if __name__ == '__main__':
    data = WorkWFiles.write_to_list('RR.txt')
    data_lg = LogMap.do_map()

    profile_data = do_profile(data)
    profile_data_lg = do_profile(data_lg)

    # ExtendedFunc.step_interpolation(profile_data, 1024)
    ExtendedFunc.do_dfa(profile_data, 1024)
