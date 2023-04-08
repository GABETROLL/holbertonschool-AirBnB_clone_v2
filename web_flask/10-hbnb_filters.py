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
from models.amenity import Amenity

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
    Returns HTML code for website
    with search filters for States, Cities
    and Amenities in the 'storage' storage system,
    for the AirBNB clone.

    The code itself is a copy of
    "<proj_root>/web_static/6-index.html",
    but the drop-down "popovers"'s contents
    have been changed to list the States, Cities
    and Amenities instead, respectively to what
    was already there.
    """
    return render_template(
        "10-hbnb_filters.html",
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values()
    )
