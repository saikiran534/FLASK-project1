import os
from flask import Flask, render_template, redirect, url_for, request
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)


# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


@app.route("/")
def index():
    return render_template("page1.html")


  


@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/submit", methods = ["GET","POST"])
def submit():
    if request.method == "GET":
        return "Please submit the form"
    else:
        username = request.form.get("user name")
        Email = request.form.get("Email")
        Gender = request.form.get("gender")
        Date_of_Birth = request.form.get("Date Of Birth")
        Address = request.form.get("Address")
        Password = request.form.get("Password")

        return render_template("submit.html", username=username,Email=Email,Date_of_Birth=Date_of_Birth,Address=Address,password=generate_password_hash(password, method='sha256'))
        

if __name__ == "__main__":
  app.run(debug=True)
# @app.route("/login",methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         uname = request.form["uname"]
#         passwd = request.form["passwd"]
        
#         login = user.query.filter_by(username=uname, password=passwd).first()
#         if login is not None:
#             return redirect(url_for("page1"))
#     return render_template("login.html")
