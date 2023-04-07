#!/usr/bin/python3
"""
URLs and their CONTENTS:

[ /cities_by_states ]: Displays a UL of
    LI's of states
    from 'storage', by their id and name,
    sorted by their name,
    AND a UL of
        LI's of all the state's cities,
        also sorted by their name, and also
        from 'storage'.

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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    return render_template(
        "8-cities_by_state.html",
        states=storage.all(State).values()
    )
