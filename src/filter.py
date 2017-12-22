# coding=utf-8

"""
Image-Filter
Provide optional filter.
__author__ = 'JNingWei'
"""

import numpy as np

def Naive_Filter():
    # 原图　Naive Filter

    filter_0 = np.array([[[0,0,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[1,0,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,0,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,1,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,0,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,0,1],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,0,0]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Sharpness_Center_Filter():
    # 中心锐化 Sharpness_Center Filter

    filter_0 = np.array([[[-1,0,0],[-1,0,0],[-1,0,0]],
                         [[-1,0,0],[9,0,0],[-1,0,0]],
                         [[-1,0,0],[-1,0,0],[-1,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,-1,0],[0,-1,0],[0,-1,0]],
                         [[0,-1,0],[0,9,0],[0,-1,0]],
                         [[0,-1,0],[0,-1,0],[0,-1,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,-1],[0,0,-1],[0,0,-1]],
                         [[0,0,-1],[0,0,9],[0,0,-1]],
                         [[0,0,-1],[0,0,-1],[0,0,-1]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Sharpness_Edge_Filter():
    # 边缘锐化滤波器 Sharpness_Edge Filter

    filter_0 = np.array([[[1,0,0],[1,0,0],[1,0,0]],
                         [[1,0,0],[-7,0,0],[1,0,0]],
                         [[1,0,0],[1,0,0],[1,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,1,0],[0,1,0],[0,1,0]],
                         [[0,1,0],[0,-7,0],[0,1,0]],
                         [[0,1,0],[0,1,0],[0,1,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,1],[0,0,1],[0,0,1]],
                         [[0,0,1],[0,0,-7],[0,0,1]],
                         [[0,0,1],[0,0,1],[0,0,1]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Edge_Detection_360_degree_Filter():
    # 360度边缘检测 Edge_Detection_360_degree Filter

    filter_0 = np.array([[[-1,0,0],[-1,0,0],[-1,0,0]],
                         [[-1,0,0],[8,0,0],[-1,0,0]],
                         [[-1,0,0],[-1,0,0],[-1,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,-1,0],[0,-1,0],[0,-1,0]],
                         [[0,-1,0],[0,8,0],[0,-1,0]],
                         [[0,-1,0],[0,-1,0],[0,-1,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,-1],[0,0,-1],[0,0,-1]],
                         [[0,0,-1],[0,0,8],[0,0,-1]],
                         [[0,0,-1],[0,0,-1],[0,0,-1]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Edge_Detection_45_degree_Filter():
    # ４５度边缘检测 Edge_Detection_45_degree Filter

    filter_0 = np.array([[[-1,0,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[2,0,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[-1,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,-1,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,2,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,-1,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,-1],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,0,2],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,0,-1]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Embossing_45_degree_Filter():
    # ４５度浮雕 Embossing_45_degree Filter

    filter_0 = np.array([[[-1,0,0],[-1,0,0],[0,0,0]],
                         [[-1,0,0],[1,0,0],[1,0,0]],
                         [[0,0,0],[1,0,0],[1,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,-1,0],[0,-1,0],[0,0,0]],
                         [[0,-1,0],[0,1,0],[0,1,0]],
                         [[0,0,0],[0,1,0],[0,1,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,-1],[0,0,-1],[0,0,0]],
                         [[0,0,-1],[0,0,1],[0,0,1]],
                         [[0,0,0],[0,0,1],[0,0,1]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Embossing_Asymmetric_Filter():
    # 非对称浮雕 Embossing_Asymmetric Filter

    filter_0 = np.array([[[2,0,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[-1,0,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[-1,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,2,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,-1,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,-1,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,2],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,0,-1],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,0,-1]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Averaging_Blur_Filter():
    # 均值模糊 Averaging_Blur Filter

    filter_0 = np.array([[[0,0,0],[0.25,0,0],[0,0,0]],
                         [[0.25,0,0],[0,0,0],[0.25,0,0]],
                         [[0,0,0],[0.25,0,0],[0,0,0]]],
                        dtype=np.float)

    filter_1 = np.array([[[0,0,0],[0,0.25,0],[0,0,0]],
                         [[0,0.25,0],[0,0,0],[0,0.25,0]],
                         [[0,0,0],[0,0.25,0],[0,0,0]]],
                        dtype=np.float)

    filter_2 = np.array([[[0,0,0],[0,0,0.25],[0,0,0]],
                         [[0,0,0.25],[0,0,0],[0,0,0.25]],
                         [[0,0,0],[0,0,0.25],[0,0,0]]],
                        dtype=np.float)
    return filter_0, filter_1, filter_2

def Completed_Blur_Filter():
    # Completed_均值模糊 Completed_Blur Filter

    filter_0 = np.array([[[1.0/9,0,0],[1.0/9,0,0],[1.0/9,0,0]],
                         [[1.0/9,0,0],[1.0/9,0,0],[1.0/9,0,0]],
                         [[1.0/9,0,0],[1.0/9,0,0],[1.0/9,0,0]]],
                        dtype=np.float)

    filter_1 = np.array([[[0,1.0/9,0],[0,1.0/9,0],[0,1.0/9,0]],
                         [[0,1.0/9,0],[0,1.0/9,0],[0,1.0/9,0]],
                         [[0,1.0/9,0],[0,1.0/9,0],[0,1.0/9,0]]],
                        dtype=np.float)

    filter_2 = np.array([[[0,0,1.0/9],[0,0,1.0/9],[0,0,1.0/9]],
                         [[0,0,1.0/9],[0,0,1.0/9],[0,0,1.0/9]],
                         [[0,0,1.0/9],[0,0,1.0/9],[0,0,1.0/9]]],
                        dtype=np.float)
    return filter_0, filter_1, filter_2

def Motion_Blur_Filter():
    # Motion_Blur Filter

    filter_0 = np.array([[[1,0,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[1,0,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[1,0,0]]],
                        dtype=np.int16)

    filter_1 = np.array([[[0,1,0],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,1,0],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,1,0]]],
                        dtype=np.int16)

    filter_2 = np.array([[[0,0,1],[0,0,0],[0,0,0]],
                         [[0,0,0],[0,0,1],[0,0,0]],
                         [[0,0,0],[0,0,0],[0,0,1]]],
                        dtype=np.int16)
    return filter_0, filter_1, filter_2

def Gaussian_Blur_Filter():
    # 高斯模糊 Gaussian_Blur Filter

    filter_0 = np.array([[[1.0/36,0,0],[4.0/36,0,0],[1.0/36,0,0]],
                         [[4.0/36,0,0],[16.0/36,0,0],[4.0/36,0,0]],
                         [[1.0/36,0,0],[4.0/36,0,0],[1.0/36,0,0]]],
                        dtype=np.float)

    filter_1 = np.array([[[0,1.0/36,0],[0,4.0/36,0],[0,1.0/36,0]],
                         [[0,4.0/36,0],[0,16.0/36,0],[0,4.0/36,0]],
                         [[0,1.0/36,0],[0,4.0/36,0],[0,1.0/36,0]]],
                        dtype=np.float)

    filter_2 = np.array([[[0,0,1.0/36],[0,0,4.0/36],[0,0,1.0/36]],
                         [[0,0,4.0/36],[0,0,16.0/36],[0,0,4.0/36]],
                         [[0,0,1.0/36],[0,0,4.0/36],[0,0,1.0/36]]],
                        dtype=np.float)
    return filter_0, filter_1, filter_2

def None_Exist_Filter():
    # None_Exist Filter

    filter_0 = np.zeros((3,3,3), dtype=np.float)

    filter_1 = np.zeros((3,3,3), dtype=np.float)

    filter_2 = np.zeros((3,3,3), dtype=np.float)

    return filter_0, filter_1, filter_2

def Filter(filter_name):
    # Choose which group of filters to be returned

    if filter_name == 'Naive':
        filter_0, filter_1, filter_2 = Naive_Filter()
    elif filter_name == 'Sharpness_Center':
        filter_0, filter_1, filter_2 = Sharpness_Center_Filter()
    elif filter_name == 'Sharpness_Edge':
        filter_0, filter_1, filter_2 = Sharpness_Edge_Filter()
    elif filter_name == 'Edge_Detection_360_degree':
        filter_0, filter_1, filter_2 = Edge_Detection_360_degree_Filter()
    elif filter_name == 'Edge_Detection_45_degree':
        filter_0, filter_1, filter_2 = Edge_Detection_45_degree_Filter()
    elif filter_name == 'Embossing_45_degree':
        filter_0, filter_1, filter_2 = Embossing_45_degree_Filter()
    elif filter_name == 'Embossing_Asymmetric':
        filter_0, filter_1, filter_2 = Embossing_Asymmetric_Filter()
    elif filter_name == 'Averaging_Blur':
        filter_0, filter_1, filter_2 = Averaging_Blur_Filter()
    elif filter_name == 'Completed_Blur':
        filter_0, filter_1, filter_2 = Completed_Blur_Filter()
    elif filter_name == 'Motion_Blur':
        filter_0, filter_1, filter_2 = Motion_Blur_Filter()
    elif filter_name == 'Gaussian_Blur':
        filter_0, filter_1, filter_2 = Gaussian_Blur_Filter()
    else:
        filter_0, filter_1, filter_2 = None_Exist_Filter()
        print '\nNo such Filter !\n'

    return filter_0, filter_1, filter_2

