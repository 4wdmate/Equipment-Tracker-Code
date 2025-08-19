from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/login")
def Login():
    return render_template("log-in.html")

@app.route("/facilities")
def facilities():
    return render_template("All-Facilities.html")

@app.route("/facility/<facName>")
def facility(facName):
    facData = ???.??(facName)
    return render_template("Facility.html", facdata=facData)

@app.route("/facility/<facName>/items")
def Items(facName):
    
    return render_template("items.html", )

app.run(debug=True, port=5000)