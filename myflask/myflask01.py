#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_root():
    return "Hello Root\n"

@app.route("/hello")
def hello_world():
   return "Hello World"
app.add_url_rule("/test", "test", hello_world)
app.add_url_rule("/newtest", "newtest", hello_world)
app.add_url_rule("/new", "newtest", hello_world)

if __name__ == "__main__":
   app.run(port=5008) # runs the application
   # app.run(port=5006, debug=True) # DEBUG MODE

