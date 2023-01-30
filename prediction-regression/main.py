import numpy
import pandas as pnd
from matplotlib import pyplot


def predict(x: float, a: float, b: float):
    return x * a + b


def print_info(x: float, y: float, yp: float):
    print('read value: ' + str(x))
    print('estimated value: ' + str(yp))
    print('error: ' + str(y - yp))
    print('---------------------------')


def draw_regression(v: numpy.ndarray, data_array: numpy.ndarray):
    x = numpy.linspace(0, 100, 1000)
    pyplot.plot(x, v[1] * x + v[0])
    i = 0
    while i < 100:
        pyplot.scatter(data_array[i][0], data_array[i][1])
        i += 1
    pyplot.show()


if __name__ == '__main__':
    data = pnd.read_csv('data.csv')
    data_array = numpy.array(data)
    array_x = []
    array_y = []
    i = 0
    while i < 95:
        array_x.append(list([1, data_array[i][0]]))
        array_y.append(list([data_array[i][1]]))
        i += 1
    x_matrix = numpy.array(array_x)
    y_matrix = numpy.array(array_y)
    x_t = x_matrix.transpose()
    v = numpy.matmul(numpy.linalg.inv(numpy.matmul(x_t, x_matrix)), numpy.matmul(x_t, y_matrix))
    i = 95
    while i < 100:
        print_info(data_array[i][0], data_array[i][1], predict(data_array[i][0], v[1], v[0]))
        i += 1
    draw_regression(v, data_array)
