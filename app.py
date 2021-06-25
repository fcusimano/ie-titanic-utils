from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__)

@app.route("/") # this url corresponds to this function
def home():
    return {
        "message": "Hello world!",
        "version": "0.1",
    }

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    sentence = request.args["sentence"] # th
    lower = bool(request.args.get("lower",False))
    return str(tokenize(sentence, lower = lower))


if __name__ == "__main__":
    import os # to access Heroku environment variables
    port = int(os.environ["PORT"])
    app.run(host="0.0.0.0",port=port)