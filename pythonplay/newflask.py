from flask import Flask
app = Flask(__name__)
@app.route('/')

def wthtml():

 string = """<html><head><title>Test html page</title></head>
 <body>
 <h2> First Python Webpage  </h2>
 <p> I hope it works!!  </p>
 </body>
 </html>
 """
 return string

  
wthtml()
