import tensorflow as tf
import matplotlib
from tensorflow import keras
from tensorflow.keras import layers

from filter_data import clean_data
from generate_ds import generate_dataset
from visualize import visualize
from unzip import unzip

matplotlib.use("Qt5Agg")

# unzip()

# clean_data()

train_ds, val_ds = generate_dataset()

print("visualise initiating")
visualize(train_ds)
