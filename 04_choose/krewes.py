'''
SS AFK | Anson Wong, Faiza Huda, Kevin Xiao, Truthful Tom, Faizem, FamousMrTable 
Softdev P2
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
OPS SUMMARY:
We decided to make a list of the keys and then randomly choose from that list
because they aren't numerically sequential. After that, we got a random index for both 
the list of keys and the list of values. With those, we got a random devo in a random period. 
'''

import random

krewes = {2:['1', '2', '3'], 7:['4', '5', '6'], 8:['7', '8', '9']}

listofkeys= list(krewes.keys())
keyIndice = random.randint(0,2)
valueIndice = random.randint(0,2)

#print(listofkeys)

# random indices
#print(keyIndice)
#print(valueIndice)

# key values
#print(krewes[listofkeys[keyIndice]])
# the random value
print(krewes[listofkeys[keyIndice]][valueIndice])

# checking if it seems random by running it multiple times
#for i in range(100):
#    keyIndice = random.randint(0,2)
#    valueIndice = random.randint(0,2)
#    print(krewes[listofkeys[keyIndice]][valueIndice])