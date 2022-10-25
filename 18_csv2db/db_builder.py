#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

command = "create table students(name text, age int, id text)"
c.execute(command)

with open ('students.csv', newline ='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'], row['id'])
        command = f"insert into students values({row['name']},{row['age']},{row['id']})"
        c.execute(command)

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

'''
command = "create table urmom(weight int, height int, age int, sexiness double)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

command = "insert into urmom values(1000,60,120,1000.0)"
c.execute(command)
'''

#==========================================================

db.commit() #save changes
db.close()  #close database


