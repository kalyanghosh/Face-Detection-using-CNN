# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:54:41 2018

@author: Kalyan
"""

###########################################################################################################
#Instructions to run the code UMD.py inside the dataset subfolder folder inside Project2 folder

#1. Download the data(Batch 3, 12GB version) from http://www.umdfaces.io/ 
#2. Create a folder named data_UMD inside the dataset folder.Inside the data_UMD folder,
#   create two dirs named Annotation and original_pics
#3. Extract the dataset inside the original_pics folder and copy the umdfaces_batch3_ultraface.csv annotation
#   file to the Annotation folder.
#4. Run the code UMD.py inside the dataset folder by specifying the following parameters.

#   INPUT PARAMETERS
#   image_dir = .\data_UMD\original_pics
#   anno_dir  = .\data_UMD\Annotation
#   save_dir  = .\data_UMD\cache
#   use_Color = True for color image , False for gray
#   patch_size = 60, you are free to give your own size
#   train_size =  10000, number of training images  
#   test_size = 1000, number of testing images

#   OUTPUT
#   After running the code UMD.py, the folder structure that will be generatd is as follows:
#   1. Inside the data_UMD folder, a folder 'cache' will be created
#   2. Inside the data_UMD folder, a folder 'color' (if use_Color=True) else 'gray' will be created
#   3. Inside the 'color'/'gray' folder, two folders namely 'train' and 'test' will be created
#   4. Inside each of the 'train' and 'test' folders,
#      'neg' folder for negative images and 'pos' foder for positive images will be created         
###########################################################################################################



import os
import glob
import sys
import csv
import numpy as np
import random
import cv2
import math
import argparse
import cPickle

from util_file import *

def parse_UMD(image_dir, anno_dir,train_size,test_size):
    """ origional annotation format
            '313', 'gaetano_donizetti/gaetano_donizetti_0010.jpg', '3.652360', '0.998470', '235.973200', '113.164400', '83.661600', '82.111200', '12.000000', '-21.000000', '1.000000', '242.945000', 
            '123.762000', '0.672196', '249.732000', '122.254000', '0.953512', '258.527000', '123.782000', '0.987899', '275.412000', '122.693000', '0.976441', '285.191000', '120.007000', '0.952408', '294.760000', '120.541000', '0.888727', '248.084000', '130.652000', 
            '0.918214', '254.237000', '130.043000', '1.003340', '260.078000', '130.637000', '0.961023', '278.597000', '129.900000', '0.959223', '285.327000', '128.429000', '0.985439', '291.989000', '128.231000', '0.981398', '243.272000', '147.739000', '0.000000', '261.525000', '152.766000', '0.627117', '267.922000', '153.909000', '0.989203', '278.154000', '151.961000', '0.948437', '312.663000', '144.420000', '0.000000', '261.234000', '167.113000', '0.896388', '271.949000', '168.055000', '0.972544', '284.254000', 
            '166.072000', '0.986057', '274.983000', '188.433000', '0.247581', '0.874067', '0.125933'
        """
    # check directories of the dataset
    check_path(image_dir)
    check_path(anno_dir)
    #parse the annotation file
    anno_file = os.path.join(anno_dir, 'umdfaces_batch3_ultraface.csv')
    dataset=[]
    
    num_train_test_size=train_size+test_size 
    
    count=0
    with open(anno_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            
            per_data_info=[]
            img_name=row[1]
            per_data_info.append(img_name)
            face_x=row[4]
            per_data_info.append(face_x)
            face_y=row[5]
            per_data_info.append(face_y)
            face_width=row[6]
            per_data_info.append(face_width)
            face_height=row[7]
            per_data_info.append(face_height)
            count+=1
            dataset.append(per_data_info)
            if(count<num_train_test_size):
                continue
            break
    
    return dataset
    
def create_datasets_UMD(image_dir,anno_dir,save_dir,use_Color,patch_size,train_size,test_size):
    dataset=parse_UMD(image_dir,anno_dir,train_size,test_size)
    
    # create directories for saving cropped datasets if necessary
    make_dir_if_not_exist(save_dir)
    dataset_tag ='color' if use_Color  else 'gray'
    
    save_folder = os.path.join(save_dir, dataset_tag)
    make_dir_if_not_exist(save_folder)
    
    dataset_train='train' 
    save_folder_train = os.path.join(save_folder, dataset_train)
    make_dir_if_not_exist(save_folder_train)
    
    dataset_test='test' 
    save_folder_test = os.path.join(save_folder, dataset_test)
    make_dir_if_not_exist(save_folder_test)
    
    #create pos folder-train
    positive='pos'
    positive_folder_train=os.path.join(save_folder_train, positive)
    make_dir_if_not_exist(positive_folder_train)
    
    #create neg folder-train
    negative='neg'
    negative_folder_train=os.path.join(save_folder_train, negative)
    make_dir_if_not_exist(negative_folder_train)
    
    #create pos folder-test
    positive='pos'
    positive_folder_test=os.path.join(save_folder_test, positive)
    make_dir_if_not_exist(positive_folder_test)
    
    #create neg folder-test
    negative='neg'
    negative_folder_test=os.path.join(save_folder_test, negative)
    make_dir_if_not_exist(negative_folder_test)
    
    count=0
    dSize=patch_size
    
    img_tag = cv2.IMREAD_COLOR if use_Color else cv2.IMREAD_GRAYSCALE
    
    #train
    #crop positive
    for i in range(1,train_size):
        per_data_info=dataset[i]
        full_name=per_data_info[0]
        index_of_slash=full_name.find('/')
        img_name=full_name[index_of_slash+1:]
        folder_name=img_name[:index_of_slash]
        X=int(float(per_data_info[1]))
        Y=int(float(per_data_info[2]))
        W=int(float(per_data_info[3]))
        H=int(float(per_data_info[4]))
                
        #find the image in the image_dir
        folder_path=os.path.join(image_dir,folder_name)
        
        # if use_Color is True
        if use_Color:
          
            for filename in glob.glob(folder_path+'\*.jpg'): 
                
                length=len(img_name)
                filename_short=filename[len(filename)-length:]
                
                if(filename_short==img_name):
                    
                    img= cv2.imread(folder_path+'\\'+img_name,img_tag)
                    cv2.rectangle(img,(X,Y),(X+H,Y+H),(255,255,255))
                    
                    #crop pos
                    cropped_image_pos=img[Y:Y+H,X:X+W]
                    
                    #crop neg
                    cropped_image_neg=img[0:dSize,0:dSize]
                    
                    #save pos
                    resized_pos=cv2.resize(cropped_image_pos,(dSize,dSize)) 
                    cv2.imwrite(positive_folder_train+'\\'+img_name,resized_pos)
                    
                    #save neg
                    resized_neg=cv2.resize(cropped_image_neg,(dSize,dSize))
                    cv2.imwrite(negative_folder_train+'\\'+img_name,resized_neg)
                    
        # if use_Color is False            
        else:
            
            for filename in glob.glob(folder_path+'\*.jpg'): 
                
                length=len(img_name)
                filename_short=filename[len(filename)-length:]
                
                if(filename_short==img_name):
                    
                    img= cv2.imread(folder_path+'\\'+img_name,img_tag)
                    cv2.rectangle(img,(X,Y),(X+H,Y+H),(255,255,255))
                    
                    #crop pos
                    cropped_image_pos=img[Y:Y+H,X:X+W]
                    
                    #crop neg
                    cropped_image_neg=img[0:dSize,0:dSize]
                    
                    #save pos
                    resized_pos=cv2.resize(cropped_image_pos,(dSize,dSize)) 
                    cv2.imwrite(positive_folder_train+'\\'+img_name,resized_pos)
                    
                    #save neg
                    resized_neg=cv2.resize(cropped_image_neg,(dSize,dSize))
                    cv2.imwrite(negative_folder_train+'\\'+img_name,resized_neg)
          
    #**************************************************************************
    #test
    for i in range(train_size,train_size+test_size):
        per_data_info=dataset[i]
        full_name=per_data_info[0]
        index_of_slash=full_name.find('/')
        img_name=full_name[index_of_slash+1:]
        folder_name=img_name[:index_of_slash]
        X=int(float(per_data_info[1]))
        Y=int(float(per_data_info[2]))
        W=int(float(per_data_info[3]))
        H=int(float(per_data_info[4]))
                
        #find the image in the image_dir
        folder_path=os.path.join(image_dir,folder_name)
        
        # if use_Color is True
        if use_Color:
          
            for filename in glob.glob(folder_path+'\*.jpg'): 
                
                length=len(img_name)
                filename_short=filename[len(filename)-length:]
                
                if(filename_short==img_name):
                    
                    img= cv2.imread(folder_path+'\\'+img_name,img_tag)
                    cv2.rectangle(img,(X,Y),(X+H,Y+H),(255,255,255))
                    
                    #crop pos
                    cropped_image_pos=img[Y:Y+H,X:X+W]
                    
                    #crop neg
                    cropped_image_neg=img[0:dSize,0:dSize]
                    
                    #save pos
                    resized_pos=cv2.resize(cropped_image_pos,(dSize,dSize)) 
                    cv2.imwrite(positive_folder_test+'\\'+img_name,resized_pos)
                    
                    #save neg
                    resized_neg=cv2.resize(cropped_image_neg,(dSize,dSize))
                    cv2.imwrite(negative_folder_test+'\\'+img_name,resized_neg)
                    
        # if use_Color is False            
        else:
            
            for filename in glob.glob(folder_path+'\*.jpg'): 
                
                length=len(img_name)
                filename_short=filename[len(filename)-length:]
                
                if(filename_short==img_name):
                    
                    img= cv2.imread(folder_path+'\\'+img_name,img_tag)
                    cv2.rectangle(img,(X,Y),(X+H,Y+H),(255,255,255))
                    
                    #crop pos
                    cropped_image=img[Y:Y+H,X:X+W]
                    
                    #crop neg
                    cropped_image=img[Y:Y+H,X:X+W]
                    
                    #save pos
                    resized=cv2.resize(cropped_image,(dSize,dSize))
                    cv2.imwrite(positive_folder_test+'\\'+img_name,resized)
        
                    #save neg
                    resized_neg=cv2.resize(cropped_image_neg,(dSize,dSize))
                    cv2.imwrite(negative_folder_test+'\\'+img_name,resized_neg)

# --image_dir .\data_UMD\originalPics, --anno_dir .\data_UMD\annotations,  --save_dir .\data_UMD\cache, 
# --use_Color True for Color else False, -- patch_size=60 , --train_size =10000 , --test_size= 1000 
                    #

if __name__ == '__main__':
    
    create_datasets_UMD('.\data_UMD\original_pics', '.\data_UMD\Annotation','.\data_UMD\cache',True,60,10000,1000)