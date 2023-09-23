#!/usr/bin/python3
"""
A script that starts a Flask Web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    returns a text when the app is accessed from the root directory
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns a string from the route /hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
