# Image Filter　![Travis](https://img.shields.io/travis/rust-lang/rust.svg) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![AD](https://img.shields.io/badge/东半球最好的-图像滤波器-pink.svg)
 
__Update 13-05-2017__:   __It's an image filter written by myself.__

MIT license. Contributions welcome.

## Introduction


There are 11 filters to choose:

- [x] 1. Naive_Filter
- [x] 2. Sharpness_Center_Filter
- [x] 3. Sharpness_Edge_Filter
- [x] 4. Edge_Detection_360_degree_Filter
- [x] 5. Edge_Detection_45_degree_Filter
- [x] 6. Embossing_45_degree_Filter
- [x] 7. Embossing_Asymmetric_Filter
- [x] 8. Averaging_Blur_Filter
- [x] 9. Completed_Blur_Filter
- [x] 10. Motion_Blur_Filter
- [x] 11. Gaussian_Blur_Filter

Choose the one you need, and the filterred image will generated at folder *Image_Generated*.


	Labeling_Tool        root directory
	     |
	     |
	     +-- src              the code files that implement the function
	     |
	     |
	     +-- Image_Origin     images which be chosen to filtering
	     |
	     |
	     +-- Image_Generated  images which be generated after filtering
	     |
	     |
	     +-- README.md        introduce of program
	     |
	     |
	     +-- README.md        license of program
	     |
	     |
	     +-- requirements.txt   environment required for this program
      

## Usage 

1. Use ```cd src/``` to find code files 
2. Run ```run.sh``` to generated the image you need

## Requirements

   * Python2.7

   * Opencv2

## Demo


Naive_Image:

![Naive](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Naive.jpg)

<br>

Averaging_Blur:

![Averaging_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Averaging_Blur.jpg)

<br>

Averaging_Blur_Enhanced:

![Averaging_Blur_Enhanced](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Averaging_Blur_Enhanced.jpg)

<br>

Completed_Blur:

![Completed_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Completed_Blur.jpg)

<br>

Edge_Detection_360_degree:

![Edge_Detection_360_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Edge_Detection_360_degree.jpg)

<br>

Edge_Detection_45_degree:

![Edge_Detection_45_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Edge_Detection_45_degree.jpg)

<br>

Embossing_45_degree:

![Embossing_45_degree](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Embossing_45_degree.jpg)

<br>

Embossing_Asymmetric:

![Embossing_Asymmetric](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Embossing_Asymmetric.jpg)

<br>

Gaussian_Blur:

![Gaussian_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Gaussian_Blur.jpg)

<br>

Motion_Blur:

![Motion_Blur](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Motion_Blur.jpg)

<br>

Sharpness_Center:

![Sharpness_Center](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Sharpness_Center.jpg)

<br>

Sharpness_Edge:

![Sharpness_Edge](https://github.com/JNingWei/Image-Filter/blob/master/Image_Generated/Sharpness_Edge.jpg)

## License

[MIT](https://github.com/JNingWei/Image-Filter/blob/master/LICENSE.md)
