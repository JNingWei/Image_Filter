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

def main(src, dst):

    src_pic_paths = [os.path.join(src, name) for name in os.listdir(src)
                     if os.path.splitext(name)[-1] in [".jpg", ".JPG", ".png", ".PNG"]]
    filters = [
        'Naive',                     # Naive Filter  原图滤波（相当于无变化）
        'Sharpness_Center',          # Sharpness_Center Filter  中心锐化 滤波
        'Sharpness_Edge',            # Sharpness_Edge Filter  边缘锐化 滤波
        'Edge_Detection_360_degree', # Edge_Detection_360° Filter  360°边缘检测 滤波
        'Edge_Detection_45_degree',  # Edge_Detection_45° Filter  45°边缘检测 滤波
        'Embossing_45_degree',       # Embossing_45° Filter  45°浮雕 滤波
        'Embossing_Asymmetric',      # Embossing_Asymmetric Filter  非对称浮雕 滤波
        'Averaging_Blur',            # Averaging_Blur Filter  均值模糊 滤波
        'Completed_Blur',            # Completed_Blur Filter  完全模糊 滤波
        'Motion_Blur',               # Motion_Blur Filter  运动模糊 滤波
        'Gaussian_Blur',             # Gaussian_Blur Filter  高斯模糊 滤波
        
        'DIY'                        # DIY Filter  自定义 滤波
    ]

    # ===================================================================
    ## Choose the filter from list: "filter_names"  选择你需要的滤波器

    filter_name = 'Sharpness_Center'
    # filter_name = 'DIY'
    # ===================================================================

    for src_pic_path in src_pic_paths:
        img = cv2.imread(src_pic_path)
        h, w, c = img.shape
        assert c == 3, "Error! Please use the picture of 3 color channels."
        filter_0, filter_1, filter_2 = filter.Filter(filter_name)
        img2 = np.zeros((h, w, c), dtype=np.float)
        for i in range(1, h-1, 1):
            for j in range(1, w-1, 1):
                img2[i][j][0] = convolution.conv(img, filter_0, i, j)
                img2[i][j][1] = convolution.conv(img, filter_1, i, j)
                img2[i][j][2] = convolution.conv(img, filter_2, i, j)
        dst_pic_name = filter_name + '.jpg'
        dst_pic_path = os.path.join(dst, dst_pic_name)
        cv2.imwrite(dst_pic_path, img2)

        img3 = cv2.imread(dst_pic_path)
        cv2.imshow(dst_pic_name, img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    SRC = '../Image_Origin'       # dir for origin pics  原图像文件夹
    DST = '../Image_Generated'    # dir for filtered pics  滤波后生成图像存放的文件夹
    main(SRC, DST)
