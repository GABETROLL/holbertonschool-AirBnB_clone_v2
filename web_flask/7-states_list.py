#!/usr/bin/python3
"""
URLs and their CONTENTS:

[ /states_list ]: Displays a UL of states
from 'storage', by their id and name,
sorted by their name.

(For more info on how the cities and states
are connected, look at
models/state.py,
models.citiy.py
and models/engine)

When this script is the main script,
the website is ran and hosted in
"0.0.0.0" in port 5000.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def reload_states_list(exception):
    """
    Calls storage.close()
    (to re-load the data)
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list_page():
    """
    Returns HTML page
    "templates/7-states_list.html"
    with a UL of states in 'storage'
    listed by their id and their name.
    """
    return render_template(
        "7-states_list.html",
        states=storage.all(State).values()
    )


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
