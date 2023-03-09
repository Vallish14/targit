from flask import *

app = Flask(__name__) 

@app.route("/") 

@app.route("/home")
def home():
    asset = "home.html"
    return render_template(asset)

if __name__ == "__main__": 
    app.run(debug=True,port=4949)
