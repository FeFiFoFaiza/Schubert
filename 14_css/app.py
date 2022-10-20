from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
totally_secure = {}

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #### This breaks code bc there is no username key or any key for that fact
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    ####
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'index.html' )

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
