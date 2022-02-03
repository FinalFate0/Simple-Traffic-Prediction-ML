import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import numpy as np
import tensorflow as tf


model = tf.keras.models.load_model('model.h5')

test_data = pd.read_excel('test_data.xlsx', skiprows=[0]).values
test_data_y = pd.read_excel('test_data_y.xlsx', skiprows=[0]).values

model.evaluate(test_data, test_data_y)

print('')
print("Comparing first 1000 results...")
for i in range(1000):
    
    test_case = np.array([test_data[i]])
    test_case_expected = test_data_y[i]
    test_case_result = model.predict(test_case)
    
    print("Case #", i+1, " Expected:", test_case_expected, " Predicted:", test_case_result[0])
    