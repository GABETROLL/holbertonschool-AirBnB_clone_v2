#!/usr/bin/python3
"""
URLs and their CONTENTS:

[ /states ]: Displays a UL of states
from 'storage', by their id and name,
sorted by their name.
[ /states/<id> ]: Displays a state
and all its cities' ids and names,
sorted by their name, if the 'id'
is found. Otherwise: "<H1>Not found!</H1>"

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
def reload_storage(exception):
    """
    Calls storage.close()
    (to re-load the data)
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states_page():
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


@app.route("/states/<id>", strict_slashes=False)
def state_cities_page(id):
    """
    Returns HTML page
    "templates/9-states.html"
    that contains a header of a state's
    id and name (where the state's id == 'id')
    and a UL of all its cities' names and id's
    ordered by name.
    """
    return render_template(
        "9-states.html",
        state=storage.all().get(f"State.{id}")
    )


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
