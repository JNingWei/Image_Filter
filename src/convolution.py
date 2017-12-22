# coding=utf-8

"""
Image-Filter
Convolution module.

__author__ = 'JNingWei'
"""

import numpy as np

def conv(image, filter, image_center_x, image_center_y):
    size = 3
    radius = int((size-1)/2)
    view = np.zeros((size, size, 3), dtype=np.float)
    for i in range(size):
        for j in range(size):
            for z in range(3):
                view[i][j][z] = image[image_center_x-radius+i][image_center_y-radius+j][z] * filter[i][j][z]
    return np.sum(view)
