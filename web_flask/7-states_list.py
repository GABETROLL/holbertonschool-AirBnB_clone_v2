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
from models import storage

storage.all()
app = Flask(__name__)


@app.teardown_appcontext
def states_list():
    """
    Calls storage.close()
    (to re-load the data)
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template(
        "7-states_list.html",
        states_list=sum(
            (f"<LI>{obj.id}: <B>{obj.name}</B></LI>"
             for obj in storage.all().values()
            ),
            start=""
        )
    )


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
