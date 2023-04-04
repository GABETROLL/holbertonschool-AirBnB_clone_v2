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


@app.route("/number/<n>", strict_slashes=False)
def checks_if_n_is_a_number(n: str):
    """
    Returns "{n} is a number" HTML code, 
    ONLY if n is a valid Python3 int;
    "" HTML code otherwise.
    """
    try:
        return f"{n} is a number"
    except ValueError:
        # value error is raised when n isn't
        # a valid int string
        return ""


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
