# coding=utf-8

"""
Image-Filter
Provide optional filter.

__author__ = 'JNingWei'
"""

import numpy as np

def Naive_Filter():
    # Naive Filter  原图 滤波
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
    # Sharpness_Center Filter  中心锐化 滤波
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
    # Sharpness_Edge Filter  边缘锐化 滤波
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
    # Edge_Detection_360° Filter  360°边缘检测 滤波
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
    # Edge_Detection_45° Filter  45°边缘检测 滤波
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
    # Embossing_45° Filter  45°浮雕 滤波
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
    # Embossing_Asymmetric Filter  非对称浮雕 滤波
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
    # Averaging_Blur Filter  均值模糊 滤波
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
    # Completed_Blur Filter  完全模糊 滤波
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
    # Motion_Blur Filter  运动模糊 滤波
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
    # Gaussian_Blur Filter  高斯模糊 滤波
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

def DIY_Filter():
    # Design a filter yourself  自己设计一个滤波器
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

def No_Exist_Filter():
    # When filter name doesn't exist  当滤波器不存在时
    filter_0 = np.zeros((3, 3, 3), dtype=np.float)
    filter_1 = np.zeros((3, 3, 3), dtype=np.float)
    filter_2 = np.zeros((3, 3, 3), dtype=np.float)
    return filter_0, filter_1, filter_2

def Filter(filter_name):
    # Choose which filter to be returned  根据用户指定的 滤波器名称，挑选对应的 滤波器配置 返回
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
    elif filter_name == 'DIY':
        filter_0, filter_1, filter_2 = DIY_Filter()
    else:
        print("\n No such Filter !")
        exit(0)
        filter_0, filter_1, filter_2 = No_Exist_Filter()

    return filter_0, filter_1, filter_2

