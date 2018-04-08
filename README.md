

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

1.1.<b> Data Preprocessing Input/Output Code-UMD.py:</b>
<br>In the next step, we need to write a code that would read the annotations from the .csv file , crop out the faces to create the 
positive dataset and crop out the background to create the negative dataset.The code should be self sufficient and modular so that when parameters like <b>"dataset path", "# of train images", "# of test images", "color/gray"</b>, the code should perform all the tasks and divide the dataset into a folder structure as below:</br>
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
<br>3.3 The hyperparameters used are as follows:</br>
<br><b> LEARNING RATE =1e-4 </b></br>
<br><b> STEPS PER EPOCH =100 </b></br>
<br><b> EPOCHS =30 </b></br>
<br><b> VALIDATION STEPS =50 </b></br>

4.<b> HYPER PARAMETER OPTIMIZATION:</b>
<br>The tune the hyperparameters, we run a random search over the hyperparameter space, by sampling the Learning Rate & Regularization   from a uniform distribution.</br>
<br>The optimal set of hyperparameters after running a coarse search and fine search are as follows:<br>
<br><b> COARSE SEARCH: <b><br>
<br><b> Maximum Testing Accuracy=96.89% </b></br>
<br><b> Minimum Testing Loss=0.094 </b></br>
<br><b> Value of optimum Learning Rate=4.48e-4 </b></br>
<br><b> Value of optimum Regularization=2.27e-5 </b></br>


<br><b> FINE SEARCH: <b><br>
<br><b> Maximum Testing Accuracy=97.79% </b></br>
<br><b> Minimum Testing Loss=0.1034 </b></br>
<br><b> Value of optimum Learning Rate=8.29e-4 </b></br>
<br><b> Value of optimum Regularization=3.91e-3 </b></br>

<br>The plots of TRAINING VS TESTING ACCURACY and TRAINING VS TESTING LOSS: </br>
<br>![TRAINING VS TESTING LOSS](https://github.com/kalyanghosh/Face-Detection-using-CNN/blob/master/1_reg_10minus6_lr_10minus4.png)</br>
<br>![TRAINING VS TESTING ACCURACY](https://github.com/kalyanghosh/Face-Detection-using-CNN/blob/master/2_reg_10minus6_lr_10power4.png)</br>
5.<b> SETUP INSTRUCTIONS:</b>
<br>The entire setup instructions to run the code can be found in <b>README.txt</b></br>
