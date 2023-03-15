import json
import os

directory = "json/"

for filename in os.listdir(directory):
    file = open(directory + filename)
    data = json.load(file)
    print(filename)    
    for index in range(8, 13):
        print(data['attributes'][index]['value'])
        