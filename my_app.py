from flask import Flask
from flask import render_template
from flask import request
import user
app = Flask(__name__)

@app.route("/") 
def hello_world():  
    return render_template(
        "template.html",
       
        
        
    )
@app.route("/add_user", methods=["GET", "POST"])
def user_form():
    if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Username: <input type="text" name="username"></label></div>
                      <div><label>Firstname: <input type="text" name="first_name"></label></div>
                      <div><label>Lastname: <input type="text" name="last_name"></label></div>
                      <div><label>Lieblingsverein: <input type="text" name="lieblingsverein"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
    else:
        username = request.form.get("username")
        firstname = request.form.get("first_name")
        lastname = request.form.get("last_name")
        lieblingsverein = request.form.get("lieblingsverein")
        name = user.User(username, firstname, lastname, lieblingsverein)
        name.to_db()
        return f"Benutzer {username} wurde hinzugefügt"
    
@app.route("/search")
def search():
    q = request.args.get("q")
    suche = User.search(q)
    return render_template("search.html", suche=users)

@app.route("/hello/<string:username>")
def hello_user(username):
    u = user.User.from_db(username)
    return  render_template(
        "user.html",
        title = "Hello",
        name = u.firstname + u.lastname,
        verein = u.lieblingsverein
        )
    
    
