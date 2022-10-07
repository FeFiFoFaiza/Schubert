import csv
import random
from flask import Flask

jobs = {}
app = Flask(__name__)

##opens and prints out content of csv
with open("./occupations.csv", 'r') as file:
  csvreader = csv.reader(file)
  line_count = 0
  for row in csvreader:
      if line_count != 0:
          ##print(row)
          jobs[row[0]] = float(row[1])
      line_count = line_count + 1
  del jobs["Total"]
  ##for e in jobs:
  ##    print(e)

#print random job from jobs dict
def choose_job(jobs: dict):
    return random.choices(list(jobs), weights = list(jobs.values()))[0]
    
#display page
@app.route("/")
def page():
    randomJob = choose_job(jobs)
    jobsString = ',\n'.join(list(jobs))
    s = f'''
    <!doctype html>
    <head>
    DTurt: Sam, Faiza, Hui
    Softdev Period 2
    k08
    2022-10-06
    Time Spent: 0.3
    </head>
    <body>
    {randomJob}

    {jobsString}
    </body>
    '''
    s = '<br>'.join(s.split("\n"))
    return s

app.run()