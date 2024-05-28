from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)

@app.route("/") #oder dein dein eigener Pfad
def hello_world():  # beliebiger Funktionsname
    return render_template(
        "template.html",
        title = "Hello",
        
    )


@app.route("/hello/<string:username>")
def hello_user(username):
    return render_template(
        "template.html",
        title = "Hello",
        user = username
    )
