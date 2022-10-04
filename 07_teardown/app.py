'''
SS AFK | Anson Wong, Faiza Huda, Kevin Xiao, Truthful Tom, Faizem, FamousMrTable 
Softdev 
K07 -- TearDown
2022-10-04-2022
time spent: 0.5 hour
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. A java overloaded constructor.
1. Separating and used in directory path and URLs.
2. The print statement should print the URL or link to the website created by the flask , as __name__ is probably a container that stores the website information
inside the terminal for easy access for the user.
3. Prints the URL/ link to the website
4. On the website, because we tested it and it does appear on the website.
5. Running methods in java requires an object with the class calling upon methods within the class, and app.run() looks very familiar to OOP.
...
INVESTIGATIVE APPROACH:

We were kool kids and didn't use the internet and instead bash our heads into the wall multiple times trying to figure out what flask even is, and after multiple tests
we concluded that it's very similar to java's object oriented programming with its incorperation of constructions and using objects to call upon methods. 
'''