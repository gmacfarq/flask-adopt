"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash, request
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_homepage():
    """Route to display homepage"""

    pets = Pet.query.all()

    return render_template('homepage.html', pets = pets)

@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        flash(f"Added {name} at {price}")
        return redirect("/add")

    else:
        return render_template(
            "snack_add_form.html", form=form)
