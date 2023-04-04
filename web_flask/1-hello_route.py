#!/usr/bin/python3
"""
Flask website with plain text
(without paragraph tags)
that says "Hello, HBNB!" in the main page,
and "HBNB" in the path: /hbnb.

When this script is the main script,
the website is ran and hosted in
"0.0.0.0" in port 5000.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Just "Hello, HBNB!",
    without any tags sorrounding it.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    Just "HBNB",
    without any tags sorrounding it.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
