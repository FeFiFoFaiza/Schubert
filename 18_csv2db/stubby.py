#a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo") 

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE roster(name TEXT,
           userid INTEGER)")

db.commit() #save changes
db.close()
