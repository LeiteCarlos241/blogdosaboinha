from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "hello world"