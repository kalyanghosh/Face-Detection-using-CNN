
# coding: utf-8

# In[7]:


#*******************************************#
#Importing the libraries 

from keras import layers
from keras import models

#*******************************************#
#Defining the architechture

model=models.Sequential()

model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(60,60,3)))

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64,(3,3),activation='relu'))

model.add(layers.MaxPooling2D(2,2))

model.add(layers.Conv2D(128,(3,3),activation='relu'))

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(128,(3,3),activation='relu'))

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Flatten())

model.add(layers.Dense(512,activation='relu'))

model.add(layers.Dense(1,activation='sigmoid'))

#**********************************************#
# Summazing the model

#model.summary()

#**********************************************#
# Configuring the model for training

from keras import optimizers

model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
             metrics=['acc'])

#***********************************************#
# Using the ImageDataGenerator class to read the.. 
# images from the directories

from keras.preprocessing.image import ImageDataGenerator

train_dir='/home/kghosh/dataset/data_UMD/cache1/color/train/'
test_dir='/home/kghosh/dataset/data_UMD/cache1/color/test/'

#Rescale all the images by 1/255
train_datagen=ImageDataGenerator(rescale=1./255)
test_datagen=ImageDataGenerator(rescale=1./255)

train_generator=train_datagen.flow_from_directory(
                train_dir,
                target_size=(60,60),
                batch_size=20,
                class_mode='binary')
test_generator=test_datagen.flow_from_directory(
                test_dir,
                target_size=(60,60),
                batch_size=20,
                class_mode='binary'
                )
#Fit the model using batch generator
history=model.fit_generator(
        train_generator,
        steps_per_epoch=100,
        epochs=30,
        validation_data=test_generator,
        validation_steps=50)

#Save the model 
model.save('face_vs_nonface.h5')

#Plotting accuracy and loss
import matplotlib.pyplot as plt
acc=history.history['acc']
test_acc=history.history['val_acc']
loss=history.history['loss']
test_loss=history.history['val_loss']
epochs=range(1,len(acc)+1)

plt.plot(epochs,acc,'bo',label='TRAINING ACCURACY')
plt.plot(epochs,test_acc,'b',label='TEST ACCURACY')
plt.title('TRAINING AND TEST ACCURACY')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.figure()

plt.plot(epochs,loss,'bo',label='TRAINING LOSS')
plt.plot(epochs,test_loss,'b',label='TEST LOSS')
plt.title('TRAINING AND TESTING LOSS')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()










