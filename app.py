from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Mackenzie!!! Meu nome é Sophia <3 "
