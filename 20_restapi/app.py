'''
SEXIST

'''


from flask import Flask, render_template, request
import urllib
import json

app = Flask(__name__)

key = None

with open('key_nasa.txt') as f:
    key = f.read()

print(key)



@app.route("/")
def dispInfo():
    return True



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()