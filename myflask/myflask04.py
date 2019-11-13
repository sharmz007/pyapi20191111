#!/usr/bin/python3

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

@app.route("/start")
def start():
    return render_template("postmaker.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("nm")
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    return redirect(url_for("success", name = user)) # pass back to /success with val for name

if __name__ == "__main__":
    app.run(port=5006)
