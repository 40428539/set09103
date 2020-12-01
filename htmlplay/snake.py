import sqlite3
from flask import Flask, render_template, request 
app = Flask(__name__)
@app.route("/")
def index():

    
    return render_template("index.html")

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login/logging', methods=['post'])
def logging():
     User = request.form['user']
     Pass = request.form['pass']

     if User=="Admin" and Pass=="Admin":
      return render_template("index.html")
     else:
      return render_template('login.html')


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/register/Register', methods=['post'])
def Register(): 
        User = request.form['user']
        Email = request.form['email']
        Pass = request.form['pass']
        with sqlite3.connect("datab/dbase.db") as db:
            cursor = db.cursor()
        adduser = ("INSERT INTO Users (Username, Email, Password) VALUES ( 'User', 'Email', 'Pass')")
        db.cursor().execute(adduser)
        db.commit()
        return render_template('login.html')
