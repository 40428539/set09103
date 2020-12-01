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
