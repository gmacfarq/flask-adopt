"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import (StringField, URLField,
                    BooleanField, SelectField, TextAreaField)


class AddPetForm(FlaskForm):

    name = StringField("Name")
    species = StringField("Species")
    photo_url = URLField("Profile Picture")
    age = SelectField("Age Group")
    notes = StringField("Notes")