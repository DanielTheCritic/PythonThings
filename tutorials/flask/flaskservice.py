from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/person/<person_name>")
def helloPerson(person_name):
    return "Hello " + person_name