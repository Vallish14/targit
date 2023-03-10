from flask import *
import os

app = Flask(__name__) 

def does_assest_exist(asset):
    return os.path.isfile(f"./static/{asset}")

@app.route("/") 

@app.route("/home")
def home():
    asset = "home.html"
    if not does_assest_exist(asset):
        return false 
    return render_template(asset)

if __name__ == "__main__": 
    app.run(debug=True,port=4949) #running flask (Initalised on line 4)
