from flask import Flask, session, request, render_template
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask.helpers import flash

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:5432/flask'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'haeeuq1@aAU1'
db.init_app(app)


def main() :
    db.create_all()
@app.route("/")
def index():
    return render_template("page1.html")


@app.route("/home")
def home():
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
    timestamp=datetime.now()
    s= Test(name=name,password=generate_password_hash(password, method='sha256'),mobile=mobile,dob=dob,email=email,gender=gender,timestamp=timestamp)
    user = Test.query.filter_by(email=email).first()
    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return render_template('register.html')
    db.session.add(s)
    db.session.commit()
    return render_template("search.html",name=name)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/submit1",methods = ["POST"])
def submit1():
    name = request.form.get("name")
    password = request.form.get("password")
    users=Test.query.all()
    for user in users:
        if user.name==name and check_password_hash(user.password, password):

            return render_template("search.html",name =name)
        # else:
    return render_template("register.html",name = name)


@app.route("/search", methods=["POST"])
def search():
    name = request.form.get("search")
    user = upload.query.all()
    return render_template("search.html", users = user, name = name )


@app.route("/admin")
def admin(): 
    return render_template("submit.html",users = Test.query.all())

@app.route("/details/<string:id>")
def details(id):
    print(id)
    usr = upload.query.all()
    for i in usr:
        if id == i.isbn:
            a = i.isbn
            b = i.title
            c = i.author
            d = i.year
    return render_template("details.html", isbn = a, title=b,author=c,year=d)



if __name__ == "__main__" :

    with app.app_context() :
        main()
    

