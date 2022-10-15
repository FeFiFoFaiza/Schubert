# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso pero queso es muy fabuloso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.

@app.route("/shh_test")
def french():
    return render_template('01_testing_tmplt.html')
if __name__ == "__main__":
    app.debug = True
    app.run()
