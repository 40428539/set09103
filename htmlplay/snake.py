from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def base():

    
    return render_template("index.html")

@app.route('/link1/')
def link1():
    return render_template('link1.html')

@app.route('/link2/')
def link2():
    return render_template('link2.html')
