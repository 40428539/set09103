import sqlite3
import bcrypt
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session 

app = Flask(__name__)
app.secret_key = 'ILik3Ch33s3'
salt = bcrypt.gensalt()



@app.route("/")
def index():
     return render_template("index.html")

@app.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for('index'))
@app.route('/chatroom/')
def chatroom():
if (session['active'] == True) and (session['inroom'] == True) :
    return render_template('chatroom.html')
else:
    return redirect(url_for('index'))
@app.route('/hallway/')
def hallway():
if session['active'] == True :
    return render_template('hall.html')
else:
    return redirect(url_for('index'))
@app.route('/hallway/rdoor')
def rdoor():
if session['active'] == True :
        Room = request.form['rname']
        Rpast = request.form['rpass']
        RPass = bcrypt.hashpw(Past.encode('utf8'), salt)
        with sqlite3.connect("datab/dbase.db") as db:
            cursor = db.cursor()
		    for row in db.execute("SELECT RoomPass FROM RoomList WHERE RoomName = ?", [Room]):
             checkroom = row[0]
        	 if bcrypt.checkpw(Pass.encode('utf8'), checkroom):
			  session('inroom') = True
			  session('Rname') = Rname
			  db.close() 
			  return redirect(url_for('chatroom'))
			 else: 
				params = (Room, RPass)
				db.cursor().execute("INSERT INTO RoomList VALUES (?, ?)", params)
				db.commit()
				db.close()
				return redirect(url_for('hallway'))
	
	
else:
    return redirect(url_for('index'))
		
@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login/logging', methods=['post'])
def logging():
     User = request.form['user']
     Pass = request.form['pass']

     with sqlite3.connect('datab/dbase.db') as db:
         cursor = db.cursor()
         for row in db.execute("SELECT Password FROM Users WHERE Username = ?", [User]):
             checksql = row[0]
        

     if bcrypt.checkpw(Pass.encode('utf8'), checksql):
        db.close()
        session['user'] = User
        session['active'] = True


        return redirect(url_for('index'))
     else:
      db.close()   
      return redirect(url_for('login'))

@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/register/Register', methods=['post'])
def Register(): 
        User = request.form['user']
        Email = request.form['email']
        Past = request.form['pass']
        Pass = bcrypt.hashpw(Past.encode('utf8'), salt)
        with sqlite3.connect("datab/dbase.db") as db:
            cursor = db.cursor()
            params = (User, Email, Pass)
        db.cursor().execute("INSERT INTO Users VALUES (?, ?, ?)", params)
        db.commit()
        db.close()
        return redirect(url_for('login'))

if __name__=='__main__':
    socketio.run(app, debug=True)
