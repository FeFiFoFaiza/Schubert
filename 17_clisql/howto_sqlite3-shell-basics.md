# how-to :: sqlite3 shell basics
---
## Overview
SQLite is the lite weight, handy dandy way of making and organising a database.
This guide will teach you how to create, show, and save a one table database.

### Estimated Time Cost: 0.5 hrs (Depending on your data)

### Prerequisites:

- Have SQLite3 installed
- Have some type of table you want to input
____
### **Starting Point**
There are two ways to start to make a database on the get go:  
   - By inline commands on the terminal  
   With this method, each command would be it's own line (and yes you have to press enter after each)  
   ```shell
   foo@root:~$ sqlite3
   ```

   - By .sql file  
   If you want to run it via terminal:  
   ```shell
    foo@root:~$ sqlite3 < file.sql
   ```  

### **Creation**
Let's say we have a table
| Food | Price  |
|------|--------|
| Apple|  13.01 |  
|Cereal|  54.67 |

In order to create this table, you'd type the following command  
`CREATE TABLE menu(name text, price double);`  
Here you're creating a table called menu that has two columns: the name column that's all text and the price column which holds doubles.
<br>
<br>
### **Insertion**
In order to actually input values into the table, you'd type:  
`INSERT INTO menu values('Apple', 13.01);`  
Here you are inserting a row into menu that has the value 'Apple' (corresponding to the name) and the value 13.01 (corresponding to the price)
<br>
<br>
### **Saving**
Once you're done with inputting everything into your table how do you save?
If you made your database using the terminal, then right now it's only been written into the memory. If you were to exit or quit the program, you'd lose it all. If you want to save it into a file type the following.  
```
sqlite> .save restuarant.db
```  
In this example I've saved my table into a .db file called restuarant.  
<br>
If you've done all your commands on a .sql file, type the following command:
`.output restaurant.db`  
<br>
Here you are outputting the table and everything else you've created via that file into a separate file.
<br>
<br>
### **Leaving... and coming back?**
Once you're done and want to close up shop you can simply type:  
```
sqlite> .exit
```  
Of course if you've just used a .sql file you don't have to do anything special, just close out of the editor as you would normally.  

In order to come back/access your work again via sqlite on terminal use:
```
sqlite> .open restuarant.db
```  
### **Housekeeping**
These here are some cool stuff you can do:
- `select [COL] from [TABLE]` returns the specified column
- `select [COL] from [TABLE] where [COL] [ARGUMENT]` returns specified columns that validate the argument
  * ex: return all foods whose prices are less than 20.00
- `.mode` changes the formatting
  * ex: `.mode html` = html (I would also include markdown but it seems to not be included for SQLite3?)
- `.table` lists all the tables you have created
- `.schema` shows the command you used to create it (useful for seeing what each column has)
- `.show` shows important settings
  * ex: the filename, the width, the mode, etc
- `.help` ***MOST IMPORTANT*** shows you all the commands that you can do

---
### Resources
* [sqlite](https://sqlite.org/cli.html)
* Experimentations via your's truly :3 (Faiza duh)

---

Accurate as of (last update): 2022-10-25

#### Contributors:  
Crazy Chatting Chickens  
Faiza Huda, pd2  
Vivian Graeber, pd2  
Kevin Xiao, pd2  