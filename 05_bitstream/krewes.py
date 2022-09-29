'''
Erasers :: Weichen, Faiza
SoftDev
K05 -- reading and using a file
2022-09-28
time spent: 0.3 hrs

DISCO: 
- We have to make a new variable that contains the list of the elements we split off the previous string

DISCO:
- Why do we have to make that new variable?
'''


import random

file1 = open("krewes.txt", 'r')
krewes = file1.read()

classes = {2:[],7:[],8:[]}

def _sort():
    krewes1 = krewes.split('@@@')
    for i in krewes1:
        ans = i.split('$$$')
        '''TESTING print(ans) '''
        _pd = ans[0]
        _name = ans[1]
        _ducky = ans[2]
        classes[int(_pd)].append([_name, _ducky])
    return

def _random():
    pd = random.choice(list(classes.keys()))
    names = random.choice(classes[pd])

    return (f"{pd} : {names[0]} : {names[1]}")


_sort()
print(_random())