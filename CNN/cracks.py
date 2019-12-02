# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:54:41 2019

@author: vladm
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from IPython.display import display
from PIL import Image

import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model


class CnnClassifier:
    def __init__(self):
        self.classifier = Sequential()

        self.classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))

        self.classifier.add(Flatten())

        self.classifier.add(Dense(128, activation='relu'))
        self.classifier.add(Dense(1, activation='sigmoid'))

        self.classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.TRAINING_PATH = r"C:\Master\TAIP\training-datasets\concrete-crack-images-for-classification\Concrete " \
                             r"Crack Images for Classification"
        self.train_datagen = None
        self.training_set = None

    def save_model(self, path):
        self.classifier.save(path)

    def load_training_dataset(self):
        self.train_datagen = ImageDataGenerator(
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

        self.training_set = self.train_datagen.flow_from_directory(self.TRAINING_PATH,
                                                                   target_size=(64, 64),
                                                                   batch_size=32,
                                                                   class_mode='binary')

    def train(self):
        self.classifier.fit_generator(
            self.training_set,
            steps_per_epoch=40000,
            epochs=1)

    def predict(self, path):
        test_image = image.load_img(path, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.classifier.predict(test_image)
        return result


model = CnnClassifier()
model.load_training_dataset()
# #model.train()
# result = model.predict("rC:\Master\TAIP\cracks\random-images\19597.jpg")
# print(result[0][0])
# if result[0][0] >= 0.5:
#     prediction = 'crack'
# else:
#     prediction = 'not crack'
# print(prediction)
#
# model.save_model(r"C:\Master\TAIP\cracks\models\models.h5")


# training_set.class_indices


# test_image = image.load_img(r"C:\Master\TAIP\cracks\random-images\00084.jpg", target_size=(64, 64))
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis=0)

# result = classifier.predict(test_image)
# training_set.class_indices

# print(result[0][0])
# if result[0][0] >= 0.5:
#     prediction = 'crack'
# else:
#     prediction = 'not crack'
