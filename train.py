import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from timeit import default_timer as timer

import model


epochs = 100
batch_size = 32
filename = 'model'
random_seed = 20149
optimizer = 'adam'
loss = 'mean_squared_error'

train_data = pd.read_excel('train_data.xlsx', skiprows=[0]).values
train_data_y = pd.read_excel('train_data_y.xlsx', skiprows=[0]).values
valid_data = pd.read_excel('valid_data.xlsx', skiprows=[0]).values
valid_data_y = pd.read_excel('valid_data_y.xlsx', skiprows=[0]).values
test_data = pd.read_excel('test_data.xlsx', skiprows=[0]).values
test_data_y = pd.read_excel('test_data_y.xlsx', skiprows=[0]).values


tf.random.set_seed(random_seed)

model = model.two_layer.build()

model.compile(loss=loss, optimizer=optimizer)
model.summary()

start_time = timer()
h = model.fit(train_data, train_data_y, epochs=epochs, batch_size=batch_size, validation_data=(valid_data, valid_data_y))
training_time = timer()-start_time
print("training time: {:.2f} s.".format(training_time))

model.save(filename+".h5")

model.evaluate(test_data, test_data_y)


plt.style.use("ggplot")
plt.figure()
plt.plot(range(1,epochs+1), h.history["loss"], label="train loss")
plt.plot(range(1,epochs+1), h.history["val_loss"], label="validation loss")
plt.title("Train/validation loss")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.legend()
plt.savefig(filename+".png")

