from flask import Flask, session, request, render_template
from model import *
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:5432/flask'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main() :
    db.create_all()
@app.route("/")
def index():
    return render_template("page1.html")

@app.route("/register")
def register():
  return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submit", methods = ["GET","POST"])
def submit(): 
    name = request.form.get("name")
    password = request.form.get("password")
    mobile = request.form.get("mobile")
    dob = request.form.get("dob")
    email = request.form.get("email")
    gender = request.form.get("gender")
    s= Test(name=name,password=password,mobile=mobile,dob=dob,email=email,gender=gender)
    db.session.add(s)
    db.session.commit()

    return render_template("submit.html",users = Test.query.all())



if __name__ == "__main__" :

    with app.app_context() :
        main()
