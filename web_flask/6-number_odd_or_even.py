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
[ /number/<int:n> ]: Only valid when 'n' is an int,
    and it contains f"{n} is a number"
[ /number_template/<int:n> ]: Only valid when in is an int,
    and it contains f"Number: {n}"

When this script is the main script,
the website is ran and hosted in
"0.0.0.0" in port 5000.
"""
from flask import Flask, render_template

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


# only validates the link if it's a valid int,
# otherwise, 404
@app.route("/number/<int:n>", strict_slashes=False)
def checks_if_n_is_a_number(n: str):
    """
    <ONLY GETS USED BY "app.route" IF N IS A
    VALID INTEGER>
    Returns "{n} is a number" HTML code.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def first_html_file_also_integer(n: str):
    """
    <ONLY GETS USED BY "app.route" IF N IS A
    VALID INTEGER>
    Returns the text in "templates/5-number.html"
    with 'n' in place of the '{{n}}', using
    flask.render_template
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def int_is_odd_or_even(n: str):
    """
    <ONLY GETS USED BY "app.route" IF N IS A
    VALID INTEGER>
    Returns the text in "templates/6-number_odd_or_even.html",
    like last time, with 'n' in place of the '{{n}}', and
    with 'odd' or 'even' in place of the '{{odd_or_even}}', using
    flask.render_template.
    """
    return render_template("6-number_odd_or_even.html", odd_or_even=(
            "odd" if int(n) % 2 == 1 else "even"
        )
    )

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
