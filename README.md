# Image Filter　![Travis](https://img.shields.io/travis/rust-lang/rust/master.svg) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![AD](https://img.shields.io/badge/东半球最好的-图像滤波器-pink.svg)
 
__Update 13-05-2017__:   __It's an image filter written by myself.__

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

- [x] 1. Naive Filter  原图滤波（相当于无变化）
- [x] 2. Sharpness_Center Filter  中心锐化 滤波
- [x] 3. Sharpness_Edge Filter  边缘锐化 滤波
- [x] 4. Edge_Detection_360° Filter  360°边缘检测 滤波
- [x] 5. Edge_Detection_45° Filter  45°边缘检测 滤波
- [x] 6. Embossing_45° Filter  45°浮雕 滤波
- [x] 7. Embossing_Asymmetric Filter  非对称浮雕 滤波
- [x] 8. Averaging_Blur Filter  均值模糊 滤波
- [x] 9. Completed_Blur Filter  完全模糊 滤波
- [x] 10. Motion_Blur Filter  运动模糊 滤波
- [x] 11. Gaussian_Blur Filter  高斯模糊 滤波

Choose the one you need, and the filterred image will generated at folder *Image_Generated*.

## Usage 

1. Use ```cd src/``` to find code files.
2. Run ```run.sh``` to generated the image you need.

## Requirements

   * Python

   * OpenCV

## Demo



1. Naive Filter  原图滤波（相当于无变化）

![Naive](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Naive.jpg)

<br>

2. Sharpness_Center Filter  中心锐化 滤波

![Sharpness_Center](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Sharpness_Center.jpg)

<br>

3. Sharpness_Edge Filter  边缘锐化 滤波

![Sharpness_Edge](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Sharpness_Edge.jpg)

<br>

4. Edge_Detection_360° Filter  360°边缘检测 滤波

![Edge_Detection_360_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Edge_Detection_360_degree.jpg)


<br>

5. Edge_Detection_45° Filter  45°边缘检测 滤波

![Edge_Detection_45_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Edge_Detection_45_degree.jpg)

<br>

6. Embossing_45° Filter  45°浮雕 滤波

![Embossing_45_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Embossing_45_degree.jpg)

<br>

7. Embossing_Asymmetric Filter  非对称浮雕 滤波

![Embossing_Asymmetric](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Embossing_Asymmetric.jpg)

<br>

8. Averaging_Blur Filter  均值模糊 滤波
![Averaging_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Averaging_Blur.jpg)

![Averaging_Blur_Enhanced](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Averaging_Blur_Enhanced.jpg)

<br>

9. Completed_Blur Filter  完全模糊 滤波

![Completed_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Completed_Blur.jpg)

<br>

10. Motion_Blur Filter  运动模糊 滤波

![Motion_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Motion_Blur.jpg)

<br>

11. Gaussian_Blur Filter  高斯模糊 滤波<br>
![Gaussian_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Gaussian_Blur.jpg)

## License

[MIT](https://github.com/parnec/Image_Algorithm_Toolbox/blob/master/LICENSE.md)
