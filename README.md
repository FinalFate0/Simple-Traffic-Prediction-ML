# Simple-Traffic-Prediction-ML
Predict traffic volume based on weather and time data

Link to dataset used for training: https://mostwiedzy.pl/pl/open-research-data/permanent-traffic-counting-stations-expressway-s6-in-gdansk-dataset-containing-5-min-aggregated-traf,923120743943369-0

A simple ML project using data from the Expressway S6 in Gdansk.
Produces a value describing how much traffic passes in 5 minutes.

Required input:
hour (0-23)
day of week Mon-Sun (0-6)
type of day (0-2; regular day, public holiday, summer/winter holiday)
current season (0-3; spring, summer, autumn, winter)
time of day (0-3; night, dawn, day, dusk)
rain intensity (0-100)
rain state (0-5; no rain, drizzle, light rain, moderate rain, continues rain, light snow, intensive snow)
temperature in celcius(float value)
current visibility (0-8)
