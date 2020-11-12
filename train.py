import numpy as np 
from keras import backend as K
import argparse

train_dir = 'data/train'
test_dir = 'data/test'

ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-m", "--model", required=True,
	help="path to output model")
"""
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output loss/accuracy plot")
"""
args = vars(ap.parse_args())

train_datagen = ImageDataGenerator(
	rescale = 1. /  255, 
	shear_range = 0.2, 
	zoom_range = 0.2, 
	horizontal_flip = True)

test_datagen = ImageDataGenerator(
	rescale = 1. / 255)

train_generator = train_datagen.flow_from_directory(
	'data/train_little', 
	target_size=(150,150), 
	batch_size = batch_size, 
	class_mode = 'binary')

test_generator = test_datagen.flow_from_directory( 
	'data/test_little', 
	target_size = (150, 150), 
	batch_size = batch_size, 
	class_mode = 'binary')


