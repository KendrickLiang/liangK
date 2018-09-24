#KraZy Codes (Kendrick Liang, Zane Wang)
#SoftDev1 pd8
#K10: Jinja Tuning
#2018-09-24
from flask import Flask, render_template
import csv
import random
app = Flask(__name__)
dict = {}
with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile) #using dictreader instead of reader allows us to be able to pass parameters from the 1st row to create dict
    for row in reader:
        dict[row['Job Class']] = float(row['Percentage'])
    del dict['Total']
def randomOccupation():
    randomselect = random.uniform(0,99.9)
    print (randomselect)
    for x in dict:
        randomselect = randomselect - dict[x]
        if (randomselect <= 0):
            return x
@app.route("/occupations")
def tablefy():
    return render_template("occupations.html",Title = 'Occupations', Heading = 'Table of Some Occupations', value = 'Possible option: ' + randomOccupation(), col1 = 'Job Class', col2 = 'Percentage', result = dict)
if __name__ == "__main__":
    app.debug = True
    app.run()
