# LemonSoda - Kendrick Liang, Johnson Li
# SoftDev1 pd8
# K17 -- Average
# 2018-10-05

import sqlite3
import csv

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

# opens csv data and puts data into tables inside discobandit.db
# replaces row if already exists so program doesn't crash
with open("data/peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
    for row in reader:
        c.execute("INSERT OR REPLACE INTO peeps VALUES(?,?,?)", (row["name"],  row["age"],  row["id"]))

with open("data/courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER, PRIMARY KEY(code, id))")
    for row in reader:
        c.execute("INSERT OR REPLACE INTO courses VALUES(?,?,?)", (row["code"], row["mark"],  row["id"]))

grades = {}
ids = {}
data = c.execute("SELECT peeps.name, courses.mark, peeps.id FROM peeps, courses WHERE peeps.id = courses.id")
def process_data():
    # processes data in db and puts them in dictionaries
    for row in data:
        if row[0] not in grades:
            grades[row[0]] = [row[1]]
            ids[row[0]] = row[2]
        else:
            grades[row[0]].append(row[1])

def calculate_averages():
    # calculates average from each student's list of grades and replaced value with average
    for person in grades:
        grades[person] = round(sum(grades[person]) / float(len(grades[person])), 2)

def display_averages():
    # prints out name, id, and average in command line
    for person in grades:
        print("Name: {0}, ID: {1}, Average: {2}".format(person, ids[person], grades[person]))

def make_avg_table():
    # makes a new table called 'peeps_avg' and insers the values from the processed data
    c.execute("CREATE TABLE IF NOT EXISTS peeps_avg(name TEXT, id INTEGER, average INTEGER, PRIMARY KEY(id))")
    for person in grades:
        # replaces row if already exists so program doesn't crash
        c.execute("INSERT OR REPLACE INTO peeps_avg VALUES(?,?,?)", (person, ids[person],  grades[person]))
        
def add_course(code, mark, student_id):
    # adds a new row to the course table and deletes the peeps_avg table and remakes it
    # replaces row if already exists so program doesn't crash
    c.execute("INSERT OR REPLACE INTO courses VALUES(?,?,?)", (str(code), int(mark), int(student_id)))
    c.execute("DROP TABLE IF EXISTS peeps_avg")

process_data()

calculate_averages()
display_averages()

make_avg_table()

# add_course("Maf0", 0, 10)
# add_course("Maf1", 0, 10)
# add_course("Maf2", 0, 10)
# add_course("Maf3", 0, 10)
# add_course("Maf4", 0, 10)
# add_course("Maf0", 0, 1)
# add_course("Maf1", 0, 1)
# add_course("Maf2", 0, 1)
# add_course("Maf3", 0, 1)
# add_course("Maf4", 0, 1)

# make_avg_table()

db.commit() #save changes
db.close()  #close database