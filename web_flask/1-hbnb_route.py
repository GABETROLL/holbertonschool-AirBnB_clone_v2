#!/usr/bin/python3
"""
Flask website

When this script is the main script,
the website is ran and hosted in
"0.0.0.0" in port 5000.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns just "Hello, HBNB!" HTML code,
    without any tags sorrounding it.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def just_hbnb():
    """
    Returns just "HBNB" HTML code,
    without any tags sorrounding it.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
