#!/usr/bin/python3
"""
URLs and their CONTENTS:

[ / ]: "Hello, HBNB!" without any tags sorrounding it
[ /hbnb ]: "HBNB" without any tags sorrounding it
[ /c/<text> ]: f"C {text}" without any tags sorrounding it
[ /python/<text> ]: f"Python {text} without any tags sorrounding it.
    It also gets rid of all the underscores in 'text'
    and replaces them with spaces.
    If there's no "<text>" nor "/<text>", the default 'text' is:
    "is_cool"

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


@app.route("/c/<text>", strict_slashes=False)
def things_about_c(text: str):
    """
    Returns "C {text}" HTML code ,
    replacing all underscores
    in the {text} variable with spaces
    (no HTML tags)
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def things_about_python(text: str = "is_cool"):
    """
    Returns "Python {text}" HTML code ,
    replacing all underscores
    in the {text} variable with spaces
    (no HTML tags)
    """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
