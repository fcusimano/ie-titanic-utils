from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__)

@app.route("/") # this url corresponds to this function
def home():
    return "Hello world!"

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    sentence = request.args["sentence"] # th
    lower = bool(request.args.get("lower",False))
    return str(tokenize(sentence, lower = lower))