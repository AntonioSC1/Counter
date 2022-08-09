
from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "No secrets for Batman"

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/add")
def add():
    session['count'] += 1
    return redirect("/")

@app.route("/user_input", methods=["POST"])
def user_input():
    num = int(request.form["num"])
    session["count"] += num -1
    return redirect("/")

@app.route("/")
def index():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)