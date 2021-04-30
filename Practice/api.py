from flask import Flask, session, request, render_template, jsonify
from flask.helpers import flash
from model import *
from sqlalchemy import or_


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:5432/flask'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "baukfb13256$%^sfqu3oeghroq"

db.init_app(app)

def main() :
    db.create_all()


@app.route('/api/search/<string:input>')
def booksApi(input):
    a= hello.query.all()
    details =[]
    flag = 0
    for c in a:
        value={}
        if c.isbn == input or c.title==input or c.author == input or c.year == input:
            value["isbn"]=c.isbn
            value["author"]=c.author
            value["title"]=c.title
            value["year"]=c.year
            details.append(value)
            flag = 1
    if flag == 0:
        return jsonify({"error":"book not found"}), 404

    return jsonify({"Book details are ":details}), 200

@app.route('/api/review/<string:rating>')
def review(rating):
    a = Review.query.all()
    details = []
    flag = 0
    for c in a:
        value={}
        if rating == c.rating or rating==c.user or rating == c.isbn or rating ==c.review:
            value["user"]=c.user
            value["isbn"]=c.isbn
            value["rating"]=c.rating           
            value["review"]=c.review 
            details.append(value)
            flag = 1
    if flag ==0:
        return jsonify({"error":"book not found"}), 404

    return jsonify({"Review Details are ":details}), 200