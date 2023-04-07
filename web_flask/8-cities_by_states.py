#!/usr/bin/python3
"""
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
