import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import numpy as np
import tensorflow as tf
import argparse


model = tf.keras.models.load_model('model.h5')

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=False, 
                help="output model file name",
                default='model.h5', metavar="filename")
ap.add_argument("-hr", "--hour", required=True, type=int, 
                help="hour of day", default=0, metavar='int')
ap.add_argument("-w", "--weekday", required=True, type=int, help="day of week",
                default=0, metavar='int')
ap.add_argument("-t", "--type", required=True, type=int, 
                help="type of day", default=0, metavar='int')
ap.add_argument("-s", "--season", required=True, type=int, 
                help="season", default=0, metavar='int')
ap.add_argument("-d", "--daytime", required=True, type=int, 
                help="time of day", default=0, metavar='int')
ap.add_argument("-ri", "--rain_intensity", required=True, type=float, 
                help="rain intensity", default=0.0, metavar='float')
ap.add_argument("-rs", "--rain_state", required=True, type=int, 
                help="rain state", default=0, metavar='int')
ap.add_argument("-tmp", "--temperature", required=True, type=float, 
                help="temperature in celcius", default=0.0, metavar='float')
ap.add_argument("-v", "--visibility", required=True, type=int, 
                help="visibility", default=0, metavar='int')

args = vars(ap.parse_args())
model_filename = args["model"]
hour = args["hour"]
weekday = args["weekday"]
type_of_day = args["type"]
season = args["season"]
daytime = args["daytime"]
rain_intensity = args["rain_intensity"]
rain_state = args["rain_state"]
temperature = args["temperature"]
visibility = args["visibility"]

to_predict = np.array([[hour, weekday, type_of_day, season, daytime, rain_intensity, rain_state, temperature, visibility]])
result = model.predict(to_predict)
print("Predicted traffic volume: ", result)
