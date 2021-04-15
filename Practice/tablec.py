from models import *
from flask import Flask

# from app import app,db

import csv

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:5432/flask'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# db.create_all()

def main():
    db.create_all()






if __name__=='__main__':
    with app.app_context() :
        main()
