from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    return render_template("home.html")

app.run(debug=True, port=5000)