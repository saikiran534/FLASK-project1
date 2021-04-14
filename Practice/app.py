import os
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from model import *
# from sqlalchemy.testing.config import db
# from jinja2.nodes import Test
# import psycopg2
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:5432/flask'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


    



@app.route("/")
def index():
  db.create_all()
  return render_template("page1.html")

@app.route("/register")
def register():
  return render_template("register.html")

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

    return render_template("submit.html", name=name, password=generate_password_hash(password, method='sha256'), mobile=mobile, dob=dob, email=email, gender=gender)
    
    
    if __name__ == "__main__":
      app.run(debug=True)

    # username = request.form.get("username")
    # Email = request.form.get("Email")
    # Gender = request.form.get("gender")
    # Date_of_Birth = request.form.get("DateofBirth")
    # Address = request.form.get("Address")
    # Password = request.form.get("Password")
    # print (username)
    # return render_template("submit.html", username=username, Email=Email, Gender=Gender, Date_of_Birth=Date_of_Birth, Address=Address, Password=Password)
        #generate_password_hash(Password, method='sha256)

# if __name__ == "__main__":
#   app.run(debug=True)
  
# @app.route("/login",methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         uname = request.form["uname"]
#         passwd = request.form["passwd"]
        
#         login = user.query.filter_by(username=uname, password=passwd).first()
#         if login is not None:
#             return redirect(url_for("page1"))
#     return render_template("login.html")
