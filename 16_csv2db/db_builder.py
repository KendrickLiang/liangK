#Team Just Kidding -- Kendrick Liang, Joyce Liao
#SoftDev1 pd8
#K16 -- No Trouble
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#converts .csv file into a list of rows
def convert_to_list(filename):
    main_list = []
    with open(filename) as newFile:  
        reader = csv.DictReader(newFile)
        for row in reader:
            row_values = []
            for value in row:
                row_values.append(row[value]) #store each row as individual list
            main_list.append(row_values) #add new row to the main list
    return main_list

#fill given table with values
def populate_table(listname, tablename):
    for row in listname:
        command = "INSERT INTO %s Values (\'%s\',%s,%s)" % (tablename, row[0], row[1], row[2]) #generate sqlite command to insert value into table for each row
        #print(command)
        c.execute(command) #run command

#========================================================
                 
people  = convert_to_list('data/peeps.csv')
#print(people)
#build SQL stmt, save as string
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)" #create new table for peep.csv
c.execute(command)    #run SQL statement
populate_table(people, 'peeps')


classes = convert_to_list('data/courses.csv')
#print(classes)
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)
populate_table(classes, 'courses')


#==========================================================

db.commit() #save changes
db.close()  #close database

