#### Relational database
* DB that stores information as a collection of tables.
* FIELD: "Column" data in a RDB
* RECORD: "Row" in a RDB
* Data can be linked between tables based on field values.

#### SQL (Structured Query Language)
* Standard language designed to work with relational dbs.
 
used for many major db programs, though implementations
 may not (mostly are not) be compatible.

eg, some implementations:
MySQL, PostgreSQL, SQLite, Oracle, IBM DB2, Sybase, M$ Access, ... 


#### SQLite 
* SQL implementation that relies entirely on function calls in the parent program. (no db server)
* All db info stored in a single file.
* Data is dynamically typed as values are inserted.

#### Data Organization
* data type will help to convert entered values to a suggested type.
* data types: TEXT, INTEGER, REAL, NUMERIC, BLOB
* NUMERIC will default to an integer, but can be a floating point.
* BLOB means no suggested type.
* Columns can be given a PRIMARY KEY attribute, denoting that every entry in that column is unique and cannot be NULL. 
* Columns can be given a NOT NULL attribute, denoting that no entry can be NULL.

#### Basic SQLite Operations:

`CREATE TABLE`
  Add a table to a database 
eg,   
`CREATE TABLE <name> (<column name> <data type>, ...)`

`INSERT INTO`
Insert a record into a table.

eg,
`INSERT INTO <tbl_name> VALUES ( <field 1>, <field 2> ...)`
Will add a record to a table matching the values to the columns in order.
    
`NULL` can be used in any entry

eg,
```
CREATE TABLE tpotusa (name TEXT, id INTEGER PRIMARY KEY);
INSERT INTO tpotusa VALUES ("basitar", 2);
INSERT INTO tpotusa VALUES ("guitbass", 1);
INSERT INTO tpotusa VALUES ("drums", 0);
```


eg,
```
CREATE TABLE amunals (name TEXT, id INTEGER PRIMARY KEY);
INSERT INTO amunals VALUES ("whose-it", 2);
INSERT INTO amunals VALUES ("whats-it", 1);
INSERT INTO amunals VALUES ("blurb", 0);
```

To show all fields for each entry (record) in table tbl_name, use the wildcard operator:

```
SELECT * FROM <tbl_name>;
```

eg,
```
SELECT * FROM tpotusa;
```

To show a single field for each record in table tbl_name, use the wildcard operator:
```
SELECT <field_name> FROM <tbl_name>;
```

eg,
```
SELECT name FROM tpotusa;
```

You can also filter results: 

eg,
```
SELECT name FROM tpotusa WHERE id = 0;
```


__SQLite shell is your friend.__
* Use like IDLE or Python shell to interact live, test, etc.

```
$ sqlite3 <dbfilename>
```
* N: shell cmds begin with a dot
* N: some useful SQLite shell commands:
```
  .quit
  .tables
  .header on|off
  .mode column|csv|list|html|insert|line|tabs
  .help
```

#### a Python script for interacting with an SQLite db:
```python
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo") 

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")

db.commit() #save changes
db.close()
```

----------------------------------------------------------
