"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash, request
import requests
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm
from dotenv import load_dotenv
from pet_finder import update_auth_token_string, get_pet_data

load_dotenv()


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

auth_token = None

@app.before_request
def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = update_auth_token_string()


@app.get('/')
def show_homepage():
    """Route to display homepage"""

    pets = Pet.query.all()

    return render_template('homepage.html', pets = pets)

@app.route("/add", methods=["GET", "POST"])
def show_add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data.lower()
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,
                  species=species,
                  photo_url=photo_url,
                  age=age,
                  notes=notes
                 )

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/add")

    else:
        return render_template(
            "pet-add-form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_edit_pet(pet_id):
    """Pet edit form; handle editing."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Edited {pet.name}")
        return redirect(f"/{pet_id}")

    else:
        return render_template(
            "pet-edit-form.html", form=form, pet=pet)

def store_pets():
    resp = requests.get("https://api.petfinder.com/v2/oauth2/token",
        params={"grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET
                })
    return resp.json().get("access_token")

@app.get("/save-pet")
def get_random_pet():
    """Pulls in pet data and adds it to database"""

    pet = get_pet_data()
    db.session.add(pet)
    db.session.commit()

