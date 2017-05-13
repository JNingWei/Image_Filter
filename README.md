




# Image Filter
 
__Update 13-05-2017__:  __Currently, only yolo v1 (http://pjreddie.com/darknet/yolov1/) is supported. Yolo V2 (http://pjreddie.com/darknet/yolo/) is not supported. Batch norm layer is supported.__

## Introduction

It's an image filter writed by myself.
There are 11 filters to choose:
1. Naive_Filter
2. Sharpness_Center_Filter
3. Sharpness_Edge_Filter
4. Edge_Detection_360_degree_Filter
5. Edge_Detection_45_degree_Filter
6. Embossing_45_degree_Filter
7. Embossing_Asymmetric_Filter
8. Averaging_Blur_Filter
9. Completed_Blur_Filter
10. Motion_Blur_Filter
11. Gaussian_Blur

Choose the one you need, and the filterred image will generated at folder **Image_Generated**


The filter is consisted of five parts:
* src: folder for the code files that implement the function
* Image_Origin: folder for pictures which be chosen to filtering
* Image_Generated: folder for pictures which be generated after filtering
* README.md: introduce of this program
* requirements.txt: environment required for this program

## Usage 

* run "cd src/" to find code files 
* run "run.sh" to generated the image you need

## Requirements

   * Python2.7

   * Opencv2
