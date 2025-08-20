from flask import Flask, render_template, request, session, redirect
import DB_Acess

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("log-in.html")

@app.route("/facilities")
def facilities():
    AllFacilities = DB_Acess.GetAllFacilities()
    print('test' + str(AllFacilities))
    return render_template("All-Facilities.html", facilities=AllFacilities)

@app.route("/facility/<facName>")
def facility(facName):
    facData = facName
    return render_template("Facility.html", facdata=facData)

@app.route("/facility/<facName>/loan")
def loan(facName):
    facData = facName
    return render_template("Facility.html", facdata=facData)

@app.route("/facility/<facName>/items")
def items(facName):
    return render_template("items.html", )

@app.route("/facility/<facName>/items/(itemID)")
def item(facName, itemID):
    return render_template("individual_item.html", )

app.run(debug=True, port=5000)