###########################################################################################################
               DATA PREPROCESSING IO CODE (UMD.py)
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

                     NEURAL NETWORK CODE (cnn_code.py)
###########################################################################################################

#Instructions to run the code cnn_code.py inside the code folder

#1. Navigate to the code folder inside the Project_2 folder
#2. Give the path of train_dir = '/home/kghosh/dataset/data_UMD/cache1/color/train/'
#   Give the path to test_dir = '/home/kghosh/dataset/data_UMD/cache1/color/test/'
#3. Run the python file cnn_code.py in the terminal using the below command:
#   ($python cnn_code.py)
#4. After the code is run and all the epochs complete,the model will be saved in 
# face_vs_nonface.h5



#############################################################################################################