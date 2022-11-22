# TEAM APPLECAR: Abid Talukder and Faiza Huda and Ben 10 and Truthful Tom
# SoftDev
# K20: A RESTful Journey Skyward
# 2022-11-21


from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

key = None

with open('key_nasa.txt') as f:
    key = f.read()

url = "https://api.nasa.gov/planetary/apod?api_key=" + key

@app.route("/")
def dispInfo():
    r = requests.get(url)
    d = r.json()
    
    return render_template("main.html", title=d["title"],i=d["url"], description=d["explanation"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
