from flask import Flask, session, request, render_template
from models import *
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



@app.route("/search", methods=["POST"])
def search():
    name = request.form.get("search")
    user = upload.query.all()
    for i in user:
        if i.isbn==name:
            return render_template("search.html",isbn = i.isbn,title=i.title,author=i.author,year=i.year)
        # else:
    return render_template("hello.html")




@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/home")
def home():
    return render_template("page1.html")

@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/submit1",methods = ["POST"])
def submit1():
    name = request.form.get("name")
    password = request.form.get("password")
    users=Test.query.all()
    for user in users:
        if user.name==name and user.password==password:
            return render_template("search.html",name =name)
        else:
            return render_template("register.html",name = name)


@app.route("/admin")
def admin(): 
    return render_template("submit.html",users = Test.query.all())





    
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

    return render_template("search.html",name=name)



if __name__ == "__main__" :

    with app.app_context() :
        main()
