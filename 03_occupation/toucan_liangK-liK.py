# toucan: Kendrick Liang & Kenny Li
# SoftDev1 pd8
# K #06: StI/O: Divine your Destiny!
# 2018-09-13

import csv
import random

with open('occupations.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) #skips 1st row which is the header
    data = []
    for row in csv_reader:
        row = [row[0],  float(row[1])] #converts percentages from str to float
        data.append(row) 
    d = dict(data) #converts list into dictionary

def weightedRandom():
    total = d['Total'] #sets total to total percentage
    randFloat = round(random.uniform(0,total-.1), 1) #creates random float btwn 0, 99.7 inclusive
    #print (randFloat)

    if 'Total' in d: #deletes the total key
        del d['Total']

    sum = 0.0
    for percentage in d: #continuously adds the percentage
        sum += d[percentage]
        if(round(sum, 1)) > randFloat: #returns 1st percentage that exceeds the randomly generated float
            return percentage

print (weightedRandom())