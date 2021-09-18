import pandas as pd
import numpy as np


import os
import sys
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
import keras
sys.stderr = stderr

from keras.models import Model, Sequential
from keras.layers import *
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import multi_gpu_model
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn.metrics import *

def get_model(x_train):
    """
    Return the requested Keras model

    :param x_train:      The NumPy array used for training (for dimension size extraction)


    :return:             The Keras model
    """
    
    # some parameters to control model
    dp_lvl = 0.2
    regularizer_lvl = 0.002
    # network design
    model = Sequential()
    <<<TODO>>> # crate your model here
    
    return model