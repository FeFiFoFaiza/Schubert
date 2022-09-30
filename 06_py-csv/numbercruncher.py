'''
Erasers | Faiza, Weichen
SoftDev
K06 -- Divine your Destiny!
2022-09-29
time spent: 0.3 hrs

DISCO: 
- random.choices() with an "s" lets you add weight to each item that it's choosing from
- it also returns a list of however many you want

QCC:
- Had to use indexing to get rid of the list return output 
'''

import random, csv

jobTitles = []
percentage = []

with open('occupations.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        jobTitles.append(row[0])
        percentage.append(float(row[1]))
#print(jobTitles)
#print(percentage)
print(random.choices(jobTitles, weights = percentage)[0])