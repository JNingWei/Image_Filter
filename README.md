# Image Filter　![Travis](https://img.shields.io/travis/rust-lang/rust/master.svg) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![AD](https://img.shields.io/badge/东半球最好的-图像滤波器-pink.svg)
 
__Update 13-05-2017__:   __It's an image filter entirely written by myself.__

MIT license. Contributions welcome.

## Overview

	Image-Filter/       root directory
	     |
	     +-- src/               code files that implement the function
	     |
	     +-- Image_Origin/      images which be chosen to filtering
	     |
	     +-- Image_Generated/   images which be generated after filtering
	     |
	     +-- README.md          manual of project
	     |
	     +-- LICENSE.md         license of project
	     |
	     +-- requirements.txt   environment required for this program

There are 11 filters can choose:

- [x] 1. Naive Filter  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;原图滤波（相当于无变化）
- [x] 2. Sharpness_Center Filter  &emsp;&emsp;&emsp;&emsp; 中心锐化 滤波
- [x] 3. Sharpness_Edge Filter &emsp;&emsp;&emsp;&emsp;&emsp;边缘锐化 滤波
- [x] 4. Edge_Detection_360° Filter  &emsp;&emsp;&emsp;360°边缘检测 滤波
- [x] 5. Edge_Detection_45° Filter  &emsp;&emsp;&emsp;&ensp;45°边缘检测 滤波
- [x] 6. Embossing_45° Filter&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;45°浮雕 滤波
- [x] 7. Embossing_Asymmetric Filter&emsp;&emsp; 非对称浮雕 滤波
- [x] 8. Averaging_Blur Filter  &ensp;&emsp;&emsp;&emsp;&emsp;&emsp;  均值模糊 滤波
- [x] 9. Completed_Blur Filter &emsp;&emsp;&emsp;&emsp;&emsp;&ensp;完全模糊 滤波
- [x] 10. Motion_Blur Filter &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 运动模糊 滤波
- [x] 11. Gaussian_Blur Filter  &emsp;&emsp;&emsp;&emsp;&emsp;&ensp;高斯模糊 滤波

Choose the filter you need, and the filtered image will generated at folder ```Image_Generated/```.<br>
选择你需要的滤波器，卷积结果会自动保存在 ```Image_Generated/``` 文件夹。

## Usage 

1. Run ```python src/main.py``` to generated the image you need. Need to wait patiently for a while to get results.
2. In ```src/main.py```, you can also design a filter yourself to experiment.
<br>

1. 运行 ```python src / main.py``` 来生成你需要的图像，卷积结果需要耐心等待一会儿。
2. 在 ```src/main.py``` 中，自己还可以设计一个滤波器来做实验以加深对滤波器的了解。

## Requirements

   * Python

   * OpenCV

## Demo



1. Naive Filter  &emsp;&emsp; 原图滤波（相当于无变化）<br>
![Naive](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Naive.jpg)


2. Sharpness_Center Filter  &emsp;&emsp; 中心锐化 滤波<br>
![Sharpness_Center](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Sharpness_Center.jpg)

3. Sharpness_Edge Filter  &emsp;&emsp; 边缘锐化 滤波<br>
![Sharpness_Edge](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Sharpness_Edge.jpg)

4. Edge_Detection_360° Filter  &emsp;&emsp; 360°边缘检测 滤波<br>
![Edge_Detection_360_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Edge_Detection_360_degree.jpg)

5. Edge_Detection_45° Filter  &emsp;&emsp; 45°边缘检测 滤波<br>
![Edge_Detection_45_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Edge_Detection_45_degree.jpg)

6. Embossing_45° Filter  &emsp;&emsp; 45°浮雕 滤波<br>
![Embossing_45_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Embossing_45_degree.jpg)

7. Embossing_Asymmetric Filter  &emsp;&emsp; 非对称浮雕 滤波<br>
![Embossing_Asymmetric](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Embossing_Asymmetric.jpg)

8. Averaging_Blur Filter  &emsp;&emsp; 均值模糊 滤波<br>
![Averaging_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Averaging_Blur.jpg)

9. Completed_Blur Filter  &emsp;&emsp; 完全模糊 滤波<br>
![Completed_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Completed_Blur.jpg)

10. Motion_Blur Filter  &emsp;&emsp; 运动模糊 滤波<br>
![Motion_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Motion_Blur.jpg)

11. Gaussian_Blur Filter  &emsp;&emsp; 高斯模糊 滤波<br>
![Gaussian_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Gaussian_Blur.jpg)

## License

[MIT](https://github.com/JNingWei/Image_Filter/blob/master/LICENSE.md)
