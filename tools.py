import csv
from operator import itemgetter
from collections import defaultdict
from sample import get_business, obtain_bearer_token

token = obtain_bearer_token('https://api.yelp.com','/oauth2/token')

def collab():
    columns = defaultdict(list) # each value in each column is appended to a list
    ratings = []

    with open('User.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value
                if k != 'user': 
                    columns[k].append(v) # append the value into the appropriate list
                                     # based on column name k
    for res, rating in columns.items():
        rating = map(int, rating)
        ratings.append(tuple([res, sum(rating)]))

    ratings = list(reversed(sorted(ratings,key=itemgetter(1))))
    top4 = ratings[0:4]
    return top4

def yelpAPI_GetBusinesses(inputs):
    result = []
    for restaurant in inputs:
        search_result = get_business(token, restaurant[0])
        result.append(search_result)
    return result