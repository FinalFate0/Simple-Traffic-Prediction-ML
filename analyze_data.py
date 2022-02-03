import openpyxl
import numpy as np
import matplotlib.pyplot as plt

# hour_of_day: hours (0,...,23)
# season: spring, summer, autumn, winter (0,1,2,3)
# day of week: mon, tue, wed, thu, fri, sat, sun (0,1,2,3,4,5,6)
# daytime: night, dawn, day, dusk (0,1,2,3)

hour_of_day = []
type_of_day = []
day_of_week = []
season = []
daytime = []
temperature = []
visibility = []
volume = []
rain_intensity = []
rain_state = []

obj = openpyxl.load_workbook(filename='processed.xlsx', read_only=True)
data = obj.active

for row in data.iter_rows(min_row=2):
    hour_of_day.append(row[10].value)
    type_of_day.append(row[2].value)
    day_of_week.append(row[1].value)
    season.append(row[3].value)
    daytime.append(row[4].value)
    temperature.append(row[7].value)
    visibility.append(row[8].value)
    volume.append(row[9].value)
    rain_intensity.append(row[5].value)
    rain_state.append(row[6].value)

obj.close()

variables = {"Hour of day":hour_of_day,
           "Type of day":type_of_day,
           "Day of week":day_of_week,
           "Season":season,
           "Daytime":daytime,
           "Temperature":temperature,
           "Visibility":visibility,
           "Volume":volume,
           "Rain intensity":rain_intensity,
           "Rain state":rain_state
           }


number_variables = {"Temperature":temperature,
           "Visibility":visibility,
           "Volume":volume,
           "Rain intensity":rain_intensity,
           "Rain state":rain_state
           }

for name, variable in number_variables.items():
    print("Variable:", name)
    print("min = ", min(variable))
    print("max = ", max(variable))
    print("mean = ", np.mean(variable))
    print("median = ", np.median(variable))
    print("range = ", np.ptp(variable))
    print("std dev = ", np.std(variable))
    print("variance = ", np.var(variable))
    print("histogram = ", np.histogram(variable))
    plt.hist(variable, 10)
    plt.show()
    print()


def correlation(a, b):
    a = (a - np.mean(a)) / (np.std(a) * len(a))
    b = (b - np.mean(b)) / np.std(b)
    return np.correlate(a, b)

for name1, var1 in number_variables.items():
    for name2, var2 in number_variables.items():
        print("Correlation between {} and {} is {}"\
              .format(name1, name2, 
                      correlation(var1, var2)))

