# coding=utf-8

"""
Image-Filter
Main program.

__author__ = 'JNingWei'
"""

import os
import cv2
import numpy as np

import filter
import convolution

def main():

    original_images = ['girl.jpg']
    filter_names = ['Naive', 'Sharpness_Center', 'Sharpness_Edge', 'Edge_Detection_360_degree',
                    'Edge_Detection_45_degree', 'Embossing_45_degree', 'Embossing_Asymmetric',
                    'Averaging_Blur', 'Completed_Blur', 'Motion_Blur', 'Gaussian_Blur']

    # Choose the filter from list: "filter_names"
    filter_name = 'Sharpness_Center'

    for original_image in original_images:
        original_image_path = os.path.join(os.getcwd()[:-3], 'Image_Origin/', original_image)
        img =cv2.imread(original_image_path, 3)

        filter_0, filter_1, filter_2 = filter.Filter(filter_name)

        img2 = np.zeros((424, 600, 3), dtype=np.float)

        for i in range(1, 423, 1):
            for j in range(1, 599, 1):

                img2[i][j][0] = convolution.conv(img, filter_0, i, j)
                img2[i][j][1] = convolution.conv(img, filter_1, i, j)
                img2[i][j][2] = convolution.conv(img, filter_2, i, j)

        generated_image = filter_name + '.jpg'

        generated_image_path = os.path.join(os.getcwd()[:-3], 'Image_Generated/', generated_image)
        cv2.imwrite(generated_image_path,img2)
        img_show = cv2.imread(generated_image_path)

        cv2.imshow(generated_image, img_show)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
