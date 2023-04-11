#!/usr/bin/python3
"""
[ /hbnb ]: HBNB's main page, everyone!!!
    The page contains 'States' and 'Amenities'
    filters with a search button,
    and different places to stay
    with prices by night,
    name, description, reviews, number of
    bathrooms, bedrooms and max allowed guests,
    and the user who is offering it.

When this script is the main script,
the website is ran and hosted in
"0.0.0.0" in port 5000.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def reload_storage(exception):
    """
    Calls storage.close()
    (to re-load the data)
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def its_alive_omg():
    """
    Returns the HBNB's main page, everyone!!!
    The page contains 'States' and 'Amenities'
    filters with a search button,
    and different places to stay
    with prices by night,
    name, description, reviews, number of
    bathrooms, bedrooms and max allowed guests,
    and the user who is offering it.
    """
    return render_template(
        "100-hbnb.html",
        states=storage.all(State),
        amenities=storage.all(Amenity),
        places=storage.all(Place)
    )


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)