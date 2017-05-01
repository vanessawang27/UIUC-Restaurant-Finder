import pandas
import math
import numpy as np

def restaurantDistance(name): #Find the distance of one specified restaurant to all other restaurants
    with open("restaurants.csv", 'r') as csvfile:
        rData = pandas.read_csv(csvfile)

    #A simple euclidean distance function
    def euclidean_distance(row):
        inner_value = 0
        for k in distance_columns:
            inner_value += (row[k] - selected_restaurant[k]) ** 2
        return math.sqrt(inner_value)

    # Prints data for specified restaurant
    selected_restaurant = rData[rData["id"] == name ].iloc[0]
    #print(selected_restaurant)

    distance_columns = ['city', 'category', 'price'] #could change depending on how you want to compare

    restaurant_distance = rData.apply(euclidean_distance, axis=1)
    #print(restaurant_distance)

    rArray = []
    for i in range(15):
        rArray.append(restaurant_distance[i])

    return rArray #returns array with all the distances for the specified restaurant


def avgDistance(usernum): #for one user finds the average distance from all his/her liked restaurants
    with open("user.csv", 'r') as csvfile2:
        uData = pandas.read_csv(csvfile2)

    avgArr = np.zeros(15)
    # The names of all the columns in the data.
    for k in range(15): #traverse through all restaurant names
        #iloc[0] == User 1 and so on
        if (uData[ uData.columns.values[k+1] ].iloc[usernum] == 1):
            currArr = restaurantDistance(uData.columns.values[k+1])
            avgArr = [x + y for x, y in zip(avgArr, currArr)]
            #print avgArr
    #print(avgArr)
    print "{} {}".format("User",usernum)
    results = uData.columns.values[np.argsort(avgArr)[:4]]
    print(results)

##Main##

avgDistance(1)
