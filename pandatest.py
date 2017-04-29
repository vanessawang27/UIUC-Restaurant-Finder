import pandas
import math

with open("restaurants.csv", 'r') as csvfile:
    rData = pandas.read_csv(csvfile)

# The names of all the columns in the data.
#print(rData.columns.values)

# Prints data for specified restaurant
selected_restaurant = rData[rData["id"] == "masijta-grill-urbana"].iloc[0]
print(selected_restaurant)

distance_columns = ['city', 'category', 'price'] #could change depending on how you want to compare

#A simple euclidean distance function
def euclidean_distance(row):
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_restaurant[k]) ** 2
    return math.sqrt(inner_value)

restaurant_distance = rData.apply(euclidean_distance, axis=1)
print(restaurant_distance)