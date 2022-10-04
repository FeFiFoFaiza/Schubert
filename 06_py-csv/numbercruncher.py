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

_storeValues = {0:[], 1:[]}

with open('occupations.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "Job Class" and row[0] != "Total":
            _storeValues[0].append(row[0])
            _storeValues[1].append(float(row[1]))


print(random.choices(_storeValues[0], weights = _storeValues[1])[0])