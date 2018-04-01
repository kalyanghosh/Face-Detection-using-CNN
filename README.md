

# PROJECT TITLE: FACE DETECTION USING CNN aka ConvNets

## DESCRIPTION:
<br>This repository gives budding Deep Learning enthusiats a gentle introduction to the topic of Deep Learning.</br>
<br>In this repository , I will list down all the steps needed to get started with your first project in Deep Learning.</br>
<br>So go ahead, Fork this repo and get started with Deep Learning.</br>

## CONTENTS:
1. Dataset download
2. Tools & Libraries
3. Code
4. Instructions to run the code
5. Future improvements

## EXPLANATIONS & STEPS:
1. <b> Dataset download:</b>
<br>For this project we will be using the UMD face dataset which can be downloaded from: [UMD Dataset](http://www.umdfaces.io/) </br>
<br>![UMD Face Dataset](https://github.com/kalyanghosh/Face-Detection-using-CNN/blob/master/umd1.jpg)</br>
<br>Go ahead and download the <b>Batch 3 dataset</b>, which will have faces of personalities and and <b>.csv</b> file that contains the annotations
to crop out the face from each of the images:</br>
![Batch 3](https://github.com/kalyanghosh/Face-Detection-using-CNN/blob/master/umd2.jpg)</br>

1.1.<b> Data Preprocessing IO Code-UMD.py:</b>
<br>In the next step, we need to write a code that would read the annotations from the .csv file , crop out the faces to create the 
positive dataset and crop out the background to create the negative dataset.The code should be self sufficient and modular so that when parameters like "dataset path", "# of train images", "# of test images", "color/gray", the code should perform all the tasks and divide the dataset into a folder structure as below:</br>
<br>![Train/Test Folder Structure](https://github.com/kalyanghosh/Face-Detection-using-CNN/blob/master/folder.jpg)</br>

2.<b> Tools & Libraries:</b>
<br>2.1 In this project we will be using the <b>Keras Deep Learning Library</b> and we will be running it on top of the <b>Tensorflow</b> backend.
<br>![Keras & Tensorflow](https://github.com/kalyanghosh/Face-Detection-using-CNN/blob/master/keras-tensorflow-logo.jpg)</br>
<br>Instructions on how to install <b>Keras & Tensorflow</b> on an Ubuntu machine are available online.</br>
2.2 The code editors we will be using are <b>Anaconda</b> with <b>OpenCV,Numpy,Scipy</b> support. 

3.<b> Code-CNN_code.py:</b>
<br>The python file CNN_code is the main code which encapsulates the CNN architecture that was used for this project.</br>
<br>The steps performed by the code are as follows:<br>
<br>3.1: In this code, I have used a simplistic CNN architecture as below:</br>
<br><b>2D CONVOLUTION LAYER->2D MAX POOLING->2D CONVOLUTION LAYER->2D MAX POOLING->2D CONVOLUTION LAYER->2D MAX POOLING->2D CONVOLUTION LAYER->2D MAX POOLING->FULLY CONNECTED->FULLY CONNECTED</b></br>
<br>3.2: In this code, I have used <b>Binary CrossEntropy</b> as the <b>Loss Function</b> , the <b>RMSProp</b> as the <b>Gradient Descent</b> algorithm:</br>
<br><b>2D CONVOLUTION LAYER->2D MAX POOLING->2D CONVOLUTION LAYER->2D MAX POOLING->2D CONVOLUTION LAYER->2D MAX POOLING->2D CONVOLUTION LAYER->2D MAX POOLING->FULLY CONNECTED->FULLY CONNECTED</b></br>






