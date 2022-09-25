'''
SS AFK | Anson Wong, Faiza Huda, Kevin Xiao, Truthful Tom, Faizem, FamousMrTable 
Softdev 
K04 -- Dictionaries
2022-09-22
time spent: 0.8
'''
'''
DISCO:
- Typecasting is done with type(<what you're converting>)
- We got a random integer by importing random and using the function random.randint
QCC:
- We found it easier to convert to lists.
- What built-in methods are there for dictionaries?
(especially ones that could shorten what we did)
- Is there a difference in getting a random devo from a list of all devos vs
getting a random key and then a random value?
- How could we change our code to have it work with the original krewes dictionary from the care package?
- We use packages by doing <package name>.<function in package>
OPS SUMMARY:

Method 1:
    We added keys to the lists and randomly chose a period and then randomly chose a person from that period
    using the imported random method

Method 2:
    We combined all devos into one giant list and randomly selected an index/student.
    We then used the number of students in each period to see which period said index would into.

'''
#clean up line 25
import random

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "KAREN"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "WANYING"]
         }


listofkeys= list(krewes.keys()) # for when there are keys - didn't work with original krewes dictionary copied from carepkg
keyIndice = random.randint(0, len(listofkeys)-1)

valueIndice = random.randint(0, len(krewes[listofkeys[keyIndice]])-1)

print(krewes[listofkeys[keyIndice]][valueIndice] + " Of Period " + str(listofkeys[keyIndice]))

allDevos = []
for i in krewes:
    for j in krewes[i]:
        allDevos.append(j)
    
#print(allDevos)

indice = random.randint(0,len(allDevos)-1)
period = 2
stud2 = len(krewes[listofkeys[0]])
stud7 = len(krewes[listofkeys[1]])
stud8 = len(krewes[listofkeys[2]])
if (indice > stud2):
    period = 7
    if (indice > stud2 + stud7):
        period = 8
print(allDevos[indice] + " Of Period " + str(period)) #not sure if this works -Anson


# jack and jill, went up the hill, to fetch a pail of water. So they say, the subsequent fall was inevitable, they never stood a chance they were written that way/ 

# original placeholder krewes
#krewes = {2:['1', '2', '3'], 7:['4', '5', '6'], 8:['7', '8', '9']}

#print(listofkeys)

# random indices
#print(keyIndice)
#print(valueIndice)

# key values
#print(krewes[listofkeys[keyIndice]])
# the random value

# checking if it seems random by running it multiple times
#for i in range(100):
#    keyIndice = random.randint(0,2)
#    valueIndice = random.randint(0,2)
#    print(krewes[listofkeys[keyIndice]][valueIndice])