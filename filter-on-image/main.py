import numpy
from numpy import copy

import utils
from utils import *
import numpy as np


def grayScaledFilter(img):
    mat = numpy.array([[0.3, 0.59, 0.11], [0.3, 0.59, 0.11], [0.3, 0.59, 0.11]])
    return utils.Filter(img, mat)


def customFilter(img):
    mat = numpy.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    return utils.Filter(img, mat)
    # return utils.Filter(utils.Filter(img, mat), numpy.linalg.inv(mat))


def scaleImg(img: numpy.ndarray, scale_width, scale_height):
    old_height = img.shape[1]
    old_with = img.shape[0]
    co_h = old_height / scale_height
    co_w = old_with / scale_width
    new_img = np.zeros((scale_width, scale_height, 3))
    i = 0
    while i < scale_width:
        j = 0
        while j < scale_height:
            new_img[i, j] = img[int(i * co_w), int(j * co_h)]
            j += 1
        i += 1
    return new_img


def crop_img(img: numpy.ndarray, start_row, end_row, start_column, end_column):
    return copy(img[start_column:end_column, start_row:end_row])


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400
    showImage(image_matrix, "Input Image", True)

    # grayScalePic = grayScaledFilter(image_matrix)
    # showImage(grayScalePic, "Gray Scaled")
    # # #
    #
    # # #
    # croppedImage = crop_img(image_matrix, 0, 700, 0, 1200)
    # showImage(croppedImage, "Cropped Image")
    # # #
    # scaledImage = scaleImg(image_matrix, 600, 1400)
    # showImage(scaledImage, "Scaled Image")

    showImage(customFilter(image_matrix), "custom")
