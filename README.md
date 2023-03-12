# Simple-Traffic-Prediction-ML
**Predict traffic volume on Expressway S6 based on weather and time data**

A Python Machine Learning study project made as part of the PJATK(PJAIT) Gdańsk Machine Learning course, using Keras/TensorFlow and a public dataset from the Bridge of Knowledge database. The data has been gathered from the Expressway S6 in Gdańsk across the years 2014-2017.  
The model is a simple Fully Connected Neural Network with one hidden layer.

The project consists of the following Python scripts:  
```analyze_data.py```: used for simple dataset analysis  
```model.py```: containing the model description  
```training.py```: used for training the model  
```predict.py```: used for predicting using a pre-trained model file (```model.h5```) placed in the same directory  
```evaluate.py```: example script used for comparing the predicted output with the test data from the dataset  

Link to public dataset:  
[[Bridge of Knowledge]Permanent traffic counting stations - Expressway S6 in Gdansk (dataset containing 5-min aggregated traffic data and weather information)](https://mostwiedzy.pl/en/open-research-data/permanent-traffic-counting-stations-expressway-s6-in-gdansk-dataset-containing-5-min-aggregated-traf,923120743943369-0)


#### Required input for```predict.py```:

```Hour of Day (0-23; 24-Hour Time Format)
Day of Week (0-6; Monday-Sunday)
Type of Day (0-2; Regular Day, Public Holiday, Summer/Winter Holiday)
Current Season (0-3; Spring, Summer, Autumn, Winter)
Time of Day (0-3; Night, Dawn, Day, Dusk)
Rain Intensity (0-100; Least to Most)
Rain State (0-5; No Rain, Drizzle, Light Rain, Moderate Rain, Continuous Rain, Light Snow, Intense Snow)
Temperature in Celcius (Float Value)
Current Visibility (0-8)
