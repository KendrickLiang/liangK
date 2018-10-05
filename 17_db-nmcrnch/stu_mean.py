import sqlite3
import csv

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()
grades = {}
data = c.execute("SELECT peeps.name, courses.mark FROM peeps, courses WHERE peeps.id = courses.id")
def process_data():
    for row in data:
        if row[0] not in grades:
            grades[row[0]] = [row[1]]
        else:
            grades[row[0]].append(row[1])
def calculate_averages():
    counter = 0
    for person in grades:
        
print(grades)
        
