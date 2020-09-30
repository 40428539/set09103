from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def base():

    
    return render_template("index.html", content="""

            <p> This is a paragraph but will probably 
            end up being a nav bar </p>



            """ )

