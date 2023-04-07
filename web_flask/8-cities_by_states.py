#!/usr/bin/python3
"""
"""
from flask import Flask, render_template
from models import storage

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
        states=sorted(
            storage.all().values(),
            key=lambda state: state.name
        )
    )