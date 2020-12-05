#Going to use Flask, going to upload through heroku
# Text is done through HTML, 
# Embedding is done through Trinket.io
# Bootstrap 4 should make it look nice
from flask import Flask, render_template   
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")    
#Each one of these routes is to a separate part of the page
if __name__ == "__main__":
    app.run(debug=True)