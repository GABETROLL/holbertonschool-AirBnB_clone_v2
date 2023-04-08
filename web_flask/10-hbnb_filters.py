#!/usr/bin/python3
"""
This is it! The final challenge and therefore
final product!!!
All of our work has been leading up to this!!!
:D :D :D :D {:D 
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


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """
    """
    return render_template(
        "10-hbnb_filters.html",
        
    )
