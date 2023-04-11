#!/usr/bin/python3
"""
[ /hbnb_filters ]: Has a search filter for State's
and Amenitie's that are found in the 'storage' variable
from 'models'.

When this script is the main script,
the website is ran and hosted in
"0.0.0.0" in port 5000.
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


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
