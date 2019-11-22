from tkinter import filedialog as fd
from pylab import figure, plot, xlabel, grid, legend, title, savefig
from matplotlib.font_manager import FontProperties
from numpy import loadtxt


def list_to_graph(array, pic_title='default'):
    figure(1, figsize=(10, 8))
    xlabel('t')
    grid(True)
    lw = 1
    plot(array, 'b', linewidth=lw)
    legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
    title(pic_title)
    # png_file = sample path
    png_file = fd.asksaveasfilename(filetypes=(("Image files", "*.png *.jpeg"), ("All files", "*.*")))
    savefig(png_file, dpi=100)


def write_to_file(array, filename):
    f = open(filename, 'w')
    for index in array:
        f.write(str(index) + '\n')
    f.close()


def write_to_list(f):
    data_list = list()
    with open(f, "r") as file:
        for line in file:  # file.readlines()
            data_list = data_list + list(map(float, line.split()))
    return(data_list)


def file_to_list():
    file_name = fd.askopenfilename()
    s = write_to_list(file_name)
    return s


def write_to_map(f):
    dataList = list()
    with open(f, "r") as file:
        for line in file:  # file.readlines()
            dataList.append(list(map(float, line.split())))
    return(dataList)
