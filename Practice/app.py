from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("page1.html")
    
@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        page = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("page1"))
    return render_template("login.html")

